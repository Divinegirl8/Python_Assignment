from unittest import TestCase
from Function import function


class Test(TestCase):
    def test_mean(self):
        numbers = [9, 11, 22, 34, 17, 22, 34, 22 ,40]
        self.assertEqual('23.4',function.mean(numbers))
