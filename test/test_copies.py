from unittest import TestCase
from Function import function


class Test(TestCase):
    def test_below_four_copies(self):
        self.assertEqual(function.copies(3), 2000)

    def test_below_nine_copies(self):
        self.assertEqual(function.copies(6), 1800)

    def test_below_twenty_nine_copies(self):
        self.assertEqual(function.copies(21), 1600)

    def test_below_forty_nine_copies(self):
        self.assertEqual(function.copies(49), 1500)

    def test_below_ninty_nine_copies(self):
        self.assertEqual(function.copies(87), 1300)

    def test_below_hundred_ninety_nine_copies(self):
        self.assertEqual(function.copies(180), 1200)

    def test_below_nine_copies(self):
        self.assertEqual(function.copies(300), 1100)

    def test_above_five_hundred_copies(self):
        self.assertEqual(function.copies(673), 1000)
