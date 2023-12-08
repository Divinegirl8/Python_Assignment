from unittest import TestCase
from tic_tac_toe_package.player import Player
from tic_tac_toe_package.tic_tac_toe import TicTacToe
from tic_tac_toe_package.exceptions.cell_has_been_taken_error import CeilHasBeenTakenError
from tic_tac_toe_package.exceptions.invalid_input_error import InvalidInputError


class TestPlayer(TestCase):
    def test_that_a_move_is_made_when_a_player_plays(self):
        tic_tac_toe = TicTacToe()
        player = Player()
        expected = [['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY']]
        self.assertEqual(expected, tic_tac_toe.get_board())

        expected_value = [['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'X']]
        player.play("9")
        self.assertEqual(expected_value, player.get_new_board())

    def test_that_an_error_occurs_if_a_player_chooses_same_value_with_the_opponent(self):
        player = Player()
        player.play("5")
        with self.assertRaises(CeilHasBeenTakenError):
            player.play("5")

    def test_that_an_error_occurs_if_player_chooses_a_value_greater_than_nine(self):
        player = Player()
        with self.assertRaises(InvalidInputError):
            player.play("23")

    def test_that_an_error_occurs_if_player_chooses_a_value_less_than_one(self):
        player = Player()
        with self.assertRaises(InvalidInputError):
            player.play("0")
        with self.assertRaises(InvalidInputError):
            player.play("-1")

    def test_that_a_move_is_made_when_first_player_plays_for_the_first_time(self):
        tic_tac_toe = TicTacToe()
        player = Player()
        expected = [['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY']]
        self.assertEqual(expected, tic_tac_toe.get_board())

        expected_value = [['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'X', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY']]
        player.play("5")
        self.assertEqual(expected_value, player.get_new_board())

    def test_that_a_move_is_made_when_second_player_plays_for_the_first_time(self):
        tic_tac_toe = TicTacToe()
        player = Player()
        expected = [['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY']]
        self.assertEqual(expected, tic_tac_toe.get_board())

        expected_value = [['O', 'EMPTY', 'EMPTY'], ['EMPTY', 'X', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY']]
        player.play("5")
        player.play("1")
        self.assertEqual(expected_value, player.get_new_board())

    def test_that_a_move_is_made_when_first_player_plays_for_the_second_time(self):
        tic_tac_toe = TicTacToe()
        player = Player()
        expected = [['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY']]
        self.assertEqual(expected, tic_tac_toe.get_board())

        expected_value = [['O', 'EMPTY', 'X'], ['EMPTY', 'X', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY']]
        player.play("5")
        player.play("1")
        player.play("3")
        self.assertEqual(expected_value, player.get_new_board())

    def test_that_a_move_is_made_when_second_player_plays_for_the_second_time(self):
        tic_tac_toe = TicTacToe()
        player = Player()
        expected = [['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY']]
        self.assertEqual(expected, tic_tac_toe.get_board())

        expected_value = [['O', 'EMPTY', 'X'], ['EMPTY', 'X', 'EMPTY'], ['EMPTY', 'O', 'EMPTY']]
        player.play("5")
        player.play("1")
        player.play("3")
        player.play("8")
        self.assertEqual(expected_value, player.get_new_board())

    def test_that_a_move_is_made_when_first_player_plays_for_the_third_time(self):
        tic_tac_toe = TicTacToe()
        player = Player()
        expected = [['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY']]
        self.assertEqual(expected, tic_tac_toe.get_board())

        expected_value = [['O', 'X', 'X'], ['EMPTY', 'X', 'EMPTY'], ['EMPTY', 'O', 'EMPTY']]
        player.play("5")
        player.play("1")
        player.play("3")
        player.play("8")
        player.play("2")
        self.assertEqual(expected_value, player.get_new_board())

    def test_that_a_move_is_made_when_second_player_plays_for_the_third_time(self):
        tic_tac_toe = TicTacToe()
        player = Player()
        expected = [['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY']]
        self.assertEqual(expected, tic_tac_toe.get_board())

        expected_value = [['O', 'X', 'X'], ['O', 'X', 'EMPTY'], ['EMPTY', 'O', 'EMPTY']]
        player.play("5")
        player.play("1")
        player.play("3")
        player.play("8")
        player.play("2")
        player.play("4")
        self.assertEqual(expected_value, player.get_new_board())

    def test_that_a_move_is_made_when_first_player_plays_for_the_fourth_time(self):
        tic_tac_toe = TicTacToe()
        player = Player()
        expected = [['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY']]
        self.assertEqual(expected, tic_tac_toe.get_board())

        expected_value = [['O', 'X', 'X'], ['O', 'X', 'EMPTY'], ['EMPTY', 'O', 'X']]
        player.play("5")
        player.play("1")
        player.play("3")
        player.play("8")
        player.play("2")
        player.play("4")
        player.play("9")
        self.assertEqual(expected_value, player.get_new_board())

    def test_that_a_move_is_made_when_second_player_plays_for_the_fourth_time(self):
        tic_tac_toe = TicTacToe()
        player = Player()
        expected = [['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY']]
        self.assertEqual(expected, tic_tac_toe.get_board())

        expected_value = [['O', 'X', 'X'], ['O', 'X', 'O'], ['EMPTY', 'O', 'X']]
        player.play("5")
        player.play("1")
        player.play("3")
        player.play("8")
        player.play("2")
        player.play("4")
        player.play("9")
        player.play("6")
        self.assertEqual(expected_value, player.get_new_board())

    def test_that_a_move_is_made_when_first_player_plays_for_the_fifth_time(self):
        tic_tac_toe = TicTacToe()
        player = Player()
        expected = [['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY']]
        self.assertEqual(expected, tic_tac_toe.get_board())

        expected_value = [['O', 'X', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]
        player.play("5")
        player.play("1")
        player.play("3")
        player.play("8")
        player.play("2")
        player.play("4")
        player.play("9")
        player.play("6")
        player.play("7")
        self.assertEqual(expected_value, player.get_new_board())
