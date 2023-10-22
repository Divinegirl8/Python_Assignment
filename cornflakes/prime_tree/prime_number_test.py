from unittest import TestCase
from prime_tree_function import prime_number_tree


class Test(TestCase):
    def test_one(self):
        self.assertEqual([5, 5, 5], prime_number_tree(125))

    def test_two(self):
        self.assertEqual([2, 2, 3], prime_number_tree(12))

    def test_three(self):
        self.assertEqual([3, 7], prime_number_tree(21))
