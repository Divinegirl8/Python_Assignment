def divisible_by_three(number):
    total = 0
    if number < 0:
        return 0
    for count in range(0, number, 3):
        total += count
    return total
