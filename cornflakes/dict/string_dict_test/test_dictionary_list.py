from unittest import TestCase
from cornflakes.dict.strings_dict.dict_list import list_to_dictionary


class Test(TestCase):
    def test_list_one(self):
        sample_input = ['apple', 'banana', 'coconut']
        expected = {'a': 'apple', 'b': 'banana', 'c': 'coconut'}
        self.assertEqual(expected, list_to_dictionary(sample_input))

    def test_list_two(self):
        sample_input = ['Nigeria', 'Canada', 'Dubai']
        expected = {'N': 'Nigeria', 'C': 'Canada', 'D': 'Dubai'}
        self.assertEqual(expected, list_to_dictionary(sample_input))
