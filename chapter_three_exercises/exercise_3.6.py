user = input("what is your problem: ")
answer_one = input("Have you had this problem before (yes or no)? ")

if answer_one == "yes" or answer_one == "YES" or answer_one == "Yes":
    print('Well, you have it again')

if answer_one == "no" or answer_one == "NO" or answer_one == "No":
    print('Well, you have it now')