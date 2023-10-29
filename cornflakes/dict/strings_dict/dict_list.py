def capitalize_word(items: list):
    for word in range(len(items) - 1):
        if items[word][0] == items[word + 1][0]:
            items[word] = items[word].capitalize()
    return items


def list_to_dictionary(item):
    return {item[0]: item for index, item in enumerate(item)}







