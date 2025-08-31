#    nazwa_pliku         nazwa_klasy
from Uzytkownik_2 import Uzytkownik

user1 = Uzytkownik()
user2 = Uzytkownik()
user3 = Uzytkownik()
user4 = Uzytkownik()

user1.imie = "Alicja"
user1.nazwisko = "Kowalska"
user1.wiek = 32

user2.imie = "Adam"
user2.nazwisko = "Nowak"
user2.wiek = 12

user3.imie = "Piotr"
user3.nazwisko = "Murarz"
user3.wiek = 18

user4.imie = "Patrycja"
user4.nazwisko = "Lach"
user4.wiek = 14

print(user1.imie, user1.nazwisko, user1.wiek)
user1.czy_pelnoletni()

print(user2.imie, user2.nazwisko, user2.wiek)
user2.czy_pelnoletni()

print(user3.imie, user3.nazwisko, user3.wiek)
user3.czy_pelnoletni()

print(user4.imie, user4.nazwisko, user4.wiek)
user4.czy_pelnoletni()



print()
print()



print(user3.imie, user3.nazwisko, user3.wiek)
user3.zmien_wiek(12)
print(user3.imie, user3.nazwisko, user3.wiek)