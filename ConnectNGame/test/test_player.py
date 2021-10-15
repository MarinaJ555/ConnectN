import unittest
from unittest.mock import patch
from ConnectNGame.src.participants.player import Player
from ConnectNGame.src.board import Board

class TestPlayer(unittest.TestCase):

    def test_valid_player_name(self):
        user_name1 = 'Ben'
        user_name2 = "Chris Kyle"
        user_name3 = " "
        with self.subTest("Testing first name"):
            self.assertTrue(Player.valid_player_name(user_name1))

        with self.subTest("Testing second name"):
            self.assertTrue(Player.valid_player_name(user_name2))

        with self.subTest("Testing third name"):
            self.assertFalse(Player.valid_player_name(user_name3))

    def test_valid_player_piece(self):
        blank_char = '*'
        player_piece = '&'
        player_piece2 = 'piece'
        player_piece3 = ' '
        with self.subTest("Testing first piece"):
            self.assertEqual(Player.valid_player_piece(player_piece, blank_char), '&')

        with self.subTest("Testing second piece"):
            self.assertEqual(Player.valid_player_piece(player_piece2, blank_char), 'invalid')

        with self.subTest("Testing third piece"):
            player = Player.valid_player_piece(player_piece3, blank_char)
            self.assertRaises(TypeError, player)

    def test_get_player_1_name(self):
        name = 'Billybob'
        with patch('ConnectNGame.src.player.input', side_effect=[name]):
            with self.subTest("Testing first P1 name"):
                player_name = Player.get_player_1_name()
                self.assertEqual(player_name, name)

    def test_get_player_1_piece(self):
        piece = 'X'
        piece2 = '100'
        with patch('ConnectNGame.src.player.input', side_effect=piece):
            with self.subTest('Testing first P1 piece'):
                player_1_piece = Player.get_player_1_piece('*')
                self.assertEqual(player_1_piece, 'X')

        with patch('ConnectNGame.src.player.input', side_effect=[piece2]):
            with self.subTest('Testing second P1 piece'):
                player_1_piece = Player.get_player_1_piece('*')
                self.assertRaises(TypeError, player_1_piece)

    def test_get_player_2_name(self):
        name = 'Sharkeisha'
        with patch('ConnectNGame.src.player.input', side_effect=[name]):
            with self.subTest('Testing first P2 name'):
                player_2_name = Player.get_player_2_name('Bobert')
                self.assertEqual(player_2_name, 'Sharkeisha')

    def test_get_player_2_piece(self):
        piece = '&'
        piece2 = 'invalid'
        with patch('ConnectNGame.src.player.input', side_effect=piece):
            with self.subTest('Testing first P2 piece'):
                player_2_piece = Player.get_player_2_piece('$', '*', 'Bobert')
                self.assertEqual(player_2_piece, piece)

        with patch('ConnectNGame.src.player.input', side_effect=[piece2]):
            with self.subTest('Testing second P2 piece'):
                self.assertRaises(TypeError, player_2_piece)

    def test_get_diff_input(self):
        with self.subTest('Testing first inputs'):
            first_inputs = Player.check_diff_input('Bob', 'John')
            self.assertTrue(first_inputs)

        with self.subTest('Testing second inputs'):
            second_inputs = Player.check_diff_input('X AE A-12', 'X AE A-12')
            self.assertFalse(second_inputs)

    def test_get_valid_turn(self):
        user_input = 5
        with patch('ConnectNGame.src.player.input', side_effect=[user_input]):
            with self.subTest('Testing first input'):
                board = Board(7, 8, '^', 4)
                first_input = Player.get_valid_turn(Player('John', '&'), board)
                self.assertEqual(first_input, user_input)

    def test_create_player_1_from_input(self):
        name = 'Johnny'
        symbol = '@'

        with self.subTest('Testing first P1'):
            with patch('ConnectNGame.src.player.input', side_effect=[name, symbol]):
                player_1 = Player.create_player_1_from_input('*')
                self.assertEqual(player_1, Player(name, symbol))

    def test_create_player_2_from_input(self):
        name = 'Laronda'
        symbol = '&'
        with self.subTest('Testing first P2'):
            with patch('ConnectNGame.src.player.input', side_effect=[name, symbol]):
                player_2 = Player.create_player_2_from_input('*', Player('LilJon', '#'))
                self.assertEqual(player_2, Player(name, symbol))


if __name__ == '__main__':
    unittest.main()
