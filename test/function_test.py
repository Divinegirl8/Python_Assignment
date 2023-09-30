import unittest
from Function import function


# def percentage_rate(rate):
#     if rate < 50:
#         return rate * 160 + 5000
#     if rate < 59:
#         return rate * 200 + 5000
#     if rate < 69:
#         return rate * 250 + 5000
#     else:
#         return rate * 500 + 5000


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
