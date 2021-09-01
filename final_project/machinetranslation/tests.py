import unittest
from translator import english_to_french, french_to_english
class TestTranslator(unittest.TestCase):
    def test_en_to_fr(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_fr_to_en(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_enfr_null(self):
        with self.assertRaises(ValueError):
            english_to_french(None)
    
    def test_fren_null(self):
        with self.assertRaises(ValueError):
            french_to_english(None)
if __name__ == '__main__':
    unittest.main()