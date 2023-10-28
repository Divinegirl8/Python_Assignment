def count_string(value: str):
    new_dict = {}
    for letters in value: new_dict.update({letters: value.count(letters)})
    return new_dict


def character_frequency(words: str):
    return {word: words.count(word) for word in words}


print(character_frequency("bible"))
