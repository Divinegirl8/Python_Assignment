from unittest import TestCase
from array_function import list_function


class Test(TestCase):
    def test_one(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], list_function.list_digits(1234567))

    def test_two(self):
        self.assertEqual([9], list_function.list_digits(9))