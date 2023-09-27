def modify_triangle():
    user_input = int(input("Enter a number between 1 and 19: "))
    if 19 >= user_input > 0 != user_input % 2:
        for row in range(1, user_input):
            for column1 in range(row, user_input - 1):
                print(" ", end=" ")
            for count in range(row):
                print("*", end=" ")

            for count in range(1, row):
                print("*", end=" ")
            print()
        for row in range(1, user_input):
            for column in range(row):
                print(" ", end=" ")

            for column2 in range(row, user_input - 1):
                print("*", end=" ")

            for column1 in range(row, user_input - 2):
                print("*", end=" ")
            print()

    else:
        modify_triangle()






if __name__ == "__main__":
   modify_triangle()