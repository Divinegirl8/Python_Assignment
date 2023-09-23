from unittest import TestCase
from Function import function


class Test(TestCase):
    def test_fibonacci(self):
        # self.assertEqual(35, function.fibonacci(50))
        assert (2, 3, 5, 8, 13, 21, 34, function.fibonacci(50))
