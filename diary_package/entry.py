import datetime


class Entry:
    def __init__(self, id_no, title, body):
        self.__id_no = id_no
        self.__title = title
        self.__body = body
        self.__createDate = datetime.datetime.now()

    def get_id(self):
        return self.__id_no

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_body(self, body):
        self.__body = body

    def get_body(self):
        return self.__body

    def set_date_created(self, date_time):
        self.__createDate = date_time

    def __str__(self):
        return f"""
====================================
           MY DIARY        
===================================
Entry Id : {self.__id_no}
Entry Title : {self.__title}
Date Created : {self.__createDate}
===================================
Entry Body:
{self.__body}     
        """

