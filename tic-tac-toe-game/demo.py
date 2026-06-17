from game import Game
from botPlayer import BotPlayer
from symbol import Symbol
from botDifficulty import BotDifficulty
from rowWinningStrategy import RowWinningStrategy
from columnWinningStrategy import ColumnWinningStrategy
from diagonalWinningStrategy import DiagonalWinningStrategy
from randomBotPlayingStrategy import RandomBotPlayingStrategy
from obtimisedBotPlayingStrategy import ObtimisedBotPlayingStrategy

class Demo:
    def run(self):
        self.game = Game()

        self.game.createBoard(3)

        # adding players
        botPlayer1 = BotPlayer(BotDifficulty.EASY, Symbol.X, RandomBotPlayingStrategy())
        botPlayer2 = BotPlayer(BotDifficulty.EASY, Symbol.O, ObtimisedBotPlayingStrategy())
        self.game.addPlayer(botPlayer1)
        self.game.addPlayer(botPlayer2)

        # adding winning strategies
        rowWinningStrategy = RowWinningStrategy()
        columnWinningStrategy = ColumnWinningStrategy()
        diagonalWinningStrategy = DiagonalWinningStrategy()
        self.game.addWinningStrategy(rowWinningStrategy)
        self.game.addWinningStrategy(columnWinningStrategy)
        self.game.addWinningStrategy(diagonalWinningStrategy)

        # starting the game
        self.game.start()

if __name__ == "__main__":
    demo = Demo()
    demo.run()