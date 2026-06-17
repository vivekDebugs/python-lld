from botPlayingStrategy import BotPlayerStrategy

class ObtimisedBotPlayingStrategy(BotPlayerStrategy):
    def play(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] is None:
                    return (i, j)