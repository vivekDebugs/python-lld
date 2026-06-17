from player import Player
from typing import List
from winningStrategy import WinningStrategy
from symbol import Symbol

class Game:
    def __init__(self):
        self.players: List[Player] = []
        self.winningStrategies: List[WinningStrategy] = []
        self.board: List[List[Symbol]] = None

    def addPlayer(self, player: Player):
        self.players.append(player)

    def addWinningStrategy(self, winningStrategy: WinningStrategy):
        self.winningStrategies.append(winningStrategy)

    def createBoard(self, size: int):
        self.board = [[None for j in range(size)] for i in range(size)]

    def checkResult(self, symbol: Symbol):
        for winningStrategy in self.winningStrategies:
            if winningStrategy.check(self.board, symbol):
                return True
        return False

    def isDraw(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] is None:
                    return False
        return True

    def printBoard(self):
        for i in range(len(self.board)):
            print(end="|")
            for j in range(len(self.board[i])):
                val = self.board[i][j].name if self.board[i][j] is not None else '.'
                print(val, end="|")
            print(end="\n")
        print(end="\n")

    def start(self):
        print("Starting the game..")
        i = 0
        while True:
            cursor = i % len(self.players)
            player = self.players[cursor]
            print("Player turn: " + player.symbol.name)
            cell = player.play(self.board)
            symbol = player.symbol
            row = cell[0]
            col = cell[1]
            self.board[row][col] = symbol
            self.printBoard()
            result = self.checkResult(symbol)
            if result is True:
                print("Player won: " + symbol.name)
                break
            if self.isDraw():
                print("Game draw")
                break
            i += 1