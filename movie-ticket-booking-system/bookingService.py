from typing import List, TYPE_CHECKING
from ticket import Ticket
from showSeatStatus import ShowSeatStatus

if TYPE_CHECKING:
    from showSeat import ShowSeat
    from show import Show
    from user import User

class SeatLockFailedException(Exception):
    def __init__(self):
        super().__init__("Failed to lock the seat")

class BookingService:
    def lockShowSeats(self, showSeats: List['ShowSeat']):
        for showSeat in showSeats:
            if showSeat.status == ShowSeatStatus.AVAILABLE:
                showSeat.status = ShowSeatStatus.LOCKED
            else:
                raise SeatLockFailedException()

    def confirmBooking(self, show: 'Show', showSeats: List['ShowSeat'], user: 'User'):
        for showSeat in showSeats:
            showSeat.status = ShowSeatStatus.BOOKED
        ticket = Ticket(show, showSeats, user)
        return ticket