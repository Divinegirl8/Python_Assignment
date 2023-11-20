# def iteration(numbers):
#     print("       ",end=" ")
#     for i , c in enumerate(numbers[0]):
#         print("column",i,end=" ")
#     print()
#     for index, row in enumerate(numbers):
#         print("index", index, end=" ")
#         for index2, column in enumerate(row):
#             print(f"{column:>5}", end="   ")
#
#         print()
#
#
# new_list = [
#     [4, 5, 6],
#     [2, 45, 32]
# ]
#
# iteration(new_list)

def create_list(row, column):
    return [[0 for c in range(column)] for r in range(row)]


def fill_list(values):
    count = 1
    for r in range(len(values)):
        for c in range(len(values[r])):
            values[r][c] = count
            count += 1
    return values


def tabular_format(values):
    result = ""
    result += "          " + " "

    for index , column in enumerate(values[0]):
        result += f"column {index}" + "   "
    result += "\n"

    for index_row, row in enumerate(values):
        result += f"index{index_row}" + " "
        for index_column , column in enumerate(row):
            result += f"{column:>8}" + "   "
        result += "\n"
    return result



