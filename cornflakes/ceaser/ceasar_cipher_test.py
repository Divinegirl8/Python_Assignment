from unittest import TestCase
from ceaser_cipher import encrypt, decrypt


class Test(TestCase):
    def test_encrypt(self):
        self.assertEqual("ebiil", encrypt("hello"))

    def test_decrypt(self):
        self.assertEqual("hello", decrypt(encrypt("hello")))
