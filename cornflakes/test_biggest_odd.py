from unittest import TestCase
from cornflakes.biggest_odd_function import biggest_odd


class Test(TestCase):
    def test_one(self):
        letters = '23569'
        self.assertEqual('9', biggest_odd(letters))

    def test_two(self):
        letters = '23715'
        self.assertEqual('7', biggest_odd(letters))
