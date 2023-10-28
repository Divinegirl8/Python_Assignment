from unittest import TestCase
from cornflakes.dict.string_count import count_string


class Test(TestCase):
    def test_count_string(self):
        sample = "google.com"
        expected = {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
        self.assertEqual(expected, count_string(sample))

    def test_count_string2(self):
        sample = "noon"
        expected = {'n': 2, 'o': 2}
        self.assertEqual(expected, count_string(sample))

    def test_count_string3(self):
        sample = "bible"
        expected = {'b': 2, 'i': 1, 'l': 1, 'e': 1}
        self.assertEqual(expected, count_string(sample))
