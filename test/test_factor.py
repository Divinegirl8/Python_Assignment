from unittest import TestCase
from Function import  function


class Test(TestCase):
    def test_factor_of_ten(self):
        self.assertEqual(function.factor_of(10),4)

    def test_factor_of_five(self):
        self.assertEqual(function.factor_of(5), 2)

    def test_factor_of_twelve(self):
        self.assertEqual(function.factor_of(12), 6)

