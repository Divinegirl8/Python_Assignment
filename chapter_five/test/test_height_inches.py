from chapter_five.height_inches import *
import unittest


class Test(unittest.TestCase):
    def test_height_lambda(self):
        self.assertEqual([(69, 1.7526), (77, 1.9558), (54, 1.3716)], height([69,77,54]))

    def test_height_comprehension(self):
        self.assertEqual([(69, 1.7526), (77, 1.9558), (54, 1.3716)],height_comprehension([69,77,54]))
