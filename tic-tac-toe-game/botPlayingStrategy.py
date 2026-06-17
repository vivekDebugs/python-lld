from abc import ABC, abstractmethod
from typing import List, Tuple
from symbol import Symbol

class BotPlayerStrategy(ABC):
    @ abstractmethod
    def play(self, board: List[List[Symbol]]) -> Tuple[int, int]:
        raise NotImplemented("The subclass must implement the 'play' method")