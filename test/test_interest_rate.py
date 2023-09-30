from unittest import TestCase
from Function import function


class Test(TestCase):
    def test_interest_rate(self):
        self.assertEqual("1628.9", function.interestRate(5, 10, 1000))

    def test_interest_rate_two(self):
        self.assertEqual("510.0", function.interestRate(2, 1, 500))
