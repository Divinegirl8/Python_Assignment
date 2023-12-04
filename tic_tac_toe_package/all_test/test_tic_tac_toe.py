from unittest import TestCase
from tic_tac_toe_package.tic_tac_toe import TicTacToe


class TicTacToeTest(TestCase):
    def test_my_list_has_empty_enum_in_the_board_ceil(self):
        tic_tac_toe = TicTacToe()
        expected = [['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY']]
        self.assertEqual(expected,tic_tac_toe.get_board())


