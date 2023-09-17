from unittest import TestCase
from Function import function


class Test(TestCase):
    def test_divide(self):
        self.assertEqual(function.divide(5, 8), 0.62)

    def test_divide_two(self):
        self.assertEqual(function.divide(2, 0), 0)

    def test_divide_three(self):
        self.assertEqual(function.divide(4, 2), 2)

    def test_divide_four(self):
        self.assertEqual(function.divide(2, 4), 0.5)




