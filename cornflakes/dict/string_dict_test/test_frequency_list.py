from unittest import TestCase
from cornflakes.dict.strings_dict.frequency import frequency_list


class Test(TestCase):
    def test_one(self):
        sample_input = [1, 1, 1, 1, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
        expected = [1, 2, 5]
        self.assertEqual(expected, frequency_list(sample_input, 2))

    def test_two(self):
        sample_input = [1, 1, 1, 1, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
        expected = [1]
        self.assertEqual(expected, frequency_list(sample_input, 3))

    def test_three(self):
        sample_input = [1, 1, 1, 1, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
        expected = [1, 2, 3, 5, 6, 7]
        self.assertEqual(expected, frequency_list(sample_input, 0))

    def test_four(self):
        sample_input = [1, 1, 1, 1, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
        expected = [1, 2, 3, 5]
        self.assertEqual(expected, frequency_list(sample_input, 1))
