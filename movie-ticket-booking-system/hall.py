from typing import TYPE_CHECKING, List
from idGenService import IdGenService

if TYPE_CHECKING:
    from cinema import Cinema
    from seat import Seat

class Hall:
    def __init__(self, hallNumber: str, cinema: 'Cinema', seats: List['Seat'] = []):
        self.id = IdGenService.generate()
        self.hallNumber = hallNumber
        self.cinema = cinema
        self.seats = seats

    def addSeat(self, seat: 'Seat'):
        self.seats.append(seat)