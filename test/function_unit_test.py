import unittest
from Function import function


class MyTestCase(unittest.TestCase):
    def test_range_below_fifty(self):
        self.assertEqual(function.commission(40), 11400)

    def test_range_below_fifty_nine(self):
        self.assertEqual(function.commission(55), 16000)

    def test_range_below_sixty_nine(self):
        self.assertEqual(function.commission(63), 20750)

    def test_range_above_seventy(self):
        self.assertEqual(function.commission(97), 53500)


if __name__ == '__main__':
    unittest.main()
