user_string = input("Enter a value consisting of letters: ")
user_number = int(input("Enter a number: "))


check = f"{user_string[0:2] * user_number+user_string[2:len(user_string)]}" if len(user_string) > 2 else f"{user_string * user_number}"
print(check)


