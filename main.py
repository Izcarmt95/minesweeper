from minesweeper import Minesweeper
import sys


def main() -> None:
    """
    Main function for the game.
    """
    
    minesweeper = Minesweeper()
    minesweeper.set_board()
    print(minesweeper)
    

if __name__ == '__main__':
    main()