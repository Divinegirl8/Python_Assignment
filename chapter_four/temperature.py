def temperature():
    result = ""
    result += "Temperature     Fahrenheit \n"
    for celsius in range(0, 101):
        fahrenheit = f"{celsius:^10} {((9 / 5) * celsius + 32):>12.1f}"
        result += fahrenheit + "\n"
    return result


print(temperature())
