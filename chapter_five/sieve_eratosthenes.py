def prime_numbers(number):
    count = 0
    index = 1
    while index <= number:
        if number % index == 0:
            count += 1
        index += 1
    if count == 2:
        return True
    return number


def create_prime_number_list(numbers):
    new_list = []
    for value in numbers:
        new_list.append(prime_numbers(value))
    return new_list


def set_multiples_of_index_2_as_false(values):
    for index in range(len(values)):
        if values[index] % 2 == 0:
            values[index] = False
    return values


def set_other_index_as_false(values):
    primes = set_multiples_of_index_2_as_false(values)
    for index_value in range(1, len(values)):
        for prime in range(3, len(primes)):
            if values[index_value] % prime == 0:
                values[index_value] = False
                values[0] = False

    return values


def print_out_all_prime_numbers(args):
    return [index + 1 for index, value in enumerate(args) if value]


