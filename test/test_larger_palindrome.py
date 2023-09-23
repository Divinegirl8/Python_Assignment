from unittest import TestCase
from Function import function

class Test(TestCase):
    def test_palindrome(self):
        self.assertTrue(function.is_palindrome(1111))

    def test_not_palindrome(self):
        self.assertFalse(function.is_palindrome(1234567891))
