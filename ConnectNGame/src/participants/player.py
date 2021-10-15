from ConnectNGame.src import board
import abc


class Player(abc.ABC):

    def __init__(self, name: str, symbol: str, type: str) -> None:
        self.name = name
        self.symbol = symbol
        self.type = type

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.symbol == other.symbol

    @abc.abstractmethod
    def take_turn(self, current_board: board.Board) -> int:
        # processes the player's turn
        ...

    @abc.abstractmethod
    def get_valid_turn(self, current_board: board.Board) -> int:
        # takes valid user input, outputs int where the piece will be placed in the corresponding column on the board
        ...