def frequency_list(items, value):
    new_list = []
    for element in items:
        count = 0
        for element2 in items:
            if element == element2:
                count += 1

        if count > value:
            new_list.append(element)
    return list({item for item in new_list})





