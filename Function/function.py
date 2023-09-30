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
    list = ""

    output = f"{first_number} {second_number} {second_number} "
    list += output
    while count > 0:
        count -= 1
        first_number, second_number = second_number, result
        result = first_number + second_number
        if result < count:
            list_result = f"{result}"
            list += list_result
        list += " "

    return list


def interestRate(rate, year, principal):
    interest_rate = rate / 100

    for count in range(year):
        result = principal * (1 + interest_rate) ** year
    return f"{result:.1f}"


def fizzbuzz(number):
    result = ""
    for count in range(1, number):
        result += "\n"
        if count % 3 == 0 and count % 5 == 0:
            result += "fizzbuzz"
        elif count % 3 == 0:
            result += "fizz"
        elif count % 5 == 0:
            result += "buzz"
        else:
            output = f"{count}"
            result += output

    return result


def even_odd_numbers(*number):
    result = ""
    count_even = 0
    count_odd = 0

    for count in number:
        if count % 2 == 0:
            count_even += 1

        else:
            count_odd += 1

    output = f"The counted even number is {count_even}\n"
    result += output

    output2 = f"The counted odd number is {count_odd}"
    result += output2

    return result


def grade_checker():
    grade = int(input("Enter score(enter -1 to exit): "))
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_f = 0
    grade_counter = 0
    total = 0

    while grade != -1:
        total += grade
        grade_counter += 1
        grade = int(input("Enter score(enter -1 to exit): "))

        match grade / 10:
            case 10:
                count_a += 1
            case 9:
                count_a += 1
            case 8:
                count_b += 1
            case 7:
                count_c += 1
            case 6:
                count_d += 1
            case _:
                count_f += 1

    print(total)
    print(grade_counter)
    print(count_d)


def shape(item):
    aesterik = ""
    for number in item:
        for row in number:
            if row == 0:
                aesterik += " "
            if row == 1:
                aesterik += "*"
        aesterik += "\n"

    return aesterik


def triangle():
    star = ""
    for row in range(1, 8):
        for column1 in range(row, 8 - 1):
            print(" ", end=" ")
        for count in range(row):
            print("*", end=" ")

        for count in range(1, row):
            print("*", end=" ")
        print()


def reversed_triangle():
    for row in range(1, 8):
        for column in range(row):
            print(" ", end=" ")

        for column2 in range(row, 8 - 1):
            print("*", end=" ")

        for column1 in range(row, 7 - 1):
            print("*", end=" ")

        print()


def monetary_interest_calculator(principal_amount, rate_amount, compound, year):
    string_value = ""
    principal = principal_amount
    pennies = principal * 100
    rate = rate_amount / 100
    compounding_frequently = compound

    for years in range(1, year):
        result = pennies * (1 + rate / compounding_frequently) ** (compounding_frequently * years)
        dollar = result // 100
        cents = result % 100

    return f"The compounded interest is ${dollar:.0f}.{cents:.0f} cents"


def max_number(numbers):
    maximum = 0

    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def min_number(numbers):
    minimum = numbers[0]

    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def sum_number(numbers):
    total = 0

    for num in numbers:
        total += num
    return total


def average(numbers):
    return sum_number(numbers) / len(numbers)


if __name__ == "__main__":
    list_score = []

    for integers in range(1, 11):
        score = int(input("Enter scores: "))
        list_score.append(score)

print(sum_number(list_score))
print(average(list_score))
print(max_number(list_score))
print(min_number(list_score))

# if __name__ == "__main__":
#     num = [9, 11, 22, 34, 17, 22, 34, 22, 40]
#     print(mean(num))


# if __name__ == "__main__":
#     print(fizzbuzz(51))

#
# if __name__ == "__main__":
#     picture = [
#         [0, 0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 1, 1, 0, 0],
#         [0, 1, 1, 1, 1, 1, 0],
#         [1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 1, 0, 0, 0]
#     ]
# print(shape(picture))
