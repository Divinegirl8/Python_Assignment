from unittest import TestCase
from array_function import list_function


class Test(TestCase):
    def test_running_total(self):
        number = [1, 2, 3, 4]
        self.assertEqual(' 1 3 6 10 ', list_function.running_total(number))

    def test_running_total_two(self):
        number = [1, 2, 5, 4, 3]
        self.assertEqual(' 1 3 8 12 15 ', list_function.running_total(number))

    def test_running_total_three(self):
        number = [1, 2, 5, 1]
        self.assertEqual(' 1 3 8 9 ', list_function.running_total(number))

    def test_running_total_four(self):
        number = [1, 2, 5, 1, -9, -3, 2]
        self.assertEqual(' 1 3 8 9 0 -3 -1 ', list_function.running_total(number))
