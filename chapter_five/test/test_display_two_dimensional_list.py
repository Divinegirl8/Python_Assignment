from unittest import TestCase
from chapter_five.display_two_dimensional_list import *


class Test(TestCase):
    def test_display_table(self):
        result = """          Column 1    Column 2    Column 3    Column 5    
Row 0         1           2           3           5  
Row 1         1           4           5           4  
"""
        element = [[1, 2, 3, 5], [1, 4, 5, 4]]
        self.assertEqual(result,display_table(element))
