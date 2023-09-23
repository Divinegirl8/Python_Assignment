from unittest import TestCase
from Function import function


class Test(TestCase):
    def test_median(self):
        integer = [9, 11, 22, 34, 17, 22, 34, 22 ,40]
        self.assertEqual(22,function.median(integer))

    def test_median_two(self):
        integer = [9,10,2,1]
        self.assertEqual(5.5,function.median(integer))
