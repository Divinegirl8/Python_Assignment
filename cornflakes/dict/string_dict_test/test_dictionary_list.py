from unittest import TestCase
from cornflakes.dict.strings_dict.dict_list import list_to_dictionary,capitalize_word


class Test(TestCase):
    def test_list_one(self):
        sample_input = ['apple', 'banana', 'coconut']
        expected = {'a': 'apple', 'b': 'banana', 'c': 'coconut'}
        self.assertEqual(expected, list_to_dictionary(capitalize_word(sample_input)))

    def test_list_two(self):
        sample_input = ['Nigeria', 'Canada', 'Dubai']
        expected = {'N': 'Nigeria', 'C': 'Canada', 'D': 'Dubai'}
        self.assertEqual(expected, list_to_dictionary(capitalize_word(sample_input)))

    def test_list_three(self):
        my_list = ["apple", "banana", "carrot", "corn"]
        expected = {'a': 'apple', 'b': 'banana', 'C': 'Carrot', 'c': 'corn'}
        self.assertEqual(expected, list_to_dictionary(capitalize_word(my_list)))
