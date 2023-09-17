from unittest import TestCase
from Function import function


class Test(TestCase):
    def test_factorial_of_five(self):
        self.assertEqual(function.factorial(5),120)

    def test_factorial_of_eight(self):
        self.assertEqual(function.factorial(8),40320)
