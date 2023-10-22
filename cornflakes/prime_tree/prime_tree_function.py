def prime_number_tree(digit):

    if digit < 0:
        number = digit * -1
    else:
        number = digit

    count = 2
    add_list = []
    while count <= number:
        while number % count == 0:
            add_list.append(count)
            number //= count

        count += 1
    return add_list



