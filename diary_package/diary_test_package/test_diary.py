from unittest import TestCase
from diary_package.diary import Diary


class DiaryTest(TestCase):
    def test_that_my_diary_can_unlock(self):
        diary = Diary("username", "password")
        self.assertTrue(diary.is_locked())
        diary.unlock_diary("password")
        self.assertFalse(diary.is_locked())

    def test_that_my_diary_will_throw_an_exception_for_unlocking_with_wrong_password(self):
        diary = Diary("username", "password")
        self.assertTrue(diary.is_locked())
        with self.assertRaises(RuntimeError):
            diary.unlock_diary("pass")

    def test_that_my_diary_can_lock(self):
        diary = Diary("username", "password")
        diary.unlock_diary("password")
        self.assertFalse(diary.is_locked())

        diary.lock_diary()
        self.assertTrue(diary.is_locked())

    def test_that_my_diary_can_create_entry(self):
        diary = Diary("username", "password")
        diary.unlock_diary("password")
        self.assertFalse(diary.is_locked())

        diary.create_entry("title", "body")
        self.assertEqual(1, diary.get_number_of_entry())
        self.assertEqual(191, diary.generate_entry_id())

        diary.lock_diary()
        self.assertTrue(diary.is_locked())

    def test_that_my_diary_can_delete_entry(self):
        diary = Diary("username", "password")
        diary.unlock_diary("password")
        self.assertFalse(diary.is_locked())

        diary.create_entry("title", "body")
        self.assertEqual(1, diary.get_number_of_entry())

        diary.delete_entry(191)
        self.assertEqual(0, diary.get_number_of_entry())

        diary.lock_diary()
        self.assertTrue(diary.is_locked())

    def test_that_my_diary_can_delete_more_than_one_entry(self):
        diary = Diary("username", "password")
        diary.unlock_diary("password")
        self.assertFalse(diary.is_locked())

        diary.create_entry("title", "body")
        diary.create_entry("title", "body")
        diary.create_entry("title", "body")
        diary.create_entry("title", "body")
        diary.create_entry("title", "body")
        diary.create_entry("title", "body")
        self.assertEqual(6, diary.get_number_of_entry())

        diary.delete_entry(194)
        diary.delete_entry(192)
        diary.delete_entry(191)

        self.assertEqual(3, diary.get_number_of_entry())
        diary.lock_diary()
        self.assertTrue(diary.is_locked())

    def test_that_my_diary_will_raise_error_if_locked_and_trying_to_create_an_entry(self):
        diary = Diary("username", "password")
        diary.unlock_diary("password")
        self.assertFalse(diary.is_locked())

        diary.create_entry("title", "body")
        diary.create_entry("title", "body")

        self.assertEqual(2, diary.get_number_of_entry())

        diary.lock_diary()
        self.assertTrue(diary.is_locked())

        with self.assertRaises(RuntimeError):
            diary.create_entry("title", "body")

    def test_that_my_diary_cannot_delete_an_entry_that_has_been_deleted(self):
        diary = Diary("username", "password")
        diary.unlock_diary("password")
        self.assertFalse(diary.is_locked())

        diary.create_entry("title", "body")
        diary.delete_entry(191)

        with self.assertRaises(RuntimeError):
            diary.delete_entry(191)

    def test_that_my_diary_can_find_an_entry_by_id(self):
        diary = Diary("username", "password")
        diary.unlock_diary("password")
        self.assertFalse(diary.is_locked())
        diary.create_entry("title", "body")

        entry = diary.find_entry_by_id(191)

        self.assertEqual(191, entry.get_id())

    def test_that_my_diary_can_find_more_than_one_entry_by_id(self):
        diary = Diary("username", "password")
        diary.unlock_diary("password")
        self.assertFalse(diary.is_locked())
        diary.create_entry("title", "body")
        diary.create_entry("title", "body")

        entry = diary.find_entry_by_id(191)
        entry2 = diary.find_entry_by_id(192)
        self.assertEqual(191, entry.get_id())
        self.assertEqual(192, entry2.get_id())

    def test_that_my_diary_cannot_find_a_non_existing_id(self):
        diary = Diary("username", "password")
        diary.unlock_diary("password")
        self.assertFalse(diary.is_locked())
        diary.create_entry("title", "body")
        diary.create_entry("title", "body")

        with self.assertRaises(RuntimeError):
            diary.find_entry_by_id(195)

    def test_that_my_diary_will_raise_error_if_locked_and_trying_to_delete_an_entry(self):
        diary = Diary("username", "password")
        diary.unlock_diary("password")
        self.assertFalse(diary.is_locked())

        diary.create_entry("title", "body")
        diary.create_entry("title", "body")

        self.assertEqual(2, diary.get_number_of_entry())

        diary.lock_diary()
        self.assertTrue(diary.is_locked())

        with self.assertRaises(RuntimeError):
            diary.delete_entry(192)

    def test_that_my_diary_can_update_previous_entry(self):
        diary = Diary("username", "password")
        diary.unlock_diary("password")
        self.assertFalse(diary.is_locked())
        diary.create_entry("title", "body")
        diary.create_entry("title", "body")
        self.assertEqual(2, diary.get_number_of_entry())

        diary.update(192, "title", "body")
        self.assertEqual(2, diary.get_number_of_entry())

        diary.lock_diary()

    def test_that_my_diary_can_find_index_of_entry_in_the_list(self):
        diary = Diary("username", "password")
        diary.unlock_diary("password")
        self.assertFalse(diary.is_locked())
        diary.create_entry("title", "body")
        diary.create_entry("title", "body")

        self.assertEqual(1,diary.find_index_of(192))




