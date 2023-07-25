import unittest
from translator import english_to_french, french_to_english

class TestenglishToFrench(unittest.TestCase):
    def test(self):
        self.assertEqual(english_to_french("Thank you"), "Merci")
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class TestfrenchToEnglish(unittest.TestCase):
    def test(self):
        self.assertEqual(french_to_english("Bonjour"), "Hi")
        self.assertNotEqual(french_to_english("Bonjour"), "Hello")


unittest.main()
