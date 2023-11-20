def rotate(first_value, second_value, third_value):
    return third_value, first_value, second_value


a, b, c = rotate('Doug', 22, 1984)
print(a,b,c)
a, b, c = rotate(a, b, c)
print(a,b,c)
a, b, c = rotate(a, b, c)
print(a, b, c)
