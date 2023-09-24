def commission(rate):
    if rate < 50:
        return rate * 160 + 5000
    elif rate <= 59:
        return rate * 200 + 5000
    elif rate <= 69:
        return rate * 250 + 5000
    else:
        return rate * 500 + 5000


def copies(copy):
    if 0 < copy <= 4:
        return 2000
    elif copy <= 9:
        return 1800
    elif copy <= 29:
        return 1600
    elif copy <= 49:
        return 1500
    elif copy <= 99:
        return 1300
    elif copy <= 199:
        return 1200
    elif copy <= 499:
        return 1100
    else:
        return 1000


def is_even(integer):
    if integer % 2 == 0:
        return True

    return False


def is_prime(integer):
    length_of_numbers = 0
    count = 0

    while count <= integer:
        count += 1
        if integer % count == 0:
            length_of_numbers += 1

    if length_of_numbers == 2:
        return True

    return False


def subtract(first_number, second_number):
    if first_number < second_number:
        return second_number - first_number

    return first_number - second_number


def divide(first_number, second_number):
    if second_number != 0:
        result = first_number / second_number
        approximate = round(result * 100.0) / 100.0
        return approximate

    return 0


def factor_of(number):
    count = 0
    length = 0

    while count <= number:
        count += 1
        if number % count == 0:
            length += 1
    return length


def is_square(number):
    count = 0
    while count < number:
        count += 1
        if count * count == number:
            return True

    return False


def palindrome(number):
    result = number // 10000 % 10
    result2 = number % 10

    if result == result2:
        return True

    return False


def factorial(number):
    count = 1
    result = 1

    while count < number:
        count += 1
        result *= count
    return result


def is_palindrome(number):
    return str(number) == str(number)[::-1]


def sort_number(numbers):
    length_of_list = len(numbers)

    for row in range(length_of_list):
        for column in range(row, length_of_list - 1):
            if numbers[row] > numbers[column + 1]:
                numbers[row], numbers[column + 1] = numbers[column + 1], numbers[row]

    return numbers


def median(numbers):
    sort_int = sort_number(numbers)
    length = len(sort_int)

    list_number = sort_int
    if length % 2 == 0:
        middle_number = list_number[len(list_number) // 2]
        middle_number_two = list_number[len(list_number) // 2 - 1]
        median_number = (middle_number + middle_number_two) / 2
    else:
        median_number = list_number[len(list_number) // 2]

    return median_number


def mean(numbers):
    sort_int = sort_number(numbers)
    sum_number = 0
    length_number = len(sort_int)

    for number in sort_int:
        sum_number += number
        total = sum_number / length_number
    return f"{total:.1f}"


def fibonacci(count):
    first_number = 0
    second_number = 1
    result = first_number + second_number

    while count > 0:
        count -= 1
        first_number, second_number = second_number, result
        result = first_number + second_number
        if result < count:
            return result


def interestRate(rate, year, principal):
    interest_rate = rate / 100

    for count in range(year):
        result = principal * (1 + interest_rate) ** year
    return f"{result:.1f}"


def fizzbuzz(number):
    for count in range(1, number):
        if count % 3 == 0 and count % 5 == 0:
            print("fizzbuzz")
        elif count % 3 == 0:
            print("fizz")
        elif count % 5 == 0:
            print("buzz")
        else:
            print(count)


def even_odd_numbers(number):
    count_even = 0
    count_odd = 0

    for count in number:
        if count % 2 == 0:
            count_even += 1

        else:
            count_odd += 1

    print(f"Even is {count_even}\nOdd is {count_odd}")


def grade_checker():
    grade = 0
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_f = 0
    total = 0
    grade_counter = 0

    while grade != -1:

        grade = int(input("enter grade of student(enter -1 to end): "))
        total += grade
        grade_counter += 1

        match grade / 10:
            case 9, 10:
                count_a += 1
            case 8:
                count_b += 1
            case 7:
                count_c += 1
            case 6:
                count_d += 1
            case _:
                count_f += 1
    if grade != 0:
        print(f"The average grade of student score is {grade / total}")
    else:
        print("no grades entered")

# if __name__ == "__main__":
#     trial = [2, 3, 7, 4]
#     even_odd_numbers(trial)

# if __name__ == "__main__":
#     num = [9, 11, 22, 34, 17, 22, 34, 22, 40]
#     print(mean(num))
