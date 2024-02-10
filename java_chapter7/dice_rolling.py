import random


list_container = []
for number in range(1, 7):
    first_die = random.randint(1, 6)
    second_die = random.randint(1, 6)

    list_container.append(first_die + second_die)
print(list_container)


print(__name__)

if __name__ == '__main__':
    print("module")
