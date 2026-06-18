from threading import Thread
from time import sleep
from showSeat import ShowSeat
from showSeatStatus import ShowSeatStatus

class ShowSeatLockReleaser(Thread):
    """
    Sets the seat status back to AVAILABLE after lock timeout.
    """

    def __init__(self, showSeat: ShowSeat, seatLockTimeout: int):
        super().__init__()
        self.showSeat = showSeat
        self.seatLockTimeout = seatLockTimeout

    def run(self):
        sleep(self.seatLockTimeout)
        self.showSeat.lock.acquire()
        if self.showSeat.status == ShowSeatStatus.LOCKED:
            self.showSeat.status = ShowSeatStatus.AVAILABLE
            print(f"Lock on seat {self.showSeat.seat.seatNumber} is automatically removed due to timeout")
        self.showSeat.lock.release()