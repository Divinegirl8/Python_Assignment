from unittest import TestCase
from array_function import list_function


class Test(TestCase):
    def test_summation_for_loop(self):
        numbers = [1, 2, 3]
        self.assertEqual('6.0', list_function.summation_for_loop(numbers))

    def test_summation_for_loop_two(self):
        numbers = [1, 2, -3]
        self.assertEqual('0.0', list_function.summation_for_loop(numbers))

    def test_summation_for_loop_three(self):
        numbers = [15.3, 2.1, 3]
        self.assertEqual('20.4', list_function.summation_for_loop(numbers))

    def test_summation_while_loop(self):
        numbers = [1, 2, 3]
        self.assertEqual('6.0', list_function.summation_while_loop(numbers))

    def test_summation_while_loop_two(self):
        numbers = [1, 2, 3, 90, 123]
        self.assertEqual('219.0', list_function.summation_while_loop(numbers))
