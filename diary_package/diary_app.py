import re
import sys

from diary_package import diaries
from diary_package.diary import Diary
from diary_package.entry import Entry
from diary_package.diaries import Diaries
from diary_package.exceptions.username_exist_error import UserNameExistError

diary = Diaries()


def diary_menu():
    menu = input("""
==================================
         My Diary
==================================
press 1 -> Create Diary
press 2 -> Add Entry
press 3 -> Find Entry
press 4 -> Update Entry 
press 5 -> Delete Entry
press 6 -> Exit 
        """)
    match menu:
        case "1":
            create_diary()
        case "2":
            create_entry()

        case "3":
            find_entry()
        case "4":
            update_entry()
        case "5":
            delete_entry()

        case "6":
            sys.exit(0)
        case _:
            print("Error!!!\nChoose between 1 - 6")
            diary_menu()


def create_diary():
    username = input("Create Username: ")
    if not (re.match(r"^(?=.*[a-z])(?=.*\d)[a-z\d]{5,}$", username) and not username[0].isdigit()):
        print("""Username must consist of letters and digits,
number of characters must be greater than or equal to 5,
username cannot start with a number,
and username should be all lowercase.
            """)
        create_diary()

    password = input("Create your password: ")
    while len(password) < 5:
        print("password is too weak, the numbers of your password should be greater than 5")
        password = input("Create your password: ")

    try:
        diary.add(username, password)
        print(f"Diary created successfully")
        diary_menu()
    except Exception as exception:
        print(exception)
        create_diary()


def unlock_diary():
    print("Kindly provide the correct details to unlock diary")
    username = input("Enter Username: ")
    password = input("Enter password: ")

    try:
        my_diary = diary.find_diary_by_username(username)
        my_diary.unlock_diary(password)
        print("diary unlocked")
        return my_diary
    except Exception as exception:
        print(exception)
        diary_menu()


def create_entry():
    my_diary = unlock_diary()

    title = input("Title: ")
    message = input("Tell your secret: ")

    try:
        entry = my_diary.create_entry(title, message)
        print(f"Entry created.\nEntry id: {entry.get_id()}")
        diary_menu()
    except Exception as exception:
        print(exception)
        diary_menu()


def validate_id():
    entry_id = input("Enter entry id: ")

    while not re.match("\\d+", entry_id):
        print("id must consist of digits only\ntry again: ")
        entry_id = input("Enter entry id: ")
    return entry_id


def find_entry():
    my_diary = unlock_diary()
    convert_id = int(validate_id())

    try:
        entry = my_diary.find_entry_by_id(convert_id)
        print(entry)
        diary_menu()
    except Exception as exception:
        print(exception)
        diary_menu()


def update_entry():
    my_diary = unlock_diary()
    convert_id = int(validate_id())
    title = input("Title: ")
    body = input("Add more spice: ")

    try:
        my_diary.update(convert_id, title, body)
        print("Diary has been updated")
        diary_menu()
    except Exception as exception:
        print(exception)
        diary_menu()


def delete_entry():
    my_diary = unlock_diary()
    convert_id = int(validate_id())

    validate_response = input("Are you sure you want to delete entry?").lower()

    while validate_response != "yes" and validate_response != "no":
        validate_response = input("Invalid input. Please enter 'yes' or 'no': ")

    if validate_response == "yes":
        try:
            my_diary.delete_entry(convert_id)
            print(f"entry {convert_id} deleted successfully")
            diary_menu()
        except Exception as exception:
            print(exception)
            diary_menu()
    else:
        print(f"entry {convert_id} not deleted")
        diary_menu()


class DiaryApp:
    diary_menu()
