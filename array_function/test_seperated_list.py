from unittest import TestCase
from array_function import list_function


class Test(TestCase):
    def test_seperated_list(self):
        name = ["a", "b", "c", "d", "e"]
        number = [1, 2, 3, 5, 6]
        self.assertEqual('[a,b,c,d,e,1,2,3,5,6]', list_function.seperated_list(name, number))

    def test_seperated_list_two(self):
        name = ["a", "b", "c", "d", "e", "z", "y"]
        number = [1, 2, 3, 5, 6]
        self.assertEqual('[a,b,c,d,e,z,y,1,2,3,5,6]', list_function.seperated_list(name, number))

    def test_seperated_list_three(self):
        name = ["go"]
        number = [2]
        self.assertEqual('[go,2]', list_function.seperated_list(name, number))

