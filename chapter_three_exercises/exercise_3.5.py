number_one = int(input("First Number: "))
number_two = int(input("Second Number: "))

if number_one == number_two:
    print(f'{number_one} is equals to {number_two}')
else:
    print(f'{number_one} is not equals to {number_two}')

if number_one > number_two:
   print(f'{number_one} is greater than {number_two}')
else:
   print(f'{number_one} is less than {number_two}')

if number_one >= number_two:
   print(f'{number_one} is greater than and equals to {number_two}')
else:
   print(f'{number_one} is less than and equals to {number_two}')
