def difference_list(items):
    return maximum_list(items) - minimum_list(items)


def maximum_list(items):
    maximum = 0
    for value in items:
        if maximum < value:
            maximum = value
    return maximum


def minimum_list(items):
    minimum = items[0]
    for value in items:
        if minimum > value:
            minimum = value
    return minimum



