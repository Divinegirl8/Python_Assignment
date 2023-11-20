from unittest import TestCase
from chapter_five.sorted import *


class Test(TestCase):
    def test_is_sorted_list(self):
        value = [1, 2, 3, 4, 5]
        self.assertTrue(is_sorted(value))

    def test_is_not_sorted_list(self):
        value = [21, 3, 2, 15]
        self.assertFalse(is_sorted(value))

    def test_is_sorted_string(self):
        value = "abcdef"
        self.assertTrue(is_sorted(value))

    def test_is_not_sorted_string(self):
        value = "girl"
        self.assertFalse(is_sorted(value))

    def test_is_sorted_tuple(self):
        value = 1, 2, 3, 4, 5
        self.assertTrue(is_sorted(value))

    def test_is_not_sorted_tuple(self):
        value = 43, 2, 12, 1, 0
        self.assertFalse(is_sorted(value))
