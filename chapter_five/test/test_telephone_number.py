from unittest import TestCase
from chapter_five.telephone_number import *


class Test(TestCase):
    def test_non_digit(self):
        number = "244 - @3282"
        self.assertEqual("2443282",remove_non_digit_number(number))
