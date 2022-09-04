import unittest

from translator import english_to_french, french_to_english 

class Test(unittest.TestCase): 
    def test_french_to_english(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') #'Bonjour' and 'Hello'
        self.assertEqual(french_to_english('Null'), 'Null') #

class Test(unittest.TestCase): 
    def test_english_to_french(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') #'Hello' and 'Bonjour'
        self.assertEqual(english_to_french('Null'), 'Null') #
        
unittest.main()
