# Design Tic Tac Toe

## Requirements
- Board can be of any NxN size.
- There can be two players.
- Each player will be allotted a symbol.
- The symbol can be one of O and X.
- The players can be either humans or bots.
- Each human player will have a name, email and profile image.
- Each bot player will have a difficulty level.
- Any random player can start the game.
- Then the players will take turns alternatively.
- The player with any consecutive N symbols in a row, column or diagonal wins.
- If the board is full and no player has won, the game is a draw.

## Design
### Entities
- Game
- Board
- Cell
- Player
    - Human
    - Bot
- Symbol

**Symbol(Enum)**
- X
- O

**PlayerType(Enum)**
- HUMAN
- BOT

**Player**
- playerType: PlayerType
- play(): Tuple[Int, Int]
- symbol: Symbol

**HumanPlayer(Player)**
- name: String
- email: String
- profileImage: String

**BotDifficulty(Enum)**
- EASY
- MEDIUM
- HARD

**BotPlayingStrategy**
- play(): Tuple[Int, Int]

**RandomBotPlayingStrategy(BotPlayingStrategy)**

**MinMaxBotPlayingStrategy(BotPlayingStrategy)**

**ObtimisedBotPlayingStrategy(BotPlayingStrategy)**

**BotPlayer(Player)**
- difficulty: BotDifficulty
- playingStrategy: BotPlayingStrategy

**WinningStrategy**
- check(): Boolean

**RowWinningStrategy(WinningStrategy)**

**ColumnWinningStrategy(WinningStrategy)**

**DiagonalWinningStrategy(WinningStrategy)**

**Game**
- players: List[Player]
- board: List[List[Symbol]]
- winningStrategies: List[WinningStrategy]
- addPlayer(): None
- addWinningStrategy: None
- createBoard(): None
- checkResult(): Boolean
- isGameOver(): Boolean
- start(): None