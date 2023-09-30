from unittest import TestCase
from array_function import list_function


class Test(TestCase):
    def test_odd_number(self):
        list_number = [10, 20, 30, 50, 70, 150, 165]
        expected_result = [20, 50, 150]
        result = list_function.odd_number(list_number)
        self.assertEqual(result, expected_result)

    def test_odd_number_two(self):
        list_number = [10, 165]
        expected_result = [165]
        result = list_function.odd_number(list_number)
        self.assertEqual(result, expected_result)
