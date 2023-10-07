def rounding(number):
    output = ""
    for element in range(1, 5):
        result = f"{round(number, element)}"
        output += result + "\n"

    return output



