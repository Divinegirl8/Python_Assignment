def summarize_letters(values: str):
    filtered_values = [char.lower() for char in values if char.isalpha()]
    return tuple(sorted(set(
        (filtered_values[index].lower(), filtered_values.count(value)) for index, value in enumerate(filtered_values) if
        filtered_values.count(value) > 1)))


def word_contains_all_alphabet_letters(word, alphabet):
    return set(alphabet).issubset(word.lower())
