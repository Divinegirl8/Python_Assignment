def sum_series(number):
   count = 0
   total = 0

   while count < number:
    total += count
    count += 1
    print(f"{count} {total}")

if __name__ == "__main__":
    sum_series(100)
