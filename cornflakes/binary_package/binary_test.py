from unittest import TestCase
from binary_function import binary_to_decimal, decimal_to_binary


class Test(TestCase):
    def test_binary_to_decimal(self):
        self.assertEqual(13, binary_to_decimal(1101))
        self.assertEqual(13, binary_to_decimal(-1101))
        self.assertEqual(4,binary_to_decimal(1-101))

    def test_decimal_to_binary(self):
        self.assertEqual(1101, decimal_to_binary(binary_to_decimal(1101)))
        self.assertEqual(10101110, decimal_to_binary(-174))
