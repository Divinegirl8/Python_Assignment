import sys


def create_diary():
    pass


def unlock_diary():
    pass


def diary_menu():
    menu = input("""
==================================
           My Diary
==================================
press 1 -> Create Diary
press 2 -> Unlock Diary
press 3 -> Exit 
    """)
    match menu:
        case "1": create_diary()
        case "2": unlock_diary()
        case "3": sys.exit(0)
        case _ : diary_menu()



class Diary:
    diary_menu()
