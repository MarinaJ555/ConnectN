import sys
from ConnectNGame.src.board import Board
from ConnectNGame.src.game import Game
import random


def main() -> None:
    path_to_board_file = str(sys.argv[1]) # get the board file
    if len(sys.argv) > 2:
        seed_value = int(sys.argv[2])
        random.seed(seed_value)
    current_board = Board.read_board_from_file(path_to_board_file) # create the board
    current_game = Game(current_board) # create the game
    current_game.setup_game()

    while True:
        done = current_game.play() # play the game until a player wins or there is a tie
        if done == True:
            break
        else:
            continue

if __name__ == '__main__':
    main()