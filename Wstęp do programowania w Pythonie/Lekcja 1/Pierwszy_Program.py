"""
imie = input("Podaj mi swoje imie: ")
print(f"Cześć {imie}")

wiek = input("Ile masz lat? ")
print(f"O czyli masz {wiek} lat! Ja powstałem w 1991 roku.")

miasto = input("Z jakiego miasta jesteś? ")
print(f"{miasto} brzmi ciekawie")

gra = input("Podaj mi swoją ulubioną grę: ")
print(f"{gra}, znam bardzo fajna")
"""

# #LICZBY LOSOWE
# import random

# los1 = random.randint(1, 100) #liczby 1 do 100 
# los2 = random.randrange(1, 100)# liczby 1 do 99
# los3 = random.random() #0-1

# print(los1)
# print(los2)
# print(los3)

#DATA I CZAS
#KLASA DATETIME - pełna data i godzina
from datetime import datetime
today = datetime.today()

print(f"Teraz: {today}") #data i godzina
print(f"Data: {today.date()}") #data
print(f"Godzina: {today.time()}") #godzina


from datetime import date
dzis = date.today()
print(f"Teraz: {dzis}") #data
print(f"Rok: {dzis.year}") #rok
print(f"Miesiąc: {dzis.month}") #miesiąc
print(f"Dzień: {dzis.day}") #dzień