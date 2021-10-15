import random
from ConnectNGame.src.participants import player
from ConnectNGame.src import board


class RandomAI(player.Player):
    number_created = 0

    def __init__(self, name: str, symbol: str, type: str):
        super().__init__(name, symbol, type)

    @staticmethod
    def create_randomAI_from_input() -> 'RandomAI':
        name = RandomAI.generate_random_AI_name()
        piece = RandomAI.generate_random_AI_piece()
        type = 'random'
        return RandomAI(name, piece, type)

    @staticmethod
    def generate_random_AI_name() -> str:
        RandomAI.number_created += 1
        return 'RandomAi ' + str(RandomAI.number_created)

    @staticmethod
    def generate_random_AI_piece():
        VISIBLE_CHARACTERS = [chr(i) for i in range(ord('!'), ord('~') + 1)]
        AI_piece = random.choice(VISIBLE_CHARACTERS)
        return AI_piece

    def take_turn(self, current_board: board.Board) -> None:
        while True:
            col_choice = random.choice(range(current_board.num_cols))
            num_non_blanks = board.Board.count_non_blank_char_in_col(current_board, col_choice)
            if num_non_blanks == current_board.num_rows:
                continue
            else:
                board.Board.add_piece(current_board, self.symbol, col_choice)
                break

    def get_valid_turn(self, current_board: board.Board) -> int:
        pass