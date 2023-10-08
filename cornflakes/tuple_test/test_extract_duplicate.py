import unittest
from cornflakes.tuple import most_appearing


class MyTestCase(unittest.TestCase):
    def test_something(self):
        tuple5 = 20, 10, 15, 20, 5, 30, 10, 35, 10, 40, 45, 5
        self.assertEqual((5, 10, 20), most_appearing.extract_duplicate(tuple5))  # add assertion here

    def test_two(self):
        tuple5 = 2, 1, 2
        self.assertEqual((2,),most_appearing.extract_duplicate(tuple5))
