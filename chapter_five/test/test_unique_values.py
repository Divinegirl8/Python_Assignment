from unittest import TestCase
from chapter_five.unique_values import *


class Test(TestCase):
    def test_illuminate_unique_values(self):
        list_v = [3, 3, 1, 1, 2]
        result = [1, 3]
        self.assertEqual(result, illuminate_unique_values(list_v))
