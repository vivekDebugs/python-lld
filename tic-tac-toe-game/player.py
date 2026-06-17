from abc import ABC, abstractmethod
from typing import Tuple, List
from playerType import PlayerType
from symbol import Symbol

class Player(ABC):
    def __init__(self, playerType: PlayerType, symbol: Symbol):
        self.playerType = playerType
        self.symbol = symbol

    @abstractmethod
    def play(board: List[List[Symbol]]) -> Tuple[int, int]:
        raise NotImplemented("The subclass must implement the 'play' method")