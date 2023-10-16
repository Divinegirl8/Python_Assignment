from unittest import TestCase
from atm_validation_package import atm_validation_function
from atm_validation_package.atm_validation_function import separate_digit


class Test(TestCase):
    def test_separate_digit(self):
        expected = [6, 2, 6, 2, 0, 4, 8, 1, 0, 6, 7, 5, 8, 8, 3, 4]
        self.assertEqual(expected, atm_validation_function.separate_digit("4388576018402626"))

    def test_even_position_sum(self):
        self.assertEqual(37, atm_validation_function.even_atm_position(separate_digit("4388576018402626")))

    def test_odd_position_sum(self):
        self.assertEqual(38, atm_validation_function.odd_atm_position(separate_digit("4388576018402626")))

    def test_calculate(self):
        self.assertEqual(75, atm_validation_function.calculate_both_odd_even(separate_digit("4388576018402626")))

    def test_validation(self):
        expected = """
*****************************************
**Credit Card Type: Visa Card
**Credit Card Number: 4388576018402626
**Credit Card Digit Length: 16
**Credit Card Validity Status: Invalid
********************************************
"""
        self.assertEqual(expected, atm_validation_function.check_validity(separate_digit("4388576018402626")))