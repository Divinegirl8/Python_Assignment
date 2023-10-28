from unittest import TestCase
from cornflakes.dict.strings_dict.remove_empty_string import empty_string


class Test(TestCase):
    def test_one(self):
        sample_input = ['', 'ABC', 'xyz', '', 'abc', 'XYZ']
        expected = ['ABC', 'xyz', 'abc', 'XYZ']
        self.assertEqual(expected, empty_string(sample_input))

    def test_two(self):
        sample_input = ['', 'Mr Ayinlade', "", "", "", '', '', "Sikiru"]
        expected = ['Mr Ayinlade', "Sikiru"]
        self.assertEqual(expected, empty_string(sample_input))
