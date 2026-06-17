from player import Player
from botDifficulty import BotDifficulty
from playerType import PlayerType
from symbol import Symbol
from botPlayingStrategy import BotPlayerStrategy

class BotPlayer(Player):
    def __init__(self, difficulty: BotDifficulty, symbol: Symbol, playingStrategy: BotPlayerStrategy):
        super().__init__(PlayerType.BOT, symbol)
        self.difficulty = difficulty
        self.playingStrategy = playingStrategy

    def play(self, board):
        return self.playingStrategy.play(board)