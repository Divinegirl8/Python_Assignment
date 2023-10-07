import unittest
from chapter_four import modify


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(modify.average(4, 2, 9, 0), '3.75')
        self.assertEqual(modify.average(2, 2), '2.0')
