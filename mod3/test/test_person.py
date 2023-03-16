import unittest
from mod3.task4 import person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = person.Person("Aleksandr",2003,"Magnitogorsk")

    def test_get_age(self):
        self.assertEqual(20, self.person.get_age())

    def test_get_name(self):
        self.assertEqual("Aleksandr", self.person.get_name())

    def test_set_name(self):
        self.person.set_name("Ivan")
        self.assertEqual("Ivan", self.person.get_name())

    def test_set_address(self):
        self.person.set_address("Ekaterinburg")
        self.assertEqual("Ekaterinburg", self.person.get_address())

    def test_get_address(self):
        self.assertEqual("Magnitogorsk", self.person.get_address())

    def test_is_homeless(self):
        self.assertEqual(False, self.person.is_homeless())

    def test_is_homeless(self):
        self.person.set_address("")
        self.assertEqual(True, self.person.is_homeless())
