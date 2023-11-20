def height(number):
    return list(map(lambda x: (x, x * 0.0254), number))


def height_comprehension(numbers):
    return [(number, number * 0.0254) for number in numbers]
