from unittest import TestCase
from cornflakes.dict.strings_dict.difference import difference_list, minimum_list, maximum_list


class Test(TestCase):
    def test_maximum(self):
        sample_input = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        self.assertEqual(75,maximum_list(sample_input))

    def test_minimum(self):
        sample_input = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        self.assertEqual(5, minimum_list(sample_input))

    def test_difference(self):
        sample_input = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        self.assertEqual(70, difference_list(sample_input))

    def test_difference2(self):
        sample_input = [20, 30, 15]
        self.assertEqual(15, difference_list(sample_input))


