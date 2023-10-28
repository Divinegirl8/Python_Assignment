# data = {"dike": 33, "ope": 25, "melody": 20, "precious": 27}
#
#
# def student_age():
#     name = input("What is your name")
#     new_name = name.lower()
#     for keys in data.keys():
#         if keys == new_name:
#             return f"Hi {name} you are {data.get(keys)} yrs old"
#     else:
#         user = int(input("Your name is not in the database, What is your age: "))
#         data[name] = user
#         return f"Hi {name} you are {data.get(name)} yrs old"
#
#
# print(student_age())
# print(data)


def student_age(name, data):
    new_name = name.lower()
    for keys in data.keys():
        if keys == new_name:
            return f"Hi {name} you are {data.get(keys)} yrs old"
    else:
        user = int(input("Your name is not in the database, What is your age: "))
        data[name] = user
        return f"Hi {name} you are {data.get(name)} yrs old"


name_value= input("What is your name")
data_value = {"dike": 33, "ope": 25, "melody": 20, "precious": 27}
print(student_age(name_value, data_value))
print(data_value)
