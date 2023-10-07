def average(number, *args):
    return f"{sum(args, number) / (len(args) + 1)}" if args else f"{number}"



