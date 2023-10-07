import unittest
from cornflakes.tuple import reverse_tuple


class MyTestCase(unittest.TestCase):
    def test_something(self):
        tuple1 = (10, 20, 30, 40, 50)
        self.assertEqual((50, 40, 30, 20, 10), reverse_tuple.reverse_tuple(tuple1))

    def test_something_2(self):
        tuple1 = (54, 43)
        self.assertEqual((43, 54), reverse_tuple.reverse_tuple(tuple1))
