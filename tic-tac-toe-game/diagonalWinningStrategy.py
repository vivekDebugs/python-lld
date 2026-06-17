from winningStrategy import WinningStrategy

class DiagonalWinningStrategy(WinningStrategy):
    def check(self, board, symbol):
        if self.checkLeftDiagonal(board, symbol):
            return True
        if self.checkRightDiagonal(board, symbol):
            return True
        return False

    def checkLeftDiagonal(self, board, symbol):
        i = 0
        for i in range(len(board)):
            if board[i][i] != symbol:
                return False
        return True

    def checkRightDiagonal(self, board, symbol):
        i = 0
        j = len(board[i]) - 1
        while i < len(board) and j >= 0:
            char = board[i][j]
            if char != symbol:
                return False
            i += 1
            j -= 1
        return True