from unittest import TestCase
from sk.count_string import count_character


class Test(TestCase):
    def test_count_character(self):
        value = 'semicolon.africa'
        expected = {'s': 1, 'e': 1, 'm': 1, 'i': 2, 'c': 2, 'o': 2, 'l': 1, 'n': 1, '.': 1, 'a': 2, 'f': 1, 'r': 1}
        self.assertEquals(expected, count_character(value))
