user = input("what is your problem: ")
answer_one = input("Have you had this problem before (yes or no)? ")

answer_yes = answer_one.lower() == "yes"
answer_no = answer_one.lower() == "no"

if answer_yes:
    print('Well, you have it again')

if answer_no:
    print('Well, you have it now')
