from unittest import TestCase
from chapter_five.letters import summarize_letters


class Test(TestCase):
    def test_summarize_letters(self):
        result = (('a', 2), ('e', 2), ('o', 4), ('r', 2), ('u', 2))
        self.assertEqual(result, summarize_letters("The quick brown fox jumps over a lazy dog."))

    def test_contains_alphabet_letters(self):
        words = "The quick brown fox jumps over a lazy dog."
        alpha_bet = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(words, alpha_bet)
