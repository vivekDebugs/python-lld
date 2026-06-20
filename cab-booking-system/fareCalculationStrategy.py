from abc import ABC, abstractmethod
from ride import Ride

class FareCalculationStrategy(ABC):
    @abstractmethod
    def calculateFare(self, ride: Ride) -> float:
        raise NotImplementedError()
