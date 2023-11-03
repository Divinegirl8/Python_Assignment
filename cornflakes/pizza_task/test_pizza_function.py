from unittest import TestCase
import pizza_function


class Test(TestCase):
    def test_pizza_box_size(self):
        self.assertEqual("Large", pizza_function.pizza_box_size("Large"))
        self.assertEqual("Medium", pizza_function.pizza_box_size("Medium"))
        self.assertEqual("small", pizza_function.pizza_box_size("small"))

    def test_level_of_eating(self):
        self.assertEqual(4, pizza_function.number_of_super_hungry_size(4))
        self.assertEqual(6, pizza_function.number_of_hungry_size(6))
        self.assertEqual(2, pizza_function.number_of_classic_size(2))

    def test_level_of_eating_size(self):
        self.assertEqual(16, pizza_function.super_hungry_size(4))
        self.assertEqual(4, pizza_function.hungry_size(2))
        self.assertEqual(1, pizza_function.classic_size(1))

    def test_total_customer_size(self):
        self.assertEqual(21, pizza_function.total_customer_size(4, 2, 1))
        self.assertEqual(65, pizza_function.total_customer_size(10, 10, 5))

    def test_large_size_index(self):
        value = pizza_function.total_customer_size(4, 2, 1)
        self.assertEqual(3, pizza_function.large_size_index(value, 10))
        value2 = pizza_function.total_customer_size(10, 10, 5)
        self.assertEqual(7, pizza_function.large_size_index(value2, 10))
        self.assertEqual(1, pizza_function.large_size_index(10, 10))

    def test_medium_size_index(self):
        value = pizza_function.total_customer_size(4, 2, 1)
        self.assertEqual(4, pizza_function.medium_size_index(value, 6))
        value2 = pizza_function.total_customer_size(10, 10, 5)
        self.assertEqual(11, pizza_function.medium_size_index(value2, 6))
        self.assertEqual(1, pizza_function.medium_size_index(6, 6))

    def test_small_size_index(self):
        value = pizza_function.total_customer_size(4, 2, 1)
        self.assertEqual(6, pizza_function.small_size_index(value, 4))
        value2 = pizza_function.total_customer_size(10, 10, 5)
        self.assertEqual(17, pizza_function.small_size_index(value2, 4))
        self.assertEqual(1, pizza_function.small_size_index(4, 4))

    def test_large_total_slice(self):
        total_customer_size = pizza_function.total_customer_size(4, 2, 1)
        value_box_index = pizza_function.large_size_index(total_customer_size, 10)
        self.assertEqual(30, pizza_function.calculate_large_total_size(value_box_index))

    def test_medium_total_slice(self):
        total_customer_size = pizza_function.total_customer_size(4, 2, 1)
        value_box_index = pizza_function.medium_size_index(total_customer_size, 6)
        self.assertEqual(24, pizza_function.calculate_medium_total_size(value_box_index))

    def test_small_total_slice(self):
        total_customer_size = pizza_function.total_customer_size(4, 2, 1)
        value_box_index = pizza_function.small_size_index(total_customer_size, 4)
        self.assertEqual(24, pizza_function.calculate_small_total_size(value_box_index))

    def test_large_remaining_slice(self):
        total_customer_size = pizza_function.total_customer_size(4, 2, 1)
        value_box_index = pizza_function.large_size_index(total_customer_size, 10)
        result = pizza_function.calculate_large_total_size(value_box_index)

        self.assertEqual(9, pizza_function.calculate_large_remaining_size(total_customer_size, result))

    def test_medium_remaining_slice(self):
        total_customer_size = pizza_function.total_customer_size(4, 2, 1)
        value_box_index = pizza_function.medium_size_index(total_customer_size, 6)
        result = pizza_function.calculate_medium_total_size(value_box_index)
        self.assertEqual(3, pizza_function.calculate_medium_remaining_size(total_customer_size, result))

    def test_small_remaining_slice(self):
        total_customer_size = pizza_function.total_customer_size(4, 2, 1)
        value_box_index = pizza_function.small_size_index(total_customer_size, 4)
        result = pizza_function.calculate_small_total_size(value_box_index)
        self.assertEqual(3, pizza_function.calculate_small_remaining_size(result, total_customer_size))

    def test_large_price(self):
        total_customer_size = pizza_function.total_customer_size(4, 2, 1)
        value_box_index = pizza_function.large_size_index(total_customer_size, 10)
        self.assertEqual(15000, pizza_function.calculate_large_size_price(value_box_index))

    def test_medium_price(self):
        total_customer_size = pizza_function.total_customer_size(4, 2, 1)
        value_box_index = pizza_function.medium_size_index(total_customer_size, 6)
        self.assertEqual(12000, pizza_function.calculate_medium_size_price(value_box_index))

    def test_small_price(self):
        total_customer_size = pizza_function.total_customer_size(4, 2, 1)
        value_box_index = pizza_function.small_size_index(total_customer_size, 4)
        self.assertEqual(7200, pizza_function.calculate_small_size_price(value_box_index))

    def test_large_display(self):
        total_customer_size = pizza_function.total_customer_size(4, 2, 1)
        value_box_index = pizza_function.large_size_index(total_customer_size, 10)
        large = pizza_function.calculate_large_total_size(value_box_index)
        left_over = pizza_function.calculate_large_remaining_size(total_customer_size, large)
        price = pizza_function.calculate_large_size_price(value_box_index)
        expected = f"""
     Number of Slices: {large}
     Number of Boxes: {value_box_index}
     Number of Slices left: {left_over}
     Total cost to spend: {price}
    """
        self.assertEqual(expected,pizza_function.display_large(large,value_box_index,left_over,price))


