import unittest
from chapter_five.rotate_function import *


class Test(unittest.TestCase):
    def test_rotate_function_can_swap(self):
        self.assertEqual((22, "Dough", 1984), rotate("Dough", 1984, 22))


