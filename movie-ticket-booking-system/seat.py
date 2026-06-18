from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from seatType import SeatType

class Seat:
    def __init__(self, seatNumber: str, seatType: 'SeatType'):
        self.seatNumber = seatNumber
        self.seatType = seatType
