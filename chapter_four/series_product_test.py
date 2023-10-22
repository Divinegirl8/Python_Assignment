from unittest import TestCase
from chapter_four.arbitiary_list import series_product


class Test(TestCase):
    def test_app(self):
        self.assertEqual(6, series_product(1, 2, 3))

    def test_app2(self):
        self.assertEqual(100, series_product(1, 2, 5, 10))

    def test_app3(self):
        self.assertEqual(1, series_product(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ))
