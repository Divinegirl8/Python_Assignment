from unittest import TestCase
from Function import function


class Test(TestCase):
    def test_is_prime(self):
        self.assertEqual(function.is_prime(7), True)

    def test_is_not_prime(self):
        self.assertEqual(function.is_prime(20),False)
