import unittest
from cornflakes.tuple import unpacks


class MyTestCase(unittest.TestCase):
    def test_something(self):
        tuple3 = 15, 25, 60, 50, 30, 40, 45, 55
        self.assertEqual((55, 15), unpacks.unpacking(tuple3))

    def test_two(self):
        tuple3 = 60, 50
        self.assertEqual((50, 60), unpacks.unpacking(tuple3))

    def test_three(self):
        tuple3 = 10,
        self.assertEqual((10, 10), unpacks.unpacking(tuple3))
