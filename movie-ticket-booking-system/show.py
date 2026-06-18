from typing import TYPE_CHECKING, List, Dict
from datetime import datetime
from showSeat import ShowSeat
from idGenService import IdGenService

if TYPE_CHECKING:
    from movie import Movie
    from hall import Hall
    from seatType import SeatType

class Show:
    def __init__(self, movie: 'Movie', hall: 'Hall', startTime: datetime):
        self.id = IdGenService.generate()
        self.movie = movie
        self.hall = hall
        self.startTime = startTime
        self.showSeats: List['ShowSeat'] = []

    def initShowSeats(self, seatPrices: Dict['SeatType', float]):
        for seat in self.hall.seats:
            price = seatPrices[seat.seatType] # <- can use strategy pattern here
            self.showSeats.append(ShowSeat(seat, self, price))