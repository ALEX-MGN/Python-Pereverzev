import unittest
from mod3.descrypt import descrypt

array_words = ["абра-кадабра.", "абраа..-кадабра", "абраа..-.кадабра", "абраа..-.кадабра","абрау...-кадабра"]
array_empyty = ["абра........", ".", "1......................."]
class TestDescrypt(unittest.TestCase):
    def test_words(self):
        for word in array_words:
            with self.subTest(word=word):
                self.assertEqual(descrypt(word), "абра-кадабра")

    def test_empyty(self):
        for word in array_empyty:
            with self.subTest(word=word):
                self.assertEqual(descrypt(word), "")

    def test_numbers(self):
        self.assertEqual(descrypt("1..2.3"), "23")

    def test_letters(self):
        self.assertEqual(descrypt("абр......a."), "a")
