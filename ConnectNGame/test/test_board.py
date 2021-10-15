import unittest
from unittest.mock import patch
from ConnectNGame.src.board import Board

class TestBoard(unittest.TestCase):

    def test_init(self):
        with self.subTest("Testing first board"):
            new_board = Board(3, 2, '$', 2)
            self.assertListEqual(new_board.list_num_rows, [0, 1, 2])
            self.assertListEqual(new_board.list_num_columns, [0, 1])
            self.assertListEqual(new_board.grid, [['$', '$'], ['$', '$'], ['$', '$']])

        with self.subTest("Testing second board"):
            new_board = Board(0, 2, '#', 2)
            self.assertEqual(new_board.list_num_rows, [])
            self.assertEqual(new_board.list_num_columns, [0, 1])

        with self.subTest("Testing third board"):
            new_board = Board(6, 0, ')', 4)
            self.assertEqual(new_board.list_num_rows, [0, 1, 2, 3, 4, 5])
            self.assertEqual(new_board.list_num_columns, [])

    def test_read_board_from_file(self):
        with self.subTest("Testing 3X3X3.txt"):
            board = Board.read_board_from_file('../../config_files/3X3X3.txt')
            self.assertEqual(board, Board(3, 3, '&', 3))

        with self.subTest("Testing connect4.txt"):
            board = Board.read_board_from_file('../../config_files/connect4.txt')
            self.assertEqual(board, Board(6, 7, '*', 4))

    def test_count_non_blank_char_in_col(self):
        test_board = Board(3, 3, '^', 3)
        user_input = 2
        with patch('ConnectNGame.src.board.input', side_effect=user_input):
            count = Board.count_non_blank_char_in_col(test_board, user_input)
            self.assertEqual(count, 0)

            test_board.grid[2][2] = "$" # add non-blank character to the column
            symb_count = Board.count_non_blank_char_in_col(test_board, user_input)
            self.assertEqual(symb_count, 1)

            test_board.grid[2][1] = "#" # add non-blank character to a different column, should not change count
            new_symb_count = Board.count_non_blank_char_in_col(test_board, user_input)
            self.assertEqual(new_symb_count, 1)

    def test_add_piece(self):
        new_board = Board(5, 6, '&', 4)
        user_input = 5
        user_input2 = 5
        with patch('ConnectNGame.src.board.input', side_effect=user_input):
            with self.subTest("Testing add_piece 1"):
                new_board.add_piece('%', 5)
                self.assertEqual(new_board.grid[4][5], '%')
            with self.subTest("Testing add_piece 2"):
                new_board.grid[4][5] = '#'
                new_board.add_piece('$', 5)
                self.assertEqual(new_board.grid[3][5], '$')
            with self.subTest("Testing add_piece 3"):
                new_board.grid[4][0] = '%'
                new_board.add_piece('$', 0)
                self.assertEqual(new_board.grid[3][0], '$')

    def test_row_to_place_piece(self):
        new_board = Board(8, 9, '#', 5)
        user_input = 7
        with patch('ConnectNGame.src.board.input', side_effect=user_input):
            with self.subTest("Testing empty board"):
                row_index = new_board.row_to_place_piece(user_input)
                self.assertEqual(row_index, 7)

            with self.subTest("Testing non-empty board"):
                new_board.grid[7][7] = '%'
                new_row_index = new_board.row_to_place_piece(user_input)
                self.assertEqual(new_row_index, 6)

    def test_board_has_space(self):
        new_board = Board(2, 2, '-', 3)
        new_board.grid[1][0] = '%'
        new_board.grid[0][0] = '$'
        new_board.grid[1][1] = '%'
        has_space = new_board.board_has_space()
        self.assertTrue(has_space)

        new_board.grid[0][1] = '$'
        has_space_now = new_board.board_has_space()
        self.assertFalse(has_space_now)


    def test_column_has_space(self):
        new_board = Board(2, 2, '*', 3)
        new_board.grid[1][0] = '$'
        col_has_space = new_board.column_has_space(0)
        self.assertTrue(col_has_space)

        new_board.grid[0][0] = '#'
        col_has_space_now = new_board.column_has_space(0)
        self.assertFalse(col_has_space_now)




if __name__ == '__main__':
    unittest.main()
