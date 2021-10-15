from typing import List
from ConnectNGame.src.participants import player
from ConnectNGame.src import board
from ConnectNGame.src.participants.AIs import random_AI
from ConnectNGame.src.participants import humanplayer
from ConnectNGame.src.participants.AIs import simple_AI
import sys


class Game(object):
    player_count = 1

    def __init__(self, game_board: board.Board):
        self.current_board = game_board
        self.player_1 = None
        self.player_2 = None
        self.players = []

    def setup_game(self):
        self.player_1 = self.get_player_1()
        self.player_2 = self.get_player_2(self.player_1)
        self.players.append(self.player_1)
        self.players.append(self.player_2)

    def get_player_type(self) -> str:
        player_name_types = 'Human or Random or Simple'
        while True:
            str_to_print = 'Choose the type for Player ' + str(Game.player_count) + "\n" + \
                           "Enter Human or Random or Simple: "
            player_type = input(str_to_print)
            player_type = player_type.lower().strip()
            if player_type == 'h' or player_type == 'human' or player_type == 'hu' or \
                    player_type == 'hum' or player_type == 'huma':
                Game.player_count += 1
                return "human"
            if player_type == 'r' or player_type == 'random' or player_type == 'ra' \
                    or player_type == 'ran' or player_type == 'rand' or player_type == 'rando':
                Game.player_count += 1
                return "random"
            if player_type == 's' or player_type == 'simple' or player_type == 'si' \
                    or player_type == 'sim' or player_type == 'simp' or player_type == 'simpl':
                Game.player_count += 1
                return "simple"
            else:
                print(player_type, 'is not one of', player_name_types + '.', 'Please try again.')
                continue

    def get_player_1(self) -> 'player.Player':
        path_to_board_file = str(sys.argv[1])  # get the board file
        current_board = board.Board.read_board_from_file(path_to_board_file)  # create the board
        player_type = self.get_player_type()
        if player_type == 'human':
            return humanplayer.HumanPlayer.create_first_human_from_input(current_board.blank_char, Game.player_count)
        elif player_type == 'random':
            return random_AI.RandomAI.create_randomAI_from_input()
        else:
            player_number = 1
            return simple_AI.SimpleAI.create_simple_AI_from_input(player_number)

    def get_player_2(self, player_1: 'player.Player') -> 'player.Player':
        path_to_board_file = str(sys.argv[1])  # get the board file
        current_board = board.Board.read_board_from_file(path_to_board_file)  # create the board
        player_type = self.get_player_type()
        if player_type == 'human':
            if player_1.type == 'human': # to make sure that two human players aren't assigned the same name/piece
                human_player_2 = humanplayer.HumanPlayer.create_second_human_from_input(current_board.blank_char, player_1)
                return human_player_2
            else:
                human_player = humanplayer.HumanPlayer.create_first_human_from_input(current_board.blank_char, Game.player_count)
                return human_player # if the first player was not human, this is the first human player
        elif player_type == 'random':
            while True:
                random_AI = random_AI.RandomAI.create_randomAI_from_input()
                if random_AI.symbol == player_1.symbol or random_AI.symbol == self.current_board.blank_char:
                    continue
                else:
                    return random_AI
        else:
            while True:
                simple = simple_AI.SimpleAI.create_simple_AI_from_input(2)
                if simple.symbol == player_1.symbol or simple.symbol == self.current_board.blank_char:
                    continue
                else:
                    return simple

    def play(self) -> bool:
        done = False
        print(board.Board.__repr__(self.current_board))
        while not done:
            for index, player in enumerate(self.players):
                if player.type == 'human':
                    humanplayer.HumanPlayer.take_turn(humanplayer.HumanPlayer(player.name, player.symbol,
                                        str(player.type)), self.current_board)
                elif player.type == 'random':
                    random_AI.RandomAI.take_turn(random_AI.RandomAI(player.name, player.symbol, str(player.type)), self.current_board)
                else:
                    opponent_symbol = self.get_opponent_symbol(player)
                    simple_AI.SimpleAI.take_simpleAI_turn(simple_AI.SimpleAI(player.name, player.symbol, str(player.type)), self.current_board, opponent_symbol)
                print(board.Board.__repr__(self.current_board))
                check_win = self.wins_game(self.current_board, player.symbol)
                check_tie = self.tied_game()
                if check_win is True:
                    print(player.name, "won the game!")
                    done = True
                    break
                elif check_tie is True:
                    print("Tie Game.")
                    done = True
                    break
                else:
                    continue
        return done

    def get_opponent_symbol(self, player):
        if player == self.player_1:
            opponent_symbol = self.player_2.symbol
        else:
            opponent_symbol = self.player_1.symbol
        return opponent_symbol


    @staticmethod
    def wins_game(current_board: board.Board, symbol: str) -> bool:
        for i in range(current_board.num_rows):
            for j in range(current_board.num_cols):
                current_pos = current_board.grid[i][j]
                if current_pos == symbol:
                    n_char_on_right = Game.check_right(current_board, symbol, i, j)
                    n_char_below = Game.check_below(current_board, symbol, i, j)
                    n_char_right_diag = Game.check_right_diagonal(current_board, symbol, i, j)
                    n_char_left_diag = Game.check_left_diagonal(current_board, symbol, i, j)
                    if n_char_on_right or n_char_below or n_char_right_diag or n_char_left_diag:
                        return True
        return False

    @staticmethod
    def check_right(current_board: board.Board, symbol: str, i: int, j: int) -> bool:
        char_count = 1
        while i < current_board.num_rows and j + 1 < current_board.num_cols:
            if current_board.grid[i][j + 1] == symbol:
                char_count = char_count + 1
                j = j + 1
            else:
                break
        if char_count >= current_board.char_to_win:
            return True
        else:
            return False

    @staticmethod
    def check_below(current_board: board.Board, symbol: str, i: int, j: int) -> bool:
        char_count = 1
        while i + 1 < current_board.num_rows and j < current_board.num_cols:
            if current_board.grid[i + 1][j] == symbol:
                char_count = char_count + 1
                i = i + 1
            else:
                break
        if char_count >= current_board.char_to_win:
            return True
        else:
            return False


    @staticmethod
    def check_right_diagonal(current_board: board.Board, symbol: str, i: int, j: int) -> bool:
        char_count = 1
        while i + 1 < current_board.num_rows and j + 1 < current_board.num_cols:
            if current_board.grid[i + 1][j + 1] == symbol:
                char_count = char_count + 1
                i = i + 1
                j = j + 1
            else:
                break
        if char_count >= current_board.char_to_win:
            return True
        else:
            return False

    @staticmethod
    def check_left_diagonal(current_board: board.Board, symbol: str, i: int, j: int) -> bool:
        char_count = 1
        while i + 1 < current_board.num_rows and j - 1 < current_board.num_cols:
            if j - 1 >= 0:
                if current_board.grid[i + 1][j - 1] == symbol:
                    char_count = char_count + 1
                    i = i + 1
                    j = j - 1
                else:
                    break
            else:
                break
        return char_count >= current_board.char_to_win

    def tied_game(self) -> bool:
        # when board is full, there is a tie and the game ends
        if self.current_board.board_has_space() is True:
            return False
        else:
            return True