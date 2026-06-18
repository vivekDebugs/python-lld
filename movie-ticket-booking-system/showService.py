from typing import TYPE_CHECKING, List
from show import Show
from datetime import datetime

if TYPE_CHECKING:
    from movie import Movie
    from hall import Hall
    from showSeat import ShowSeat

class ShowService:
    def createShow(self, movie: 'Movie', hall: 'Hall', startTime: datetime) -> Show:
        show = Show(movie, hall, startTime)
        movie.addShow(show)
        return show

    def getShowSeats(self, show: Show, showSeatNumbers: List[str]) -> List['ShowSeat']:
        showSeats = []
        for showSeat in show.showSeats:
            if showSeat.seat.seatNumber in showSeatNumbers:
                showSeats.append(showSeat)
        return showSeats
