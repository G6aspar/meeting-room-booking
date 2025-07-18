from datetime import datetime

class BookingService:
    def __init__(self, reservation_repo, user_repo, room_repo):
        self.reservation_repo = reservation_repo
        self.user_repo = user_repo
        self.room_repo = room_repo

    def is_room_available(self, room_id: int, start: datetime, end: datetime) -> bool:
        for reservation in self.reservation_repo.get_all():
            if reservation.room_id == room_id:
                if not (end <= reservation.start or start >= reservation.end):
                    return False
        return True

    def create_reservation(self, user_id: int, room_id: int, start: datetime, end: datetime):
        if not self.user_repo.get(user_id):
            raise Exception("Usuario no encontrado")
        if not self.room_repo.get(room_id):
            raise Exception("Sala no encontrada")
        if not self.is_room_available(room_id, start, end):
            raise Exception("La sala no está disponible en ese horario")

        from src.models.reservation import Reservation
        reservation = Reservation(0, user_id, room_id, start, end)
        reservation_id = self.reservation_repo.add(reservation)
        reservation.reservation_id = reservation_id
        return reservation_id

    def get_reservations_by_user(self, user_id: int):
        return self.reservation_repo.get_by_user(user_id)

    def get_reservations_by_room(self, room_id: int):
        return self.reservation_repo.get_by_room(room_id)