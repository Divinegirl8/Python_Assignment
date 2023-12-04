import enum

from tic_tac_toe_package.tic_tac_toe import TicTacToe
from tic_tac_toe_package.ceil_value import CeilValue
from tic_tac_toe_package.exceptions.ceil_has_been_taken_error import CeilHasBeenTakenError


class Player:
    def __init__(self, player_name):
        self.__player_name = player_name
        self.__tic_tac_toe = TicTacToe().get_board()
        self.__first_player = True

    def get_player_name(self):
        return self.__player_name

    def get_new_board(self):
        return self.__tic_tac_toe

    def move(self, square_index):
        ceil = CeilValue.X.value if self.__first_player else CeilValue.O.value
        self.__first_player = False

        match square_index:
            case "1":
                self.first_index(ceil)
            case "2":
                self.second_index(ceil)
            case "3":
                self.third_index(ceil)
            case "4":
                self.fourth_index(ceil)
            case "5":
                self.fifth_index(ceil)
            case "6":
                self.sixth_index(ceil)
            case "7":
                self.seventh_index(ceil)
            case "8":
                self.eight_index(ceil)
            case "9":
                self.ninth_index(ceil)

    def first_index(self, ceil_value):
        if self.__tic_tac_toe[0][0] == CeilValue.EMPTY.value:
            self.__tic_tac_toe[0][0] = ceil_value
        else:
            raise CeilHasBeenTakenError("This ceil has been taken by your opponent")

    def second_index(self, ceil_value):
        if self.__tic_tac_toe[0][1] == CeilValue.EMPTY.value:
            self.__tic_tac_toe[0][1] = ceil_value
        else:
            raise CeilHasBeenTakenError("This ceil has been taken by your opponent")

    def third_index(self, ceil_value):
        if self.__tic_tac_toe[0][2] == CeilValue.EMPTY.value:
            self.__tic_tac_toe[0][2] = ceil_value
        else:
            raise CeilHasBeenTakenError("This ceil has been taken by your opponent")

    def fourth_index(self, ceil_value):
        if self.__tic_tac_toe[1][0] == CeilValue.EMPTY.value:
            self.__tic_tac_toe[1][0] = ceil_value
        else:
            raise CeilHasBeenTakenError("This ceil has been taken by your opponent")

    def fifth_index(self, ceil_value):
        if self.__tic_tac_toe[1][1] == CeilValue.EMPTY.value:
            self.__tic_tac_toe[1][1] = ceil_value
        else:
            raise CeilHasBeenTakenError("This ceil has been taken by your opponent")

    def sixth_index(self, ceil_value):
        if self.__tic_tac_toe[1][2] == CeilValue.EMPTY.value:
            self.__tic_tac_toe[1][2] = ceil_value
        else:
            raise CeilHasBeenTakenError("This ceil has been taken by your opponent")

    def seventh_index(self, ceil_value):
        if self.__tic_tac_toe[2][0] == CeilValue.EMPTY.value:
            self.__tic_tac_toe[2][0] = ceil_value
        else:
            raise CeilHasBeenTakenError("This ceil has been taken by your opponent")

    def eight_index(self, ceil_value):
        if self.__tic_tac_toe[2][1] == CeilValue.EMPTY.value:
            self.__tic_tac_toe[2][1] = ceil_value
        else:
            raise CeilHasBeenTakenError("This ceil has been taken by your opponent")

    def ninth_index(self, ceil_value):
        if self.__tic_tac_toe[2][2] == CeilValue.EMPTY.value:
            self.__tic_tac_toe[2][2] = ceil_value
        else:
            raise CeilHasBeenTakenError("This ceil has been taken by your opponent")


player = Player("divine")
player.move("1")
player.move("2")
player.move("3")
player.move("4")
player.move("5")
player.move("6")
player.move("7")
player.move("8")
player.move("9")
print(player.get_new_board())
