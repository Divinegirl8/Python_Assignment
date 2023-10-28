from unittest import TestCase
from cornflakes.dict.strings_dict.two_list_to_dictionary import two_list


class Test(TestCase):
    def test_one(self):
        element1 = ['a', 'b', 'c', 'd', 'e']
        element2 = [1, 2, 3, 4, 5]
        expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.assertEqual(expected, two_list(element1, element2))

    def test_two(self):
        element1 = [2, 3, 4, 6, 9]
        element2 = ["chicken", "goat", "turkey", "bags of rice", "basket of tomato"]
        expected = {2: 'chicken', 3: 'goat', 4: 'turkey', 6: 'bags of rice', 9: 'basket of tomato'}
        self.assertEqual(expected, two_list(element1, element2))
