import unittest
from cornflakes.tuple import tuple_sort


class MyTestCase(unittest.TestCase):
    def test_something(self):
        tuple4 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
        self.assertEqual((('c', 11), ('a', 23), ('d', 29), ('b', 37)), tuple_sort.sort_tuple(tuple4))

    def test_something_two(self):
        tuple4 = (('b', 37), ('d', 29))
        self.assertEqual((('d', 29), ('b', 37)), tuple_sort.sort_tuple(tuple4))


