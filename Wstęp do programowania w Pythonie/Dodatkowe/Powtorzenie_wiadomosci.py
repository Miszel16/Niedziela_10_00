# 1. WSTĘP
# ▷ PRINT() - wyświetla dane na ekranie
print("Cześć!")

# ▷ INPUT() - pobiera dane od użytkownika jako tekst (typ str)
input("Jak masz na imię?: ") #po prostu pozwoli coś wpisać w konsoli
imie = input("Jak masz na imię?: ") #wpisana rzezc w konsoli zostanie zapisana do zmiennej

# ▷ Python wykonuje instrukcje od góry do dołu w kolejności ich zapisu

#-------------------------------------------------------------------------------------------------
# 2. ZMIENNE
# ▷ ZMIENNA - "pudełko"/"szufladka" do przechowywania danych
# ▷ TYPY ZMIENNYCH - kategoria, która mówi komputerowi jakiego rodzaju są dane (co moga zawierać)
imie = "Franek"      # napis (string)  [len(napis) - długość napisu]
wiek = 12            # liczba całkowita (int)
wzrost = 1.89        # liczba z przecinkiem (float)
pelnoletni = False   # prawda/fałsz (bool)

# ▷ WYPISANIE TYPU ZMIENNEJ
print(type(imie))

# ▷ ZASADY NAZYWANIA ZMIENNYCH
# - mogą mieć litery, cyfry i _
# - nie mogą zaczynać się od cyfry
# - nie mogą mieć polskich znaków (ą, ę, ł...)
# - Python rozróżnia duże i małe litery (kot ≠ Kot)
# - nie mogą być 'słowem znaczącym', czyli np. "false"

# ▷ KONWERSJA MIĘDZY TYPAMI ZMIENNYCH
a = 123 # typ int
a = str(a) # typ string (teraz zawartośc jest rozpatrywana przez komputer jako napis)

b = 7.0 # typ float
b = int(b) # typ int (wszystko po kropce zniknęło)

c = "True" # typ string (napis)
c = bool(c) # typ bool (wartość oznaczająca 'prawda')

# ▷ MATEMATYKA
# +   dodawanie
# -   odejmowanie
# *   mnożenie
# /   dzielenie zwykłe
# //  dzielenie całkowite 
# %   modulo (reszta z dzielenia)
# **  potęgowanie

# SKRÓT: (a += 2)  to samo co  (a = a + 2) 

# "Ala" + " ma kota" → "Ala ma kota"
# "ha" * 3 → "hahaha"

#-------------------------------------------------------------------------------------------------
# 3. LOGIKA
# ▷ Logika w programowaniu to sposób, w jaki komputer sprawdza, 
# czy coś jest prawdą (True) czy fałszem (False)

# ▷ PORÓWNANIA
# > – większe niż
# < – mniejsze niż
# == – równe
# != – różne
# >= – większe lub równe
# <= – mniejsze lub równe

5 > 3   # True
2 == 4  # False

# ▷ ŁĄCZENIE WARUNKÓW
# and – prawda, jeśli oba warunki są prawdziwe
# or – prawda, jeśli przynajmniej jeden warunek jest prawdziwy
# not – odwraca wartość (prawda ↔ fałsz)

wiek = 12
wysoki = True
print(wiek > 10 and wysoki) # True

# ▷ BOOL czyli zmienna logiczna (True = tak, warunek spełniony; False = nie)
wiek = 12
czy_moze_miec_prawo_jazdy = wiek >= 18 
print(czy_moze_miec_prawo_jazdy) # Nie, czyli False

#-------------------------------------------------------------------------------------------------
# 4. INSTRUKCJE WARUNKOWE
# ▷ Instrukcja warunkowa to pytanie do komputera: „Jeśli coś jest prawdą, zrób to ...""
# if warunek:
#   co zrobić, gdy warunek jest prawdziwy

# ▷ if-else - wybór między dwiema opcjami:
if wiek >= 18:
    print("Jesteś pełnoletni.")
else:
    print("Jesteś niepełnoletni.")


# ▷ if-elif-else - wybór z wielu opcji:
# - pierwszy spełniony warunek powoduje, że reszta warunków nie będzie już sprawdzana
liczba = 20

if liczba > 0:
    print("Dodatnia")
elif liczba < 0:
    print("Ujemna")
else:
    print("Zero")


#-------------------------------------------------------------------------------------------------
# 5. PĘTLA while
# ▷ while() - powtarzania kodu zawartego w pętli dopóki wearunek jest spełniony
# wypisanie 5 razy "Cześć!":
i = 0
while i < 5:
    print("Cześć!")
    i += 1

# ▷ PĘTLA NIESKOŃCZONA - działa dopóki jej nie przerwiesz
# while True:
#     print("Działam bez końca!")


# ▷ BREAK - przerywa pętle
while True:
    odp = input("Napisz coś: ")
    if odp == "koniec":
        break

# ▷ CONTINUE - od razu rozpoczyna pętle od nowa

#-------------------------------------------------------------------------------------------------
# 6. PĘTLA for
# ▷ for - powtarza coś określoną liczbę razy 
# lub iteruje, czyli przechodzi po każdym elemencie listy, napisu czy innej struktury
for i in range(5):
    print("Cześć!")

# ▷ FUNKCJA RANGE() - tworzy ciąg liczb
# range(start, stop, step)
# start - pierwsza liczba w ciągu (jeśli nie jest podana to domyślnie 0)
# stop - pierwsza liczba, która już w ciągu nie będzie
# step - co ile mają się zwiększać liczby (jeśli nie jest podana to domyślnie 1; mogą być ujemne)
for i in range(2, 10, 2):
    print(i)  # 2, 4, 6, 8

# ▷ ITEROWANIE
# przejście po wszystkich literach w napisie
for litera in "kot":
    print(litera) # k o t

#-------------------------------------------------------------------------------------------------
# 7. LISTA
# ▷ struktura danych przechowująca wiele zmiennych - "Szafa z szufladami"
# gdzie każda szufladka (element) ma swój przypisany numer (indeks)
# indeksy zaczynają się od 0
owoce = ["jabłko", "gruszka", "banan"]
liczby = [1, 2, 3, 4.5]
mieszane = [2, "tekst", True, [1, 2]]

# ▷ FUNKCJE DOTYCZĄCE LIST
lista = [1,2,2,2,3,4,"Alicja", 34.98, True]

len(lista) # długość listy
lista.append("haha") # dodanie nowego elementu na koniec
lista.clear() # wyczyszczenie
lista.count(2) # ile razy występuje 2

slowa = ["Ala", "ma", "kota"] # łączy listę słów w jedno zdanie
print(" ".join(slowa))  # Ala ma kota

# ▷ ITEROWANIE
for i in lista:
    print(i) # wyświeli elemnt po elemencie

# ▷ WYPISYWANIE
# w nawiasach znajdują się numery indeksów
liczby = [0, 1, 2, 3, 4]
print(liczby[1:4])  # [1, 2, 3]
print(liczby[:3])   # od początku
print(liczby[2:])   # do końca


#-------------------------------------------------------------------------------------------------
# 8. FUNKCJE
# przepis dla komputera, który wykonuje pewne kroki, kiedy go poprosisz
# Dzięki funkcjom nie musisz pisać w kółko tego samego kodu – możesz go nazwać i wywołać wiele razy

def powitanie():
    print("Cześć!")

powitanie()

# ▷ ARTGUMENTY - przekazywanie informacji do funckji
def powitanie_po_imieniu(imie):
    print(f"Cześć, {imie}!")

# ▷ WARTOŚĆ DOMYŚLNA - zostanie użyta, jeżeli przy wywołaniu nie zostanie podany argument
def pole_prostokata(a=5, b=5):
    print(a * b)

# ▷ ZWRACANIE WYNIKU - return
def dodaj(a, b):
    return a + b

suma = dodaj(2, 3)  # suma = 5

#-------------------------------------------------------------------------------------------------
# 9. BIBLIOTEKI 
# dodatkowa wiedza dla komputera
# dodatkowe funckje i możliwości

# ▷ IMPORT - zaznajomienie komputera z biblioteką

import random # losowe liczby
random.randint(1, 100)   # losuje liczbę od 1 do 100 (włącznie)
random.randrange(1, 100) # losuje liczbę od 1 do 99 (bez 100)
random.random()          # losuje liczbę od 0 do 1


from datetime import datetime # data i czas
teraz = datetime.today()
print(teraz.date())  # sama data
print(teraz.time())  # sama godzina


from datetime import date # data i czas
dzis = date.today()
print(dzis.year)   # rok
print(dzis.month)  # miesiąc
print(dzis.day)    # dzień


import time
time.sleep(1)  # zatrzymanie programu na 1 sekundę


import math # Pierwiastek kwadratowy z liczby
liczba = 25
pierwiastek = math.sqrt(liczba)


import getpass # Zapytaj o hasło (nie będzie widać wpisywanych znaków)
haslo = getpass.getpass("Podaj hasło: ")


# ▷ ZAPISYWANIE DO PLIKU
with open("plik.txt", "w", encoding="utf-8") as f:
    f.write("To jest zapisany tekst")

# open(nazwa_pliku, tryb, encoding)
#   - nazwa_pliku – np. "dane.txt", "paragon.txt".
#   - tryb – określa, co chcemy zrobić z plikiem (zapis, dopisanie itd.).
#       - "w" usuwa starą zawartość i wpisuje nową
#       - "a" zachowuje starą zwartość i dopisuje nowy tekst na końcu
#       - "x" zapisze tylko, jeśli plik jeszcze nie istenieje
#   - encoding="utf-8" – pozwala zapisywać polskie litery.