import unittest
from ConnectNGame.src.game import Game
from ConnectNGame.src.board import Board
from ConnectNGame.src.participants.player import Player
from ConnectNGame.src.participants.AIs.random_AI import RandomAI
from ConnectNGame.src.participants.humanplayer import HumanPlayer
from ConnectNGame.src.participants.AIs.simple_AI import SimpleAI


class TestGame(unittest.TestCase):

    def setUp(self) -> None:
        self.current_board = Board.read_board_from_file('../../config_files/Connect4.txt')
        self.current_game = Game(self.current_board)
        self.player_1 = HumanPlayer('Anthony', '%', 'human')
        self.player_2 = RandomAI('RandomAi 2', 'T', 'random')
        self.player_3 = SimpleAI('SimpleAi 2', 'G', 'simple')

    def test__init__(self):
        with self.subTest("Testing list of players"):
            list1 = []
            list1.append(Player('Bob', '%', 'human'))
            list1.append(Player('SimpleAi 2', '$', 'simple'))
            self.assertEqual(self.current_game.players, list1)

        with self.subTest("Testing second list of players"):
            list2 = []
            list2.append(Player('Billyjoe', '@', 'human'))
            list2.append(Player('RandomAi 2', '#', 'random'))
            self.assertEqual(self.current_game.players, list2)

    def test_wins_game(self):
        with self.subTest("Testing first win"):
            board = Board.read_board_from_file('../../config_files/3X3X3.txt')
            board.grid[0][0] = '@'
            board.grid[1][0] = '@'
            board.grid[2][0] = '@'
            board.grid[2][2] = '$'
            board.grid[1][1] = '$'
            game = Game(board, Player('LilXan', '$'), Player('JCole', '@'))
            self.assertTrue(Game.wins_game(game, '@'))

        with self.subTest("Testing second win"):
            board2 = Board.read_board_from_file('../../config_files/connect4.txt')
            board2.grid[4][5] = '#'
            board2.grid[1][4] = '&'
            game2 = Game(board2, Player('Kendrick Lamar', '#'), Player('Mac Miller', '&'))
            self.assertFalse(Game.wins_game(game2, '#'))

    def test_check_right(self):
        with self.subTest('Testing check right'):
            board = Board.read_board_from_file('../../config_files/connect4.txt')
            game = Game.check_right(Game(board, Player('John', '%'),
                                         Player('Ricky', '$')), '%', 5, 3)
            self.assertFalse(game)

        with self.subTest('Testing second check right'):
            board2 = Board.read_board_from_file('../../config_files/3X3X3.txt')
            board2.grid[2][0] = '%'
            board2.grid[2][1] = '%'
            board2.grid[2][2] = '%'
            game2 = Game.check_right(Game(board2, Player('John', '%'),
                                          Player('Ricky', '$')), '%', 2, 0)
            self.assertTrue(game2)

    def test_check_below(self):
        with self.subTest('Test one down'):
            board = Board.read_board_from_file('../../config_files/3X3X3.txt')
            board.grid[2][0] = '%'
            board.grid[2][1] = '%'
            board.grid[2][2] = '%'
            game2 = Game.check_below(Game(board, Player('John', '%'),
                                          Player('Ricky', '$')), '%', 0, 0)
            self.assertFalse(game2)

        with self.subTest('Test two down'):
            board2 = Board.read_board_from_file('../../config_files/connect4.txt')
            board2.grid[0][1] = '$'
            board2.grid[1][1] = '$'
            board2.grid[2][1] = '$'
            board2.grid[3][1] = '$'
            game2 = Game.check_below(Game(board2, Player('John', '%'),
                                          Player('Ricky', '$')), '$', 0, 1)
            self.assertTrue(game2)

    def test_check_right_diagonal(self):
        with self.subTest('Test one down'):
            board = Board.read_board_from_file('../../config_files/3X3X3.txt')
            board.grid[0][0] = '%'
            board.grid[1][1] = '%'
            board.grid[2][2] = '%'
            game2 = Game.check_right_diagonal(Game(board, Player('John', '%'),
                                          Player('Ricky', '$')), '%', 0, 0)
            self.assertTrue(game2)

        with self.subTest('Test two down'):
            board2 = Board.read_board_from_file('../../config_files/connect4.txt')
            board2.grid[0][1] = '$'
            board2.grid[1][1] = '$'
            board2.grid[2][1] = '$'
            board2.grid[3][1] = '$'
            game2 = Game.check_right_diagonal(Game(board2, Player('John', '%'),
                                          Player('Ricky', '$')), '$', 0, 1)
            self.assertFalse(game2)


    def test_check_left_diagonal(self):
        with self.subTest('Test one down'):
            board = Board.read_board_from_file('../../config_files/3X3X3.txt')
            board.grid[0][2] = '%'
            board.grid[1][1] = '%'
            board.grid[2][0] = '%'
            game2 = Game.check_left_diagonal(Game(board, Player('John', '%'),
                                          Player('Ricky', '$')), '%', 0, 2)
            self.assertTrue(game2)

        with self.subTest('Test two down'):
            board2 = Board.read_board_from_file('../../config_files/connect4.txt')
            board2.grid[0][1] = '$'
            board2.grid[1][1] = '$'
            board2.grid[2][1] = '$'
            board2.grid[3][1] = '$'
            game2 = Game.check_left_diagonal(Game(board2, Player('John', '%'),
                                          Player('Ricky', '$')), '$', 0, 1)
            self.assertFalse(game2)

    def test_check_tied_game(self):
        with self.subTest('Test one down'):
            board = Board.read_board_from_file('../../config_files/3X3X3.txt')
            board.grid[0][0] = '%'
            board.grid[0][1] = '$'
            board.grid[0][2] = '%'
            board.grid[1][0] = '$'
            board.grid[1][1] = '%'
            board.grid[1][2] = '$'
            board.grid[2][0] = '%'
            board.grid[2][1] = '$'
            board.grid[2][2] = '%'
            game = Game.tied_game(Game(board, Player('John', '%'), Player('Ricky', '$')))
            self.assertTrue(game)

        with self.subTest('Test two down'):
            board2 = Board.read_board_from_file('../../config_files/connect4.txt')
            board2.grid[0][1] = '$'
            board2.grid[1][1] = '$'
            board2.grid[2][1] = '$'
            board2.grid[3][1] = '$'
            game2 = Game.tied_game(Game(board2, Player('Mr.Potatohead', '%'),
                                        Player('Mrs.Potatohead', '*')))
            self.assertFalse(game2)


if __name__ == '__main__':
    unittest.main()
