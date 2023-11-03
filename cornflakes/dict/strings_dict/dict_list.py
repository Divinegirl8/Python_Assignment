# def capitalize_word(items: list):
#     for word in range(len(items) - 1):
#         if items[word][0] == items[word + 1][0]:
#             items[word] = items[word].capitalize()
#     return items


def capitalize_word(items: list):
    for word in range(len(items) - 1):
        if items[word][0] == items[word + 1][0]:
            items[word] = items[word].capitalize()
    return items


# def list_to_dictionary(item):
#     return {item[0]: item for index, item in enumerate(item)}


def capital(items: list):
    list_v = []
    r = ""
    for index, item in enumerate(items):
        result = items[index][0]
        if result in list_v:
            result = items[index][0].upper()
        list_v.append(result)
        list_v.append(item)

    return list_v


def list_to_dictionary(items):
    dict_value = {}

    for index, item in enumerate(items):
        result = items[index][0]

        if result in dict_value:
            result = items[index][0].upper()
        dict_value.update({result: item})

    return dict_value


v = ["apple", "corn", "axe","cucumber"]

print(list_to_dictionary(v))
