from ConnectNGame.src import board
from ConnectNGame.src.participants import player


class HumanPlayer(player.Player):

    def __init__(self, name: str, symbol: str, type: str):
        super().__init__(name, symbol, type)

    def take_turn(self, current_board: board.Board) -> int:
        column_choice = self.get_valid_turn(current_board)
        try:
            current_board.add_piece(self.symbol, column_choice)
        except ValueError:
            print(str(player) + "," + "column needs to be an integer.", column_choice, "is not an integer.")
        return column_choice

    def get_valid_turn(self, current_board: board.Board) -> int:
        while True:
            turn = input(str(self.name).strip() + ', ' +
                         "please enter the column you want to play in: ")
            try:
                turn = int(turn)  # type: ignore
                if int(turn) >= 0 and int(turn) < int(current_board.num_cols):
                    if board.Board.column_has_space(current_board, turn) is True:
                        return int(turn)
                    else:
                        print("You cannot play in", turn, "because it is full.")
                        continue
                else:
                    print("Your column needs to be between 0 and", current_board.num_cols - 1, "but is actually",
                          str(turn) + ".")
                    continue
            except:
                print(str(self.name) + ',', 'column needs to be an integer. ' +
                      str(turn) + ' is not an integer.')
                continue

    @staticmethod
    def create_first_human_from_input(blank_char: str, player_count: int) -> "HumanPlayer":
        type = 'human'
        while True:
            name = HumanPlayer.get_first_human_name(player_count)
            if name == "invalid":
                continue
            symbol = HumanPlayer.get_first_human_piece(blank_char, player_count)
            if symbol == "invalid":
                continue
            else:
                return HumanPlayer(name, symbol, type)

    @staticmethod
    def create_second_human_from_input(blank_char: str, player_1: "player.Player") -> "HumanPlayer":
        type = 'human'
        while True:
            name = HumanPlayer.get_second_human_name(player_1.name)
            if name == "invalid":
                continue
            symbol = HumanPlayer.get_second_human_piece(player_1.symbol, blank_char, player_1.name)
            if symbol == "invalid":
                continue
            else:
                return HumanPlayer(name, symbol, type)

    @staticmethod
    def valid_human_name(human_name: str) -> bool:
        # checks that name is not whitespace or empty string
        if human_name.strip() != "" and human_name is not None and human_name != "None":
            return True
        else:
            print("Your name cannot be the empty string or whitespace.")
            return False

    @staticmethod
    def valid_player_piece(player_piece: str, blank_char: str) -> str:
        # the piece cannot be None, whitespace, must be one char, and not the board's blank char
        not_empty = False
        not_whitespace = False
        one_character = False
        not_blank_char = False

        if player_piece.strip() != "" and player_piece is not None:
            not_empty = True
            not_whitespace = True
        else:
            print('Your piece cannot be the empty string or whitespace.')

        if len(player_piece) == 1:
            one_character = True
        elif len(player_piece) == 0:
            one_character = False
        else:
            print(player_piece, 'is not a single character. Your piece can only be a single character.')

        if player_piece != blank_char:
            not_blank_char = True
        else:
            print('Your piece cannot be the same as the blank character.')

        if not_empty and not_whitespace and one_character and not_blank_char == True:
            return player_piece
        else:
            return "invalid"

    @staticmethod
    def get_first_human_name(player_count) -> str:  # user enters their name and their name is checked
        str_to_print = "HumanPlayer " + str(player_count - 1) + " enter your name: "
        human_1_name = input(str_to_print).strip()
        if HumanPlayer.valid_human_name(human_1_name) is True:
            return human_1_name
        else:
            return "invalid"

    @staticmethod
    def get_first_human_piece(blank_char: str, player_count) -> str:  # user chooses their piece and the piece is checked
        str_to_print = "HumanPlayer " + str(player_count - 1) + " enter your piece: "
        human_1_piece = input(str_to_print).strip()
        human_1_piece = HumanPlayer.valid_player_piece(human_1_piece, blank_char)
        return human_1_piece

    @staticmethod
    def get_second_human_name(player_1_name: str) -> str:
        human_2_name = input("HumanPlayer 2 enter your name: ").strip()
        if HumanPlayer.valid_human_name(human_2_name) is True:
            if not HumanPlayer.check_diff_input(player_1_name,
                                                human_2_name):  # checks that both players don't have the same name
                print("You cannot use", human_2_name, "for your name as someone else is already using it.")
                return "invalid"
            else:
                return human_2_name
        else:
            return "invalid"

    @staticmethod
    def get_second_human_piece(human_1_piece: str, blank_char: str, human_1_name: str) -> str:
        human_2_piece = input("HumanPlayer 2 enter your piece: ").strip()
        human_2_piece = HumanPlayer.valid_player_piece(human_2_piece, blank_char)
        if human_2_piece == "invalid":  # prompt user again if piece does not meet criteria
            return "invalid"
        if not HumanPlayer.check_diff_input(human_1_piece, human_2_piece):
            print("You cannot use", human_2_piece, "for your piece as", human_1_name, "is already using it.")
            return "invalid"
        else:
            return human_2_piece

    @staticmethod
    def check_diff_input(human_1_input: str, human_2_input: str) -> bool:
        # checks that player 1 and 2 do not have the same name or piece
        if human_1_input.lower() != human_2_input.lower():
            return True
        else:
            return False