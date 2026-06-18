from typing import TYPE_CHECKING
from showSeatStatus import ShowSeatStatus
from idGenService import IdGenService
from threading import Lock

if TYPE_CHECKING:
    from seat import Seat
    from show import Show


class ShowSeat:
    def __init__(self, seat: 'Seat', show: 'Show', price: float = 0.0):
        self.id = IdGenService.generate()
        self.seat = seat
        self.show = show
        self.status = ShowSeatStatus.AVAILABLE
        self.price = price
        self.lock = Lock()