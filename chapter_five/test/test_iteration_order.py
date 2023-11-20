from unittest import TestCase
from chapter_five.iteration_order import *


class Test(TestCase):
    def test_create_list(self):
        self.assertEqual([[0, 0, 0], [0, 0, 0]], create_list(2, 3))

    def test_fill_list(self):
        self.assertEqual([[1, 2], [3, 4]], fill_list(create_list(2, 2)))

    def test_tabular_format(self):
        result = """           column 0   column 1   column 2   
index0        1          2          3   
index1        4          5          6   
"""
        self.assertEqual(result,tabular_format(fill_list(create_list(2,3))))

