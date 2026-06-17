from player import Player
from playerType import PlayerType
from typing import List
from symbol import Symbol

class HumanPlayer(Player):
    def __init__(self, name: str, email: str, symbol: Symbol):
        super().__init__(PlayerType.HUMAN, symbol)
        self.name = name
        self.email = email

    def play(board):
        return super().play()