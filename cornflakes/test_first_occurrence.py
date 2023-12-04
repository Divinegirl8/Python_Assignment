from unittest import TestCase
from cornflakes.first_occurrence import replace_occurrence


class Test(TestCase):
    def test_replace_occurrence(self):
        self.assertEqual("resta$t", replace_occurrence("restart", "$"))
        self.assertEqual("tee/h", replace_occurrence("teeth", "/"))
        self.assertEqual("rest", replace_occurrence("rest", "|"))
        self.assertEqual("ma--al", replace_occurrence("mammal", "-"))
        self.assertEqual("tesit", replace_occurrence("testt", "i"))
