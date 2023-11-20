from unittest import TestCase
from chapter_five.telephone_number2 import *


class Test(TestCase):
    def test_telephone_letters(self):
        value = 'BIGDATA'
        self.assertEqual("2443282", telephone_letters(value))

    def test_length_is_not_seven(self):
        value = 'BIGDATAS'
        self.assertEqual("Error", telephone_letters(value))
