import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertIsNone(englishToFrench(None), None) 
    def test2(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') 
    
class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertIsNone(frenchToEnglish(None), None) 
    def test2(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') 
        
unittest.main()
