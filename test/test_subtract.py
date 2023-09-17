from unittest import TestCase
from Function import function


class Test(TestCase):
    def test_subtract_one(self):
        self.assertEqual(function.subtract(3, 7), 4)

    def test_subtract_two(self):
        self.assertEqual(function.subtract(7, 3), 4)
