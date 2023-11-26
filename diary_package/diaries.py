from diary_package.diary import Diary


class Diaries:
    def __init__(self):
        self.__diaries = []

    def add(self, username, password):
        diary = Diary(username, password)
        self.__diaries.append(diary)

    def get_diaries_size(self):
        return len(self.__diaries)

    def find_diary_by_username(self, username):
        for index, value in enumerate(self.__diaries):
            if value.get_username() == username:
                return value
        raise RuntimeError("Diary not found")

    def delete_diary(self, username, password):
        for index, value in enumerate(self.__diaries):
            if value.get_username() == username and value.get_password() == password:
                return self.__diaries.remove(value)
        raise RuntimeError("Diary not found")
