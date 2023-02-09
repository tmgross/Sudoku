from Sudoku import *

if __name__ == '__main__':
    board = Sudoku(9, 20)
    board.print()
    board.generate_board()
    print()
    board.print()