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

# Crear usuario y sala
user_id = user_repo.add(User(0, "Juan", "juan@example.com"))
room_id = room_repo.add(Room(0, "Sala A", 10))

# Hacer una reserva válida
start = datetime(2025, 7, 20, 10, 0)
end = datetime(2025, 7, 20, 11, 0)

try:
    res_id = service.create_reservation(user_id, room_id, start, end)
    print(f"Reserva creada con ID: {res_id}")
except Exception as e:
    print("Error al crear reserva:", e)

# Mostrar reservas por usuario
print("\nReservas del usuario:")
for r in service.get_reservations_by_user(user_id):
    print(f"Reserva {r.reservation_id}: Sala {r.room_id} de {r.start} a {r.end}")

# Mostrar reservas por sala
print("\nReservas de la sala:")
for r in service.get_reservations_by_room(room_id):
    print(f"Reserva {r.reservation_id}: Usuario {r.user_id} de {r.start} a {r.end}")

# CRUD: Update usuario
user = user_repo.get(user_id)
user.name = "Juan Pérez"
user_repo.update(user_id, user)

# CRUD: Delete sala
room_repo.delete(room_id)
print("\nSala eliminada correctamente.")

# Verificar que la sala fue eliminada
print("\nSalas restantes:")
for room in room_repo.get_all():
    print(f"Sala {room.room_id}: {room.name}")