from typing import List, TYPE_CHECKING
from ticket import Ticket
from showSeatStatus import ShowSeatStatus
from showSeatLockReleaser import ShowSeatLockReleaser

if TYPE_CHECKING:
    from showSeat import ShowSeat
    from show import Show
    from user import User

class SeatLockFailedException(Exception):
    def __init__(self):
        super().__init__("Failed to lock the seat")

class SeatNotLockedException(Exception):
    def __init__(self):
        super().__init__("Seat is not locked")

class BookingService:
    def __init__(self):
        self.SEAT_LOCK_TIMEOUT = 5

    def lockShowSeats(self, showSeats: List['ShowSeat']):
        for showSeat in showSeats:
            showSeat.lock.acquire()
            ShowSeatLockReleaser(showSeat, self.SEAT_LOCK_TIMEOUT).start()
            if showSeat.status == ShowSeatStatus.AVAILABLE:
                showSeat.status = ShowSeatStatus.LOCKED
                showSeat.lock.release()
            else:
                showSeat.lock.release()
                raise SeatLockFailedException()

    def confirmBooking(self, show: 'Show', showSeats: List['ShowSeat'], user: 'User'):
        for showSeat in showSeats:
            showSeat.lock.acquire()
            if showSeat.status == ShowSeatStatus.LOCKED:
                showSeat.status = ShowSeatStatus.BOOKED
                showSeat.lock.release()
            else:
                showSeat.lock.release()
                raise SeatNotLockedException()
        ticket = Ticket(show, showSeats, user)
        return ticket