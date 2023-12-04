from tic_tac_toe_package.ceil_value import CeilValue


class TicTacToe:

    def __init__(self):
        self.__board = [[CeilValue.EMPTY.value for column in range(3)] for row in range(3)]

    def get_board(self):
        return self.__board


