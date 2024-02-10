def store_values():
    new_list = []
    for value in range(1, 11):
        user_input = int(input())
        while user_input < 10 or user_input > 100:
            print("Error")
            user_input = int(input())
        new_list.append(user_input)
    return eliminate_duplicates(new_list)


def eliminate_duplicates(values):
    container = []

    for value in values:
        if value not in container:
            container.append(value)
    return container



