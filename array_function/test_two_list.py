from unittest import TestCase
from array_function import list_function


class Test(TestCase):
    def test_two_list(self):
        number_list = ["a", "b", "c", "d", "e"]
        letter_list = [1, 2, 3, 4, 5]
        self.assertEqual('[a,1,b,2,c,3,d,4,e,5]', list_function.two_list(number_list, letter_list))

    def test_two_list_two(self):
        number_list = ["dog", "cat"]
        letter_list = [4, 5]
        self.assertEqual('[dog,4,cat,5]', list_function.two_list(number_list, letter_list))