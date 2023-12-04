from diary_package.diary import Diary
from diary_package.exceptions.username_exist_error import UserNameExistError
from diary_package.exceptions.diary_not_found_error import DiaryNotFoundError


class Diaries:
    def __init__(self):
        self.__diaries = []

    def add(self, username, password):
        for existing_diary in self.__diaries:
            if existing_diary.get_username() == username:
                raise UserNameExistError("A user with that name exists")

        diary = Diary(username, password)
        self.__diaries.append(diary)

    def get_diaries_size(self):
        return len(self.__diaries)

    def find_diary_by_username(self, username) -> Diary:
        for index, value in enumerate(self.__diaries):
            if value.get_username() == username:
                return value
        raise DiaryNotFoundError("Diary not found")

    def delete_diary(self, username, password):
        for index, value in enumerate(self.__diaries):
            if value.get_username() == username and value.get_password() == password:
                return self.__diaries.remove(value)
        raise DiaryNotFoundError("Diary not found")
