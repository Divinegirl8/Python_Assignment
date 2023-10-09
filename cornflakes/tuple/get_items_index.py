
def item_index(item):
    tuples = ()
    tuples2 = ()

    for index, value in enumerate(item):
        if index == 1:
            tuples += index - 1,
            tuples += value[1],

        if index == 2:
            tuples2 += index - 1,
            tuples2 += value[2],

    return tuples, tuples2



