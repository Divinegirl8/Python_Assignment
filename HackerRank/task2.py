N = int(input("Enter a number: "))

if N % 2 != 0:
    print("Weird")

if 2 <= N <= 5 and N % 2 == 0:
    print("Not Weird")

if 6 <= N <= 20 and N % 2 == 0:
    print("Weird")
if N > 20 and N % 2 == 0:
    print("Not Weird")
