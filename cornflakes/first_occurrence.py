# def replace_occurrence(sample):
#     first_letter = sample[0]
#     words = sample.replace(first_letter, "$")
#     return first_letter + words[1:]


def replace_occurrence(elements, symbol: str):
    value = ""
    for word in elements:
        value += symbol if word == elements[0] else word
    return elements[0] + value[1:]
