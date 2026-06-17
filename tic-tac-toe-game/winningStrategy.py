from abc import ABC, abstractmethod
from symbol import Symbol
from typing import List

class WinningStrategy(ABC):
    @abstractmethod
    def check(self, board: List[List[Symbol]], symbol: Symbol) -> bool:
        raise NotImplemented("The subclass must implement the 'check' method")