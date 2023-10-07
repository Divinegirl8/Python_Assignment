def sort_tuple(number):
    result = ()
    for num in range(len(number) // 2):
        result += (number[num],)

    result2 = ()
    for num2 in range(len(number) // 2, len(number)):
        result2 += (number[num2],)

    tuples = ()
    for row in range(len(result2)):
        tuples += (result2[row],) + (result[row],)

    return tuples



