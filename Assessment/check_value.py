def check_element(list_of_numbers, integer):
    for items in list_of_numbers:
        if items == integer:
            return True
    return False


listed = [1, 5, 8, 3]
print(check_element(listed, -1))
