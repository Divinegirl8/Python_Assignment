def reverse_tuple(number):
    count = len(number)
    result = ()

    while count > 0:
        count -= 1
        result += number[count],
    return result


