print(f'number  square  cube')

count = 0
result_sqr = 1
result_cube = 1

for number in range(6):
    count +=1
    
    result_sqr = number ** 2
    result_cube = number ** 3


    print(f"{number: < 8}{result_sqr: < 2}{result_cube: > 8}")