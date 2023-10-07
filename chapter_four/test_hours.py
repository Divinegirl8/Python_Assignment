from unittest import TestCase
from chapter_four import hours


class Test(TestCase):
    def test_seconds_since_midnight(self):
        self.assertEqual(hours.seconds_since_midnight(13, 30, 45), 48645)
        self.assertEqual(hours.seconds_since_midnight(1, 30, 45), 5445)
