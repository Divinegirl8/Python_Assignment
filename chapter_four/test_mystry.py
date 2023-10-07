import unittest
from chapter_four import mystery;


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(mystery.mystery([1, 2, 3, 4, 5]), 55)


if __name__ == '__main__':
    unittest.main()
