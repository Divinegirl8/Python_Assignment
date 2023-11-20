def display_table(values):
    result = "          "
    for index, column in enumerate(values[0]):
        result += f"Column {column}    "
    result += "\n"

    for row in range(len(values)):
        result += f"Row {row}"
        for column in range(len(values[row])):
            result += f"{values[row][column]:>10}" + "  "
        result += "\n"
    return result


