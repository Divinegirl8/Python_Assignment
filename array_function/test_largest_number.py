from unittest import TestCase
from array_function import list_function


class Test(TestCase):
    def test_largest_number(self):
        list_number = [1, 21, 3, 500]
        self.assertEqual(500,list_function.largest_number(list_number))

    def test_largest_number_two(self):
        list_number = [1, 21, 3122, 500]
        self.assertEqual(3122, list_function.largest_number(list_number))

    def test_largest_number_three(self):
        list_number = [1, 5240]
        self.assertEqual(5240, list_function.largest_number(list_number))


