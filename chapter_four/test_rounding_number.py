import unittest
from chapter_four import round_number


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = '13.6\n13.56\n13.564\n13.5645\n'
        self.assertEqual(result, round_number.rounding(13.56449))


