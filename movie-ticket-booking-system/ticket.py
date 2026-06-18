from typing import TYPE_CHECKING, List
from datetime import datetime

if TYPE_CHECKING:
    from show import Show
    from showSeat import ShowSeat
    from user import User

class Ticket:
    def __init__(self, show: 'Show', showSeats: List['ShowSeat'], user: 'User'):
        self.show = show
        self.showSeats = showSeats
        self.user = user
        self.bookingTime = datetime.now()

    def printTicket(self):
        print("Movie: " + self.show.movie.name)
        print("Timing: " + str(self.show.startTime))
        print("Cinema: " + self.show.hall.cinema.name)
        print("Hall: " + self.show.hall.hallNumber)
        print("Seats: " + f"{''.join([showSeat.seat.seatNumber for showSeat in self.showSeats])}")
        print("Booking time: " + str(self.bookingTime))