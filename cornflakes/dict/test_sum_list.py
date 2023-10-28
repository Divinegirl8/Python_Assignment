from unittest import TestCase
from cornflakes.dict.sum_list import sum_list


class Test(TestCase):
    def test_sum_list(self):
        number_list = [[2, 4, 5, 6], [2, 3, 5, 6]]
        self.assertEqual(33,sum_list(number_list))
