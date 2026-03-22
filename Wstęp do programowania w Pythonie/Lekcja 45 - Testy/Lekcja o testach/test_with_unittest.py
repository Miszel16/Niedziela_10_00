import funkcje
import unittest

# - Klasa powinna dziedziczyc po unittest.TestCase
# - metody muszą nazywać się od 'test' - automatyczne wykrywanie

# class Test_add(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(funkcje.add(2,4), 6)
#         self.assertNotEqual(funkcje.add(1,2), 4)


class Test_palindrom(unittest.TestCase):
    def test_palindrom(self):
        self.assertEqual(funkcje.palindrom("oko"), True)
        self.assertTrue(funkcje.palindrom("ala"))
        self.assertIs(funkcje.palindrom("kamilslimak"), True)
    
    def test_not_palindrom(self):
        # "wiadro", "kamyk", "ola"
        self.assertNotEqual(funkcje.palindrom("wiadro"), True)
        self.assertFalse(funkcje.palindrom("kamyk"))
        self.assertIsNot(funkcje.palindrom("ola"), True)








# uruchamiamy tylko jesli bezpośrednio startujemy ten plik
if __name__ == '__main__':
    # uruchomiene runnera testów (wyszukiwać testy i je uruchamiać)
    unittest.main()
