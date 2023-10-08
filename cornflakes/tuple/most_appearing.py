def extract_duplicate(digit):
    tuples = ()
    for number in digit:
        count = 0
        for num in range(len(digit)):
            if number == digit[num]:
                count += 1
        if count >= 2:
            tuples += number,

    new_tuple = ()
    for integer in tuples:
        if integer not in new_tuple:
            new_tuple += integer,
    return new_tuple[::-1]


