from tic_tac_toe_package.cell_value import CeilValue
from unittest import TestCase


class TestCeilValue(TestCase):
    def test_all_the_value_in_ceil_value_enum(self):
        self.assertEqual('EMPTY', CeilValue.EMPTY.value)
        self.assertEqual('X', CeilValue.X.value)
        self.assertEqual("O",CeilValue.O.value)
