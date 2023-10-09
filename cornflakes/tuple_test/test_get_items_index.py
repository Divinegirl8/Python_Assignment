from unittest import TestCase
from cornflakes.tuple import get_items_index


class Test(TestCase):
    def test_item_index(self):
        my_list = ("Orange", [10, 20, 30], [5, 15, 25])
        self.assertEqual(((0, 20), (1, 25)),get_items_index.item_index(my_list))
