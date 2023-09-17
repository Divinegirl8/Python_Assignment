from unittest import TestCase
from Function import function


class Test(TestCase):
    def test_is_palindrome(self):
        self.assertTrue(function.palindrome(12211))

    def test_is_not_palindrome(self):
        self.assertFalse(function.palindrome(12215))

