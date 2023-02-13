import random
import math


class Sudoku:
    def __init__(self, size=9, num_remove=50):
        """ Sudoku constructor
        :param size: length of each side of the grid (default 9)
        :param num_remove: number of cells to remove to create a board to solve (default 40)
        """
        self.__size = size
        self.__num_remove = num_remove
        self.__matrix = [[0 for _ in range(size)] for _ in range(size)]

    def generate_board(self):
        """
        Randomly generates a full Sudoku board and removes num_remove tiles from the grid
        """
        self.__fill_board()
        self.__create_user_grid()

    def get_value(self, row, col):
        """
        Returns the value of matrix[row][col]
        :param row: row of cell
        :param col: column of cell
        :return: Value of matrix[row][col]
        """
        return self.__matrix[row][col]

    def set_value(self, n, row, col):
        """
        Assigns n into matrix[row][col]
        :param n: number to assign to cell
        :param row: row of cell
        :param col: column of cell
        """
        self.__matrix[row][col] = n

    def clear(self):
        """
        Sets the value of every cell to 0
        """
        for i in range(self.__size):
            for j in range(self.__size):
                self.__matrix[i][j] = 0

    def __fill_board(self):
        self.__fill_diagonals()
        self.__fill_values(0, 0)

    def __fill_diagonals(self):
        for k in range(3):
            nums = [x for x in range(1, 10)]
            random.shuffle(nums)
            counter = -1
            for i in range(3):
                for j in range(3):
                    self.__matrix[(k * 3) + i][(k * 3) + j] = nums[(counter := counter + 1)]

    def __fill_values(self, row, col):
        if row == self.__size - 1 and col == self.__size:
            return True

        if col == self.__size:
            row += 1
            col = 0

        if self.__matrix[row][col] != 0:
            return self.__fill_values(row, col + 1)

        for i in range(1, 10):
            if self.__valid_placement(i, row, col):
                self.__matrix[row][col] = i
                if self.__fill_values(row, col + 1):
                    return True
                self.__matrix[row][col] = 0

        return False

    def __valid_row(self, n, row):
        for i in range(self.__size):
            if self.__matrix[row][i] == n:
                return False
        return True

    def __valid_col(self, n, col):
        for i in range(self.__size):
            if self.__matrix[i][col] == n:
                return False
        return True

    def __valid_box(self, n, row, col):
        col_offset = col - col % 3
        row_offset = row - row % 3
        for i in range(3):
            for j in range(3):
                if self.__matrix[i + row_offset][j + col_offset] == n:
                    return False
        return True

    def __valid_placement(self, n, row, col):
        return self.__valid_row(n, row) and self.__valid_col(n, col) and self.__valid_box(n, row, col)

    def __create_user_grid(self):
        i = 0
        while i < self.__num_remove:
            rand_row = random.randint(0, self.__size - 1)
            rand_col = random.randint(0, self.__size - 1)
            if self.__matrix[rand_row][rand_col] == 0:
                i -= 1
            else:
                self.__matrix[rand_row][rand_col] = 0
            i += 1

    def print(self):
        """
        Prints out the current state of the Sudoku board
        """
        for i in range(self.__size):
            if i % 3 == 0: print('-' * (self.__size * 2 + int(math.sqrt(self.__size))))
            for j in range(self.__size):
                if j % 3 == 0: print('|', end="")
                print(self.__matrix[i][j], end=" ")
            print('|')
        print('-' * int((self.__size * 2 + math.sqrt(self.__size))))
