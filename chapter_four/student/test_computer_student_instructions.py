from unittest import TestCase
from chapter_four.student.computer_student_instructions import generate_random_single_digit_number


class Test(TestCase):
    def test_generate_random_single_digit_number(self):
        check_number_generated_is_between_0_to_9 = 1 >= generate_random_single_digit_number() <= 9
        self.assertTrue(check_number_generated_is_between_0_to_9)
