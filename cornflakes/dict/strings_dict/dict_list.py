# def list_to_dictionary(item):
#     return {item[0]: item for index, item in enumerate(item)}
#
#
# def list_to_dictionary2(value):
#     new_dict = {}
#     for index, item in enumerate(value):
#         new_dict.update({item[0]: item})
#         print(new_dict)

# Sample list of strings
my_list = ["apple", "carrot",  "banana", "corange"]

for i in range(len(my_list) - 1):
    if my_list[i][0] == my_list[i + 1][0]:
        my_list[i] = my_list[i].capitalize()

    else:
        my_list[i] = my_list[i]

# Print the resulting list
print(my_list)

# sample_input = ['apple', 'banana', 'coconut', 'corn']
# list_to_dictionary2(sample_input)
