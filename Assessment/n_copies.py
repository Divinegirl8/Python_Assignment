user_string = input("Enter a value consisting of letters: ")
user_number = int(input("Enter a number: "))

result = f"{user_string * user_number}" if user_number > 0 else f"Invalid, Enter a number greater than 0"
print(result)


#
def n_copies(word, number):
    result_copies = f"{word * number}" if number > 0 else f"Invalid, Enter a number greater than 0"
    return  result_copies


print(n_copies("divine", 3))
