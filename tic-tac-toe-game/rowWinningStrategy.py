from winningStrategy import WinningStrategy

class RowWinningStrategy(WinningStrategy):
    def check(self, board, symbol):
        for row in board:
            if self.checkRow(row, symbol):
                return True
        return False

    def checkRow(self, row, symbol):
        for char in row:
            if char != symbol:
                return False
        return True
