from unittest import TestCase
from array_function import list_function


class Test(TestCase):
    def test_string_palindrome(self):
        self.assertTrue(list_function.string_palindrome("mum"))

    def test_string_palindrome_two(self):
        self.assertFalse(list_function.string_palindrome("sister"))

    def test_string_palindrome_three(self):
        self.assertTrue(list_function.string_palindrome("noon"))
