user = input("Hello, Kindly Enter Card details to verify: ")

count = 0
new_list = []
while count < len(user):
    result = int(user) // 10 ** count % 10
    count += 1
    new_list.append(result)

single_digit = 0
double_digit = 0
two_digit = 0

# even position

for number in range(1, len(new_list), 2):
    store = new_list[number]
    product = store * 2

    if 10 <= product <= 99:
        two_digit = product

        loop = 0
        while loop < 2:
            out = two_digit // 10 ** loop % 10
            loop += 1
            double_digit += out
    else:
        single_digit += product

sum_both = single_digit + double_digit

odd_sum = 0
# odd position
for digit in range(0, len(new_list), 2):
    odd_sum += new_list[digit]

total = sum_both + odd_sum
last_index = len(user) - 1
second_to_the_last_index = len(user) - 2
get_index = new_list[last_index]
get_index_two = new_list[second_to_the_last_index]

if get_index == 5 and 13 <= len(user) <= 16 and total % 10 == 0:
    card_type = "MasterCard"
    validity_status = "Valid"
elif get_index == 5 and 13 <= len(user) <= 16 and total % 10 != 0:
    card_type = "MasterCard"
    validity_status = "Invalid"

if get_index == 6 and 13 <= len(user) <= 16 and total % 10 == 0:
    card_type = "Discover Card"
    validity_status = "Valid"
elif get_index == 6 and 13 <= len(user) <= 16 and total % 10 != 0:
    card_type = "Discover Card"
    validity_status = "Invalid"

if get_index == 4 and 13 <= len(user) <= 16 and total % 10 == 0:
    card_type = "Visa Card"
    validity_status = "Valid"
elif get_index == 4 and 13 <= len(user) <= 16 and total % 10 != 0:
    card_type = "Visa Card"
    validity_status = "Invalid"


if get_index == 3 and get_index_two == 7 and 13 <= len(user) <= 16 and total % 10 == 0:
    card_type = "America Express Card"
    validity_status = "Valid"
elif get_index == 3 and get_index_two == 7 and 13 <= len(user) <= 16 and total % 10 != 0:
    card_type = "America Express Card"
    validity_status = "Invalid"

if get_index < 3 or get_index > 6:
    card_type = "Invalid Card";
    validity_status = "Invalid"




print(f"""
*****************************************
**Credit Card Type: {card_type}
**Credit Card Number: {user}
**Credit Card Digit Length: {len(user)}
**Credit Card Validity Status: {validity_status}
********************************************    
""")

