import unittest
from unittest.mock import patch
from .print_capturer import PrintCapturer
from ConnectNGame.src.example_printing import print_hello, print_list


class TestExamplePrinting(unittest.TestCase):
    def test_print_hello(self):
        capture = PrintCapturer()
        with patch('ConnectNGame.src.example_printing.print', side_effect=capture):
            print_hello()
            self.assertEqual(['Hello\n'], capture.output)

    def test_print_list(self):
        values = [4, 5, 'hi', 'bye']
        capture = PrintCapturer()
        with patch('ConnectNGame.src.example_printing.print', side_effect=capture):
            print_list(values)
            answer = ['4\n', '5\n', 'hi\n', 'bye\n']
            self.assertEqual(answer, capture.output)

    def test_print_list_but_using_as_string(self):
        values = ['It', 'is', 'time to', 'duel!']
        capture = PrintCapturer()
        with patch('ConnectNGame.src.example_printing.print', side_effect=capture):
            print_list(values)
            answer = 'It\nis\ntime to\nduel!\n'
            self.assertEqual(answer, capture.as_string())


if __name__ == '__main__':
    unittest.main()
