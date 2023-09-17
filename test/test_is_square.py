from unittest import TestCase
from Function import function


class Test(TestCase):
    def test_is_square(self):
        self.assertTrue(function.is_square(25))

    def test_is_square_two(self):
        self.assertTrue(function.is_square(121))

    def test_is_not_square(self):
        self.assertFalse(function.is_square(2))
