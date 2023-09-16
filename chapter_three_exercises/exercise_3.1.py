#
# passes = 0
# fail = 0
#
# for score in range(10):
#     result = int(input("Enter result (pass = 1, fail = 2): "))
#
#     if result == 1:
#         passes +=1
#     if result == 2:
#         fail +=1
#
#
# print(f'The number of passes is {passes}')
# print(f'The number of failure is {fail}')
#
# if passes > 8:
#     print("Bonus to the instructor")



passes = 0
fail = 0
count = 0

while count < 10:
    result = int(input("Enter result (pass = 1, fail = 2): "))
    if result == 1:
        count+=1
    if result == 2:
        fail +=1
        count += 1

        if result != 1 or result != 2: continue

print(f'The number of failure is {fail}')
