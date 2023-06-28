import unittest
from translator import english_to_french, french_to_english

class Translate(unittest.TestCase):
    def en2fr(self):
        self.assertEqual(english_to_french('Hello'), "Bonjour")
        self.assertNotEqual(english_to_french('Dog'), "Bonjour")

    def fr2en(self):
        self.assertEqual(french_to_english('Bonjour'), "Hello")
        self.assertNotEqual(french_to_english('Chat'), "Dog")


unittest.main()