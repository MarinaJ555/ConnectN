import unittest
import random
from ConnectNGame.src.participants.AIs import random_AI


class TestRandomAI(unittest.TestCase):

    def test_create_randomAI_from_input(self):
        name = 'RandomAi 1'
        piece = '%'
        type = 'random'
        with self.subTest('Testing first randomAI from input...'):
            self.assertEqual(random_AI.RandomAI(name, piece, type),
                             random_AI.RandomAI('RandomAi 1', '%', 'random'))

    def test_generate_random_AI_name(self):
        name = 'RandomAi 1'
        with self.subTest('Testing first randomAI name...'):
            self.assertEqual(random_AI.RandomAI.generate_random_AI_name(), name)

    def test_generate_random_AI_piece(self):
        with self.subTest('Testing first randomAI piece...'):
            random.seed(10)
            self.assertEqual(random_AI.RandomAI.generate_random_AI_piece(), 'j')
        with self.subTest('Testing second randomAI piece...'):
            random.seed(99)
            self.assertEqual(random_AI.RandomAI.generate_random_AI_piece(), 'T')
