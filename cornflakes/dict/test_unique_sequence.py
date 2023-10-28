from unittest import TestCase
from cornflakes.dict.unique_sequence import unique_sequence_of


class Test(TestCase):
    def test_unique_sequence(self):
        sample_list = [1, 3, 2, 5, 3, 4, 6, 4, 6, 9, 8, 2, 10, 8, 6, 12, 15, 10, 4, 6, 14]
        expected = {2, 4, 6, 8, 10, 12, 14}
        self.assertEqual(expected, unique_sequence_of(sample_list))
