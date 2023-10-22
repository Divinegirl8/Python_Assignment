def encrypt(word):
    join_word = ""
    for letters in range(len(word)):
        result = word[letters]
        output = ord(result) - 3

        if 'a' <= result <= 'c':
            output = ord(result) + 23
        elif 'A' <= result <= "C":
            output = ord(result) + 23

        join_word += chr(output)
    return join_word


def decrypt(word):
    join_word = ""
    for letters in range(len(word)):
        result = word[letters]
        output = ord(result) + 3

        if 'x' <= result <= 'z':
            output = ord(result) - 23
        elif 'X' <= result <= "Z":
            output = ord(result) - 23

        join_word += chr(output)
    return join_word



