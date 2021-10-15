import unittest
from unittest.mock import patch
from ConnectNGame.src.participants import humanplayer
from ConnectNGame.src import board
from ConnectNGame.src.participants.AIs import simple_AI


class TestHumanPlayer(unittest.TestCase):

    def setUp(self):
        self.current_board = board.Board.read_board_from_file('../../config_files/Connect4.txt')
        self.current_board_2 = board.Board.read_board_from_file('../../config_files/3X3X3.txt')
        self.human_player_1 = humanplayer.HumanPlayer('Bobert', '$', 'human')
        self.human_player_2 = humanplayer.HumanPlayer('John Cena', 'G', 'human')
        self.simple_AI_1 = simple_AI.SimpleAI('SimpleAi 1', 'r', 'simple')

    def test_get_valid_turn(self):
        user_input = 4
        with patch('ConnectNGame.src.participants.humanplayer.input', side_effect = [user_input]):
            with self.subTest('Testing first input...'):
                first_input = humanplayer.HumanPlayer.get_valid_turn(self.human_player_1, self.current_board)
                self.assertEqual(first_input, user_input)

    def test_create_first_human_from_input(self):
        blank_char = self.current_board.blank_char
        name = self.human_player_1.name
        symbol = self.human_player_1.symbol
        type = str(self.human_player_1.type)
        with patch('ConnectNGame.src.participants.humanplayer.input', side_effect=[name, symbol, type]):
            with self.subTest('Testing first human player...'):
                player_1 = humanplayer.HumanPlayer.create_first_human_from_input(blank_char, 1)
                self.assertEqual(player_1, humanplayer.HumanPlayer(name, symbol, type))

    def test_create_second_human_from_input(self):
        blank_char = self.current_board_2.blank_char
        name = self.human_player_2.name
        symbol = self.human_player_2.symbol
        type = str(self.human_player_2.type)
        with patch('ConnectNGame.src.participants.humanplayer.input', side_effect=[name, symbol, type]):
            with self.subTest('Testing second human player...'):
                player_2 = humanplayer.HumanPlayer.create_second_human_from_input(blank_char, self.simple_AI_1)
                self.assertEqual(player_2, humanplayer.HumanPlayer(name, symbol, type))

    def test_valid_human_name(self):
        human_name = 'Rigoberto'
        human_name_2 = ' '
        with self.subTest('Testing first human name...'):
            self.assertTrue(humanplayer.HumanPlayer.valid_human_name(human_name))
        with self.subTest('Testing second human name...'):
            self.assertFalse(humanplayer.HumanPlayer.valid_human_name(human_name_2))

    def test_valid_player_piece(self):
        player_piece = self.human_player_1.symbol
        player_piece_2 = 'piece'
        player_piece_3 = ' '
        player_piece_4 = self.current_board.blank_char
        blank_char = self.current_board.blank_char
        with self.subTest('Testing first piece...'):
            self.assertEqual(humanplayer.HumanPlayer.valid_player_piece(player_piece, blank_char), player_piece)
        with self.subTest('Testing second piece...'):
            self.assertEqual(humanplayer.HumanPlayer.valid_player_piece(player_piece_2, blank_char), 'invalid')
        with self.subTest('Testing third piece...'):
            self.assertEqual(humanplayer.HumanPlayer.valid_player_piece(player_piece_3, blank_char), 'invalid')
        with self.subTest('Testing fourth piece...'):
            self.assertEqual(humanplayer.HumanPlayer.valid_player_piece(player_piece_4, blank_char), 'invalid')

    def test_get_first_human_name(self):
        user_input = 'Donny'
        user_input_2 = ' '
        with patch('ConnectNGame.src.participants.humanplayer.input', side_effect=[user_input]):
            with self.subTest('Testing first human1 name...'):
                self.assertEqual(humanplayer.HumanPlayer.get_first_human_name(1), user_input)
        with patch('ConnectNGame.src.participants.humanplayer.input', side_effect=[user_input_2]):
            with self.subTest('Testing second human1 name...'):
                self.assertEqual(humanplayer.HumanPlayer.get_first_human_name(1), 'invalid')

    def test_get_first_human_piece(self):
        human_1_name = self.human_player_1.name
        human_1_piece_1 = 'O'
        human_1_piece_2 = ' '
        with patch('ConnectNGame.src.participants.humanplayer.input', side_effect=[human_1_piece_1]):
            with self.subTest('Testing first human piece...'):
                self.assertEqual(humanplayer.HumanPlayer.get_first_human_piece(human_1_name, 1), human_1_piece_1)
        with patch('ConnectNGame.src.participants.humanplayer.input', side_effect=[human_1_piece_2]):
            with self.subTest('Testing second human piece...'):
                self.assertEqual(humanplayer.HumanPlayer.get_first_human_piece(human_1_name, 1), 'invalid')

    def test_get_second_human_name(self):
        user_input = 'Kimmy'
        user_input_2 = ' '
        human_1_name = self.human_player_2.name
        with patch('ConnectNGame.src.participants.humanplayer.input', side_effect=[user_input]):
            with self.subTest('Testing first human2 name...'):
                self.assertEqual(humanplayer.HumanPlayer.get_second_human_name(human_1_name), user_input)
        with patch('ConnectNGame.src.participants.humanplayer.input', side_effect=[user_input_2]):
            with self.subTest('Testing second human2 name...'):
                self.assertEqual(humanplayer.HumanPlayer.get_second_human_name(human_1_name), 'invalid')

    def test_get_second_human_piece(self):
        human_1_piece = '%'
        blank_char = self.current_board.blank_char
        human_1_name = self.human_player_1.name
        user_input = '#'
        user_input_2 = '%'
        user_input_3 = '*'
        with patch('ConnectNGame.src.participants.humanplayer.input', side_effect=[user_input]):
            with self.subTest('Testing first human2 piece...'):
                self.assertEqual(humanplayer.HumanPlayer.get_second_human_piece
                                 (human_1_piece, blank_char, human_1_name), user_input)
        with patch('ConnectNGame.src.participants.humanplayer.input', side_effect=[user_input_2]):
            with self.subTest('Testing first human2 piece...'):
                self.assertEqual(humanplayer.HumanPlayer.get_second_human_piece
                                 (human_1_piece, blank_char, human_1_name), 'invalid')
        with patch('ConnectNGame.src.participants.humanplayer.input', side_effect=[user_input_3]):
            with self.subTest('Testing first human2 piece...'):
                self.assertEqual(humanplayer.HumanPlayer.get_second_human_piece
                                 (human_1_piece, blank_char, human_1_name), 'invalid')

    def test_check_diff_input(self):
        human_1_name = self.human_player_1.name
        human_1_name_2 = 'Bob'
        human_1_piece = self.human_player_1.symbol
        human_2_name = self.human_player_2.name
        human_2_name_2 = 'BOB'
        human_2_piece = self.human_player_2.symbol
        with self.subTest('Testing first inputs...'):
            self.assertTrue(humanplayer.HumanPlayer.check_diff_input(human_1_name, human_2_name))
        with self.subTest('Testing second inputs...'):
            self.assertFalse(humanplayer.HumanPlayer.check_diff_input(human_1_name_2, human_2_name_2))
        with self.subTest('Testing third inputs...'):
            self.assertTrue(humanplayer.HumanPlayer.check_diff_input(human_1_piece, human_2_piece))