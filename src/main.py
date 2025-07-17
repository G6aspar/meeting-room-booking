from datetime import datetime
from src.repositories.user_repository import UserRepository
from src.repositories.room_repository import RoomRepository
from src.repositories.reservation_repository import ReservationRepository
from src.services.booking_service import BookingService
from src.models.user import User
from src.models.room import Room

user_repo = UserRepository()
room_repo = RoomRepository()
reservation_repo = ReservationRepository()
service = BookingService(reservation_repo, user_repo, room_repo)

# Crear usuario
user_id = user_repo.add(User(0, "Juan", "juan@example.com"))
room_id = room_repo.add(Room(0, "Sala A", 10))

# Hacer reserva
start = datetime(2025, 7, 20, 10, 0)
end = datetime(2025, 7, 20, 11, 0)

try:
    res_id = service.create_reservation(user_id, room_id, start, end)
    print(f"Reserva creada con ID: {res_id}")
except Exception as e:
    print("Error al crear reserva:", e)