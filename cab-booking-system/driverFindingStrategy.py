from typing import Dict, List
from abc import ABC, abstractmethod
from ride import Ride
from driver import Driver


class DriverFindingStrategy(ABC):
    @abstractmethod
    def findDrivers(self, ride: Ride, drivers: Dict[str, Driver]) -> List[Driver]:
        raise NotImplementedError()
