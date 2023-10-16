def con_element(word):
    result = " "
    result += f"'"
    for letters in word:
        result += f"{letters}"
    result += f"'"

    return result


name = ["a", "b", "c", "d", "9"]

print(con_element(name))
