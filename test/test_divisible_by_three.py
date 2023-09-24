from unittest import TestCase
from cornflakes import divisible_by_three


class Test(TestCase):
    def test_divisible_by_three_one(self):
        self.assertEqual(165,divisible_by_three.divisible_by_three(31))

    def test_divisible_by_three_two(self):
        self.assertEqual(135, divisible_by_three.divisible_by_three(30))

    def test_divisible_by_three_three(self):
        self.assertEqual(0, divisible_by_three.divisible_by_three(-31))
