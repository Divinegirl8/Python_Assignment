from unittest import TestCase
from diary_package.diaries import Diaries
from diary_package.diary import Diary


class DiariesTest(TestCase):
    def test_diaries_can_add_diary(self):
        diaries = Diaries()
        diaries.add("username", "password")
        self.assertEqual(1, diaries.get_diaries_size())

    def test_that_my_diaries_can_find_diary_by_user(self):
        diaries = Diaries()
        diaries.add("username", "password")
        diaries.add("username2", "password2")
        self.assertEqual(2, diaries.get_diaries_size())
        diary = diaries.find_diary_by_username("username2")
        self.assertEqual("username2", diary.get_username())

    def test_that_my_diaries_can_raise_exception_if_user_name_not_found(self):
        diaries = Diaries()
        diaries.add("username", "password")
        diaries.add("username2", "password2")
        self.assertEqual(2, diaries.get_diaries_size())

        with self.assertRaises(RuntimeError):
            diaries.find_diary_by_username("user").get_username()

    def test_that_my_diaries_can_delete_diary(self):
        diaries = Diaries()
        diaries.add("username", "password")
        diaries.add("username2", "password2")
        self.assertEqual(2, diaries.get_diaries_size())

        diaries.delete_diary("username2", "password2")
        self.assertEqual(1, diaries.get_diaries_size())

    def test_that_my_diaries_can_throw_an_exception_if_wrong(self):
        diaries = Diaries()
        diaries.add("username", "password")
        diaries.add("username2", "password2")
        self.assertEqual(2, diaries.get_diaries_size())

        with self.assertRaises(RuntimeError):
            diaries.delete_diary("username", "password2")




