from unittest import TestCase
from array_function import list_function


class Test(TestCase):
    def test_reverse_number_one(self):
        list_number = [10, 20, 30, 50, 70, 150, 165]
        expected_result = [165, 150, 70, 50, 30, 20, 10]
        result = list_function.reverse_list(list_number)
        self.assertEqual(result, expected_result)

    def test_reverse_number_two(self):
        list_number = [70, 150, 165]
        expected_result = [165, 150, 70]
        result = list_function.reverse_list(list_number)
        self.assertEqual(result, expected_result)
