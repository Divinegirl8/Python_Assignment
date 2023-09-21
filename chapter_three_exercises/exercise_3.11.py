# gallons = float(input("Enter the gallons used (-1 to end): "))
# miles = int(input("Enter the miles driven: "))
# print(f'The miles/gallon for this tank was: {miles / gallons:.6f}')
#
# sum_gallon = 0
# sum_miles = 0
#
# while gallons != -1:
#     sum_gallon += gallons
#     sum_miles += miles
#
#     gallons = float(input("Enter the gallons used (-1 to end): "))
#
#     if gallons == -1:
#         break
#
#     miles = int(input("Enter the miles driven: "))
#     print(f'The miles/gallon for this tank was: {miles / gallons:.6f}')
#
# print(f'The overall average miles/gallon was {sum_miles/sum_gallon:.6f}')


stopper = 0
sum_gallon = 0
sum_miles = 0

while stopper != -1:
    gallons = float(input("Enter the gallons used: "))
    miles = int(input("Enter the miles driven: "))
    print(f'The miles/gallon for this tank was: {miles / gallons:.6f}')
    sum_gallon += gallons
    sum_miles += miles
    stopper = int(input("enter -1 to end or 0 to continue: "))
print(f'The overall average miles/gallon was {sum_miles / sum_gallon:.6f}')

