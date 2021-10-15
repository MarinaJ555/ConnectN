import unittest
import random
from ConnectNGame.src.participants.AIs import simple_AI
from unittest.mock import patch
from ConnectNGame.src import board

class TestSimpleAI(unittest.TestCase):

    def setUp(self) -> None:
        self.current_board = board.Board.read_board_from_file('../../config_files/Connect4.txt')

    def test_create_simpleAI_from_input(self):
        name = simple_AI.SimpleAI.generate_simple_AI_name(1)
        random.seed(15)
        piece = simple_AI.SimpleAI.generate_simple_AI_piece()
        type = 'simple'
        with self.subTest('Testing first simpleAI from input...'):
            random.seed(15)
            simple_AI_1 = simple_AI.SimpleAI.create_simple_AI_from_input(1)
            self.assertEqual(simple_AI_1, simple_AI.SimpleAI(name, piece, type))

    def test_generate_simple_AI_name(self):
        name = 'SimpleAi 1'
        player_number = 1
        with self.subTest('Testing first simpleAI name...'):
            self.assertEqual(simple_AI.SimpleAI.generate_simple_AI_name(player_number), name)

    def test_generate_simple_AI_piece(self):
        with self.subTest('Testing first simpleAI piece...'):
            random.seed(67)
            self.assertEqual(simple_AI.SimpleAI.generate_simple_AI_piece(), '*')

    def test_find_win_opportunity(self):
        with self.subTest('Testing first win opportunity...'):
            self.assertIsNone(simple_AI.SimpleAI.find_win_opportunity(self.current_board, '%'))
