import random
from ConnectNGame.src.participants import player
from ConnectNGame.src import board
from ConnectNGame.src import game
from typing import Union


class SimpleAI(player.Player):
    number_created = 0

    def __init__(self, name: str, symbol: str, type: str):
        super().__init__(name, symbol, type)

    @staticmethod
    def create_simple_AI_from_input(player_number) -> 'SimpleAI':
        name = SimpleAI.generate_simple_AI_name(player_number)
        piece = SimpleAI.generate_simple_AI_piece()
        type = 'simple'
        return SimpleAI(name, piece, type)

    @staticmethod
    def generate_simple_AI_name(player_number) -> str:
        SimpleAI.number_created += 1
        return 'SimpleAi ' + str(player_number)

    @staticmethod
    def generate_simple_AI_piece():
        VISIBLE_CHARACTERS = [chr(i) for i in range(ord('!'), ord('~') + 1)]
        char = random.choice(VISIBLE_CHARACTERS)
        return char

    def take_turn(self, current_board: board.Board) -> int:
        pass

    def take_simpleAI_turn(self, current_board: board.Board, opponent_symbol: str):
        col_choice = SimpleAI.find_win_opportunity(current_board, self.symbol)
        block_choice = SimpleAI.find_win_opportunity(current_board, opponent_symbol)
        if col_choice is not None: # if there is a way to win
            col_to_place = col_choice
        elif block_choice is not None: # if there is a way to block a win
            col_to_place = block_choice
        else:
            while True:
                col_to_place = random.choice(range(current_board.num_cols)) # if there is no way to win or block
                num_non_blanks = board.Board.count_non_blank_char_in_col(current_board, col_to_place)
                if num_non_blanks == current_board.num_rows:
                    continue
                else:
                    break
        board.Board.add_piece(current_board, self.symbol, col_to_place)

    def get_valid_turn(self, current_board: board.Board) -> int:
        pass

    @staticmethod
    def find_win_opportunity(current_board: board.Board, symbol: str) -> Union[int, None]:
        # add a piece to each column in the board, check to see if there is a win
        # remove the piece if there is not a win
        # if there is a win, return that col and take the turn in that col
        for column in range(current_board.num_cols):
            board.Board.add_piece(current_board, symbol, column)
            win_opportunity = game.Game.wins_game(current_board, symbol)
            board.Board.remove_piece(current_board, symbol, column)
            if win_opportunity is True:
                return column
        else:
            return None