from unittest import TestCase
from leet_code.add_sum import Solution


class AddSUmTest(TestCase):
    def test_case_one(self):
        list_of_numbers = [2, 7, 11, 15]
        expected = [0, 1]
        self.assertEqual(expected, Solution.twoSum(list_of_numbers, 9))

    def test_case_two(self):
        list_of_numbers = [3, 2, 4]
        expected = [1, 2]
        self.assertEqual(expected, Solution.twoSum(list_of_numbers, 6))

    def test_case_three(self):
        list_of_numbers = [3, 3]
        expected = [0, 1]
        self.assertEqual(expected, Solution.twoSum(list_of_numbers, 6))
