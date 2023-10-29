from unittest import TestCase
from cornflakes.dict.strings_dict.split_list import split_list


class Test(TestCase):
    def test_one(self):
        value = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        expected = '[10, 75, 20, 30, 15],[5, 40, 25, 40, 35]'
        self.assertEqual(expected, split_list(value))

    def test_two(self):
        value = [20, 30, 15, 5, 40, 25]
        expected = '[20, 30, 15],[5, 40, 25]'
        self.assertEqual(expected, split_list(value))
