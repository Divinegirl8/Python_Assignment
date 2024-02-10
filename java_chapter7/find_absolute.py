import sys

for args in sys.argv[1:]:
    number = int(args)
    print(f"The absolute value of {number} is {abs(number)}")