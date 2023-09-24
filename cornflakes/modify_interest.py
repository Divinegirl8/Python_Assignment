def interest():
    principal = 1000
    rate = 5 / 100
    rate2 = 6 / 100
    rate3 = 7 / 100
    rate4 = 8 / 100
    rate5 = 9 / 100
    rate6 = 10 / 100
    print("5% Rate  6% Rate  7% Rate  8% Rate  9% Rate  10% Rate")
    for count in range(1,11):
        result = principal * ((1 + rate) ** count)
        result2 = principal * ((1 + rate2) ** count)
        result3 = principal * ((1 + rate3) ** count)
        result4 = principal * ((1 + rate4) ** count)
        result5 = principal * ((1 + rate5) ** count)
        result6 = principal * ((1 + rate6) ** count)
        print(f"{result:.2f}  {result2:.2f}  {result3:.2f}  {result4:.2f}  {result5:.2f}  {result6:.2f} ")


if __name__ == "__main__":
    interest()

