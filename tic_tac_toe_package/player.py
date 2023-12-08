from tic_tac_toe_package.tic_tac_toe import TicTacToe
from tic_tac_toe_package.cell_value import CeilValue
from tic_tac_toe_package.exceptions.cell_has_been_taken_error import CeilHasBeenTakenError
from tic_tac_toe_package.exceptions.invalid_input_error import InvalidInputError


class Player:
    def __init__(self):
        self.__tic_tac_toe = TicTacToe().get_board()
        self.__player = True

    def get_player(self):
        return self.__player

    def get_new_board(self):
        return self.__tic_tac_toe

    def play(self, square_index):
        ceil = CeilValue.X.value if self.__player else CeilValue.O.value
        self.switch_player()

        match square_index:
            case "1":
                return self.make_move(0, 0, ceil)
            case "2":
                return self.make_move(0, 1, ceil)
            case "3":
                return self.make_move(0, 2, ceil)
            case "4":
                return self.make_move(1, 0, ceil)
            case "5":
                return self.make_move(1, 1, ceil)
            case "6":
                return self.make_move(1, 2, ceil)
            case "7":
                return self.make_move(2, 0, ceil)
            case "8":
                return self.make_move(2, 1, ceil)
            case "9":
                return self.make_move(2, 2, ceil)
            case _:
                raise InvalidInputError("Error choose between 1 - 9")

    def make_move(self, row, column, ceil_value):
        if self.__tic_tac_toe[row][column] == CeilValue.EMPTY.value:
            self.__tic_tac_toe[row][column] = ceil_value
        else:
            raise CeilHasBeenTakenError("This cell has been taken by your opponent")

    def check_winner(self, current_player):
        cell_values = CeilValue.X.value if current_player else CeilValue.O.value

        # Check rows and columns
        for index in range(3):
            if (self.__tic_tac_toe[index][0] == cell_values and
                self.__tic_tac_toe[index][1] == cell_values and
                self.__tic_tac_toe[index][2] == cell_values) or (
                    self.__tic_tac_toe[0][index] == cell_values and
                    self.__tic_tac_toe[1][index] == cell_values and
                    self.__tic_tac_toe[2][index] == cell_values):
                return True

        if (self.__tic_tac_toe[0][0] == cell_values and
            self.__tic_tac_toe[1][1] == cell_values and
            self.__tic_tac_toe[2][2] == cell_values) or (
                self.__tic_tac_toe[0][2] == cell_values and
                self.__tic_tac_toe[1][1] == cell_values and
                self.__tic_tac_toe[2][0] == cell_values):
            return True

        return False

    def print_board(self):
        for row in self.__tic_tac_toe:
            print('\n')
            for column in row:
                print(f"{column:<8}", end="\t")

    def is_board_full(self):
        for row in self.__tic_tac_toe:
            for column in row:
                if column == CeilValue.EMPTY.value:
                    return False
        return True

    def switch_player(self):
        self.__player = not self.__player
