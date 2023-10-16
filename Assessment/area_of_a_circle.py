PI = 3.14159
result = f"{PI * (1.1 ** 2):.2f}"

print(result)


# b

def area(radius):
    pi = 3.14159
    area_result = pi * (radius ** 2)
    return round(area_result, 2)


r = 1.1
print(area(r))
