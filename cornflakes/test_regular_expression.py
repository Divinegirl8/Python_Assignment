from unittest import TestCase
from cornflakes import regular_expression


class Test(TestCase):
    def test_adding_ing(self):
        self.assertEqual("stingly", regular_expression.adding_ing("sting"))
        self.assertEqual("abcing", regular_expression.adding_ing("abc"))
        self.assertEqual("it", regular_expression.adding_ing("it"))

    def test_adding_ing2(self):
        self.assertEqual("sortingly", regular_expression.adding_ing("sorting"))
        self.assertEqual("fishing", regular_expression.adding_ing("fish"))
        self.assertEqual("go", regular_expression.adding_ing("go"))

    def test_not_ending(self):
        self.assertEqual("ringly", regular_expression.adding_ing("ring"))
        self.assertEqual("dingoing", regular_expression.adding_ing("dingo"))
