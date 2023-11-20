from unittest import TestCase
from chapter_five.anagrams import *


class Test(TestCase):
    def test_anagram(self):
        self.assertTrue("love", "evol")
        self.assertTrue("listen", "silent")
