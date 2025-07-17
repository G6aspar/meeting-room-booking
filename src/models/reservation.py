from datetime import datetime

class Reservation:
    def __init__(self, reservation_id: int, user_id: int, room_id: int, start: datetime, end: datetime):
        self.reservation_id = reservation_id
        self.user_id = user_id
        self.room_id = room_id
        self.start = start
        self.end = end