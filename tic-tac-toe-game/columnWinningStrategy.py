from winningStrategy import WinningStrategy

class ColumnWinningStrategy(WinningStrategy):
    def check(self, board, symbol):
        for j in range(len(board[0])):
            if self.checkCol(j, board, symbol):
                return True
        return False

    def checkCol(self, col, board, symbol):
        for i in range(len(board)):
            if board[i][col] != symbol:
                return False
        return True