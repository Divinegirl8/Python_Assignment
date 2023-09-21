number_zero = 0
number_one = 1
number_two = 2
number_three = 3
number_four = 4
number_five = 5


square_zero = number_zero ** 2
square_one = number_one ** 2
square_two = number_two ** 2
square_three = number_three ** 2
square_four = number_four ** 2
square_five = number_five ** 2

cube_zero = number_zero ** 3
cube_one = number_one ** 3
cube_two = number_two ** 3
cube_three = number_three ** 3
cube_four = number_four ** 3
cube_five = number_five ** 3

print(f"""
number\tsquare\tcube
  {number_zero}\t\t  {square_zero}\t\t  {cube_zero}
  {number_one}\t\t  {square_one}\t\t  {cube_one}
  {number_two}\t\t  {square_two}\t\t  {cube_two}
  {number_three}\t\t  {square_three}\t\t  {cube_three}
  {number_four}\t\t  {square_four}\t  {cube_four} 
  {number_five}\t\t  {square_five}\t {cube_five}
""")
