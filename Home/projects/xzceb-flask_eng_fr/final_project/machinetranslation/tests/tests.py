from translator import french_toenglish,english_tofrench
import unittest

class TestEnglishtofrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_tofrench(""),"")
        self.assertEqual(english_tofrench("Hello"),"Bonjour")
        
class TestFrenchtoenglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_toenglish(""),"")
        self.assertEqual(french_toenglish("Bonjour"),"Hello")
unittest.main()
        