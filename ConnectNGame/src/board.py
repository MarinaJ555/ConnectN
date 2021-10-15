class Board(object):

    def __init__(self, num_rows: int, num_columns: int, blank_char: str, char_to_win: int) -> None:

        self.grid = []
        self.list_num_rows = []
        self.list_num_columns = []
        self.blank_char = blank_char
        self.char_to_win = char_to_win

        x = 0
        y = 0
        while x in range(0, num_rows):
            self.list_num_rows.append(x)
            x = x + 1
        while y in range(0, num_columns):
            self.list_num_columns.append(y)
            y = y + 1
        for i in self.list_num_rows:
            L = []
            for n in self.list_num_columns:
                L.append(blank_char)
            self.grid.append(L)
        return

    @property
    def num_rows(self) -> int:
        return len(self.list_num_rows)

    @property
    def num_cols(self) -> int:
        return len(self.list_num_columns)

    def __repr__(self) -> str:
        # creates string representation of the board
        board_string = " " + " " + " ".join([str(i) for i in self.list_num_columns]) + "\n"
        for index, line in enumerate(self.grid):
            board_string += " ".join(str(index)) + " "
            board_string += " ".join([str(i) for i in line]) + "\n"
        return board_string.rstrip()

    def __eq__(self, other) -> bool:
        return self.__repr__() == other.__repr__()

    @staticmethod
    def read_board_from_file(path_to_board_file: str) -> "Board":
        starting_values = []
        with open(path_to_board_file) as board_file:
            for line in board_file:
                key, value = line.split(":")
                key, value = key.strip(), value.strip()
                T = (str(key), str(value))
                starting_values.append(T)
            starting_values = sorted(starting_values) # sorts alphabetically
            rows = int(starting_values[3][1])
            cols = int(starting_values[1][1])
            blank_char = starting_values[0][1]
            win_condition = int(starting_values[2][1])
            current_board = Board(rows, cols, blank_char, win_condition)
        return current_board


    def count_non_blank_char_in_col(self, column_number: int) -> int:
        # counts the number of pieces already in a column before adding a piece to the board
        non_blank_char = 0
        for row_index, row in enumerate(self.grid):
            if row[column_number] != self.blank_char:
                non_blank_char += 1
        return non_blank_char

    def add_piece(self, symbol: str, column_number: int) -> None:
        # add a piece to the chosen column in the board
        row_to_place_piece = self.find_corresponding_row(column_number)
        if row_to_place_piece >= self.num_rows:
            raise ValueError("This column is full")
        self.grid[row_to_place_piece][column_number] = symbol

    def find_corresponding_row(self, column_number: int) -> int:
        # find the row in the chosen column that is empty and will be filled by the player's piece
        num_non_blank_chars = self.count_non_blank_char_in_col(column_number)
        row_index = self.num_rows - (num_non_blank_chars + 1)
        return row_index

    def board_has_space(self) -> bool:
        # check if the board is full (in order to determine a tie)
        for row in self.grid:
            for char in row:
                if char == self.blank_char:
                    return True
        else:
            return False

    def column_has_space(self, chosen_column: int) -> bool:
        for row in self.grid:
            cur_char = row[chosen_column]
            if cur_char == self.blank_char:
                return True
        else:
            return False

    def remove_piece(self, symbol: str, column_number: int):
        row_to_remove_piece = self.find_corresponding_row(column_number) + 1
        self.grid[row_to_remove_piece][column_number] = self.blank_char