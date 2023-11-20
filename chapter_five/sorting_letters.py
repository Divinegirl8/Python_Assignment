import random


def generate_letters():
    new_list = []
    for number in range(1, 21):
        list_number = chr(random.randint(ord("a"), ord("f")))
        new_list.append(list_number)
    return new_list


def sort_ascending(items):
    for item in range(len(items)):
        for item2 in range(item, len(items)):
            if items[item] > items[item2]:
                items[item], items[item2] = items[item2], items[item]
    return items


def sort_descending(items):
    for item in range(len(items)):
        for item2 in range(item, len(items)):
            if items[item] < items[item2]:
                items[item], items[item2] = items[item2], items[item]
    return items


ascending_order = sort_ascending(generate_letters())
descending_order = sort_descending(generate_letters())
uniques_values = list(set(generate_letters()))

print(f"{ascending_order}\n{descending_order}\n{sort_ascending(uniques_values)}")
