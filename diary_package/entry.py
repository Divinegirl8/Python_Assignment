import datetime


class Entry:
    def __init__(self, id_no, title, body):
        self.__id_no = id_no
        self.__title = title
        self.__body = body
        self.__createDate = datetime.datetime.now()

    def get_id(self):
        return self.__id_no

    def edit_entry(self, title, body):
        self.__title = title
        self.__body = body
