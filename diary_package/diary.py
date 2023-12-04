import datetime

from diary_package.entry import Entry
from diary_package.exceptions.invalid_password_error import InvalidPasswordError
from diary_package.exceptions.diary_is_locked_error import DiaryIsLockedError
from diary_package.exceptions.entry_id_not_found_error import EntryIdNotFoundError
from diary_package.exceptions.is_empty_error import IsEmptyError


def empty_body_or_title_error(title: str, body: str):
    if (not title) or (not body):
        raise IsEmptyError("Error!!! Input cannot be empty")


class Diary:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__is_locked = True
        self.__entry_size = 0
        self.__entries = []

    def unlock_diary(self, password):
        self.validate_password(password)
        self.__is_locked = False

    def validate_password(self, password):
        if self.__password != password:
            raise InvalidPasswordError("Invalid password")
        return self.__password == password

    def is_locked(self):
        return self.__is_locked

    def lock_diary(self):
        self.__is_locked = True

    def create_entry(self, title, body):
        self.diary_is_locked()
        empty_body_or_title_error(title, body)
        self.__entry_size += 1
        entry = Entry(self.generate_entry_id(), title, body)
        entry.set_date_created(datetime.datetime.now())
        self.__entries.append(entry)
        return entry

    def get_number_of_entry(self):
        return len(self.__entries)

    def generate_entry_id(self):
        return int(f"19{self.__entry_size}")

    def diary_is_locked(self):
        if self.__is_locked:
            raise DiaryIsLockedError("diary is locked")

    def delete_entry(self, id_number):
        self.__entries.remove(self.find_entry_by_id(id_number))

    def find_entry_by_id(self, id_number):
        self.diary_is_locked()
        for value in self.__entries:
            if value.get_id() == id_number:
                return value
        raise EntryIdNotFoundError("Entry id not found")

    def update(self, id_number, title, body):
        self.diary_is_locked()
        empty_body_or_title_error(title, body)
        entry = self.find_entry_by_id(id_number)
        entry.set_title(title)
        entry_body = entry.get_body() + "\n" + body
        entry.set_body(entry_body)

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password
