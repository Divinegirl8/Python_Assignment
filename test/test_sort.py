from unittest import TestCase
from Function import function


class Test(TestCase):
    def test_sort_number(self):
        input_list = [5, 4, 3, 2, 1]
        expected_result = [1, 2, 3, 4, 5]
        result = function.sort_number(input_list)
        self.assertEqual(result, expected_result)

    def test_sort_number_one(self):
        input_list = [9, 7, 6, 5, 4]
        expected_result = [4, 5, 6, 7, 9]
        result = function.sort_number(input_list)
        self.assertEqual(result, expected_result)
