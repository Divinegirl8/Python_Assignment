user = input("Enter a letter to check if it is vowel: ")
result = user.lower()
output = ""
if result == "a" or result == "e" or result == "i" or result == "o" or result == "i":
   output = f"{user} is a vowel"

else:
    output = f"{user} is not a vowel"

print(output)