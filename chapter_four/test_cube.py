from unittest import TestCase
from chapter_four import cube


class Test(TestCase):
    def test_cube(self):
        self.assertEqual(cube.cube(2), 8)
        self.assertEqual(cube.cube(-2), -8)
