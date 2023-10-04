def avg(*number):
    total = 0
    result = 0
    for i in number:
        total += i
        result = total / len(number)
    return round(result, 2)


if __name__ == "__main__":
    print(avg(3,4))