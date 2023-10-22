from unittest import TestCase
from cornflakes.femi import check_element


class Test(TestCase):
    def test_check_element(self):
        input = ["ABC21F", "103cpz", "A1L"]
        self.assertEqual(6,check_element(input))
