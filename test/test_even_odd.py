from unittest import TestCase
from Function import function


class Test(TestCase):
    def test_is_even(self):
        self.assertEqual(function.is_even(24),True)

    def test_is_odd(self):
        self.assertEqual(function.is_even(99),False)
