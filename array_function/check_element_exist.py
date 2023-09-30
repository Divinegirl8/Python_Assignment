from unittest import TestCase
from array_function import list_function


class Test(TestCase):
    def test_check_element(self):
        listed_number = [23, 45, 65, 43]
        self.assertTrue(list_function.check_element(listed_number, 23))

    def test_check_element_two(self):
        listed_number = [23, 45, 65, 43]
        self.assertFalse(list_function.check_element(listed_number, 2))

    def test_check_element_three(self):
        listed_number = [23, 45, 65, 43]
        self.assertTrue(list_function.check_element(listed_number, 65))

    def test_check_element_four(self):
        listed_number = [23, 45, 65, 43]
        self.assertFalse(list_function.check_element(listed_number, -2))

    def test_check_element_five(self):
        listed_number = [23, 45, 65, 43]
        self.assertFalse(list_function.check_element(listed_number, 0))

    def test_check_element_six(self):
        listed_number = [23, 45, 65, 43]
        self.assertFalse(list_function.check_element(listed_number, -0))
