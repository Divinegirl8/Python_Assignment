from unittest import TestCase
from chapter_five.palindrome import palindrome_tester


class Test(TestCase):
    def test_palindrome_tester(self):
        self.assertTrue(palindrome_tester("radar"))
        self.assertFalse(palindrome_tester("dog"))
        self.assertTrue(palindrome_tester("11011"))
        self.assertTrue(palindrome_tester("noon"))
        self.assertTrue(palindrome_tester("dad"))
        self.assertFalse(palindrome_tester("sister"))
        self.assertTrue(palindrome_tester("adA"))
