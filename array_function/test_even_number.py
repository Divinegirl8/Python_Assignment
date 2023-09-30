from unittest import TestCase
from array_function import list_function


class Test(TestCase):
    def test_even_number(self):
        list_number = [10, 20, 30, 50, 70, 150, 165]
        expected_result = [10, 30, 70, 165]
        result = list_function.even_number(list_number)
        self.assertEqual(result, expected_result)

    def test_even_number_two(self):
        list_number = [70, 150, 165]
        expected_result = [70, 165]
        result = list_function.even_number(list_number)
        self.assertEqual(result, expected_result)
