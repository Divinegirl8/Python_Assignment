from unittest import TestCase
from group_task.task_function import add_to_list, odd_numbers,double_item


class Test(TestCase):
    def test_add_to_list(self):
        result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertEqual(result, add_to_list(1, 21))

    def test_odd_values(self):
        result = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        self.assertEqual(result, odd_numbers(add_to_list(1, 21)))

    def test_double_values(self):
        result = [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
        self.assertEqual(result,double_item(odd_numbers(add_to_list(1,21))))
