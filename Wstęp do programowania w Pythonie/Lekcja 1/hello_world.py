#ROZMOWA
print("Cześć, jestem Python :D")
print("A Ty jak masz na imię?")
imie = input()
print(f"Cześć {imie} miło Cię poznać!")
print("Ja powstałem w 1991 roku, dzięki pracy programisty Guido van Rossuma")

rok_urodzenia = input("A kiedy Ty się urodziłeś? ")
wiek = 2025 - int(rok_urodzenia)
print(f"Wow to masz już {wiek} lat!")

kolor = input("Jaki jest Twój ulubiony kolor? ")
print("Moim ulubionym kolorem jest niebieski i żółty")

miasto = input("A z jakiego miasta pochodzisz? ")
print(f"Było bardzo miło Cię poznać {imie}!")
print(f"Wiem, że masz {wiek} lat, jesteś z {miasto} i lubisz {kolor} kolor")
print("Postaram się zapamiętać do naszego następnego spotkania")

# #LICZBY LOSOWE
# import random
# los = random.randint(1,100) #może być 100
# los2 = random.randrange(1, 100) #nie może być 100
# los3 = random.random() #0-1

# print(los)
# print(los2)
# print(los3)



# #DATA I CZAS
# #KLASA DATETIME - pełna data i godzina
# from datetime import datetime
# today = datetime.today()
# print(f"Teraz: {today}") #data i godzina
# print(f"Dzis: {today.date()}") #data
# print(f"Godzina: {today.time()}") #godzina

# print("\n")

# #KLASA DATE - tylko data
# from datetime import date
# dzis = date.today()
# print(f"Dzisiejsza data: {dzis}") #cała data
# print(f"Rok {dzis.year}")
# print(f"Miesiąc {dzis.month}")
# print(f"Dzień: {dzis.day}")


# #OBLICZANIE WIEKU
# from datetime import datetime

# today = datetime.today() #dzisiejsza data i czas
# my_birthday = datetime(2005, 1, 16) #twoje urodziny (rok, miesiąc, dzień)
# print(f"Urodziny: {my_birthday}") #wypisanie daty urodzin

# passed = today - my_birthday #różnica między dziś a urodzinami

# print(f"Od moich urodzin minęło {passed.days} dni")
# print(f"czyli {passed.days // 366} lat")



# #ZAPISYWANIE INFORMACJI DO PLIKU
# wiadomosc = '''
# Python jest bardzo prosty w kontekście zapisywania danych do pliku
# '''

# with open("msg.txt", 'w', encoding='utf-8') as file:
#     file.write(wiadomosc)

# #'w' - write (zapis do pliku - nadpisz zawartość)
# #'a' - append (dopisz na końcu pliku)
# #encoding='utf-8' - poprawne kodowanie polskich znaków