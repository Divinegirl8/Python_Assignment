def equal_string(first_word, second_word):
    return len(first_word) == len(second_word)


def check_element(first_word: str, second_number: str) -> bool:
    for items in first_word:
        for store in second_number:
            if items == store and len(items) == len(store):
                return True
    return False


print(check_element("love", "evil"))
