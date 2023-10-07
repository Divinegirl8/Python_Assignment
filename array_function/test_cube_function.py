import unittest
from array_function import cube_function


class MyTestCase(unittest.TestCase):
    def test_something(self):
        number = [3, 7, 2, 6, 5]
        expected = [27, 343, 8, 216, 125]
        self.assertEqual(expected, cube_function.cube_function(number))



