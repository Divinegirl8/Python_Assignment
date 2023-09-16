# rating = input("Enter an integer rating between 1 and 10")
# The above code will read a runtime error because the statement is housing a string.
# Below is the right way to write the code

rating = int(input("Enter an integer rating between 1 and 10: "))

print(rating)

# or

rating = input("Enter an integer rating between 1 and 10: ")

output = int(rating)

print(output)
