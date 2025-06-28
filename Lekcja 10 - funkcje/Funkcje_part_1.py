#https://github.com/Miszel16/Niedziela_10_00
#https://quiz.giganciprogramowania.edu.pl/wdp-python1-q2

#PRZYPOMNIENIE INFORMACJI Z OSTATNICH LEKCJI:

#1. Działanie if-elif-else

#2. Działanie 'and', 'or', 'not'

#3. Działanie pętli while, pętla nieskończona

#4. Funkcja range 

#5. Pętla for:
# for a in range(10):
#     for b in range(3):
#         print((a+1)*(b+1))
#         print("juhuu")

#6. Czym jest lista? Indeksy listy: 
#- Od jakiej wartośći indeksujemy elementy listy?
#- Czy z listy możemy wyciągnąć pod-listę? Więcej elementów za jednym razem?
#- Czy lista może zmieniać swój rozmiar w trakcie działania programu?

# #7. Jakie funkcje używane przy listach znamy i jak działają?
# - len() #ilośc elementówe w liście
# - sum() #sumuje elemnty, lista musi zawierac same liczby
# - .append() #dodaje na koniec listy
# - .clear() #czyści liste
# - .count() # zlicza ilosc wystąpień

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#ROZGRZEWKA
# Napisz program, który pyta użytkownika o liczbę całkowitą, a następnie tworzy listę,
# która zawiera tyle losowych liczb.
# Wygenerowana lista powinna zostać wyświetlona w konsoli.

# import random
# los1 = random.randint(1, 100) #liczby 1 do 100 
# los2 = random.randrange(1, 100)# liczby 1 do 99
# los3 = random.random() #0-1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FUNCKJE - PRZYKŁAD

# # bez funkcji
# print("Osoba Anna Kowalska pracuje w naszej firmie od 3 lat")
# print("Osoba Jan Nowak pracuje w naszej firmie od 5 lat")
# print("Osoba Piotr Zieliński pracuje w naszej firmie od 2 lat")
# print("Osoba Maria Wiśniewska pracuje w naszej firmie od 4 lat")
# print("Osoba Tomasz Lewandowski pracuje w naszej firmie od 6 lat")


# z funkcją
def wyswietl_raport(imie, nazwisko, lata):
    print(f"Osoba {imie} {nazwisko} pracuje w naszej firmie od {lata} lat")

# wyswietl_raport("Anna", "Kowalska", 3)
# wyswietl_raport("Jan", "Nowak", 5)
# wyswietl_raport("Piotr", "Zieliński", 2)
# wyswietl_raport("Maria", "Wiśniewska", 4)
# wyswietl_raport("Tomasz", "Lewandowski", 6)

# ZALETY:
# - zmiana komunikatu wymaga zmiany tylko w jednym miejscu,

# - lepsza czytelność,

# - możemy wykorzystać stworzoną funkcję i skorzystać z niej w dowolnym miejscu
#   w naszym kodzie - nie musimy duplikować kodu.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# WŁASNA PIERWSZA FUNKCJA

#DEKLARACJA
def powitanie():
    print("Cześć, hej!")
    pass

# #WYWOŁANIE
# powitanie()
# powitanie()
# powitanie()

# print("Siemka, jestem program")

# powitanie()

# - 'def' - słowo kluczowe, nazwa funkcji, nawiasy okrągłe, dwukropek
# - we wcięciu kod, który ma się wykonać po wywołaniu funkcji
# - dla czytelności można na końcu dodać "pass"
# - aby uruchomić podaje nazwe funkcji razem z nawiasami
# - wywołać funkcję można dopiero po deklaracji

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ARGUMENTY - przekazywanie informacji do funkcji z zewnątrz; może być kilka; może być zero

# def powitanie(imie):
#     print(f"Cześć, {imie}")
#     pass

# powitanie("Alicja")

# imie = input("Podaj imie: ")
# powitanie(imie)

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# imie = "Alicja"

# def powitanie_powt(imie, powtorzenia):
#     for i in range(powtorzenia):
#         print(f"hej, {imie}")
#     pass

# powitanie_powt(imie, 5)


# powitanie_powt(5, imie)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Prostokąt"
# Przygotuj funkcję obliczającą pole prostokąta.
# Funkcja ma przyjmować długości boków, a następnie obliczać i wyświetlać pole figury.

# def pole_prostokata(a, b):
#     pole = a * b
#     print(pole)

# bok_a = int(input("Podaj bok A: "))
# bok_b = int(input("Podaj bok B: "))

# pole_prostokata(bok_a, bok_b)



# Zadanie "Pole koła"
# Program oblicza pole koła dla podanej listy promieni.
# Wzór na pole koła: pi * promień**2

# import math
# math.pi
# print(math.pi)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# WARTOŚCI DOMYŚLNE ARGUMENTÓW 
# - wartości przypisywane argumentom, jeśli nie podamy arumentów podczas wywoływanai funkcji
# import time
# # Znak '#' oznacza wykonaną część
# # Znak '-' oznacza niewykonaną część

# # [####------] - chcemy otrzymać równo 10 znaków
# def pasek_ladowania(gotowe, wszystko=100):
#     wykonane = round(gotowe * 10 / wszystko) #zaokrąglenie do najbliższej liczby całkowitej
#     niewykonane = 10 - wykonane

#     tekst_wykonane = '#' * wykonane
#     tekst_niewykonane = '-' * niewykonane

#     print(f'\r[{tekst_wykonane}{tekst_niewykonane}] ', end=' ')
#     pass


# for i in range(200):
#     pasek_ladowania(i, 200)
#     time.sleep(0.1)
#     pass


#KONTYNUACJA ZA TYDZIEŃ
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#PRZEKAZYWANIE WARTOŚCI FUNKCJI  - TRZY SPOSOBY

# 1. Wartość domyślna

# 2. Przypisywanie według kolejności

# 3. Przypisywanie po nazwie:
# pasek_ladowania(gotowe = 50, wszystko = 200)
# pasek_ladowania(wszystko = 200, gotowe = 50)

# # Ciekawostka: funkcja print
# for i in range(5):
#     print("Ala ma kota", end = '!!!')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# MOŻLIWE JEST ŁĄCZENIE SPOSOBÓW, ale nazwy moga byc uzyte na końcu

# pasek_ladowania(gotowe = 50, 200) # Źle 
# pasek_ladowania(50, wszytsko = 200) # Dobrze

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Kwadraty Liczb"
# Napisz funkcję, która przyjmuje dwa argumenty: n - liczba powtórzeń, a -
# liczba startowa. Funkcja ma generować kolejne kwadraty liczb, zaczynając od a.
# Ma wyświetlić n kolejnych liczb.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# WARTOŚCI ZWRACANE - instrukcja 'return'

# DWA RODZAJE FUNCKJI - MOŻE ZWRACAĆ LUB NIE

# Funkcja obliczająca pole sześciokąta na podstawie długości boku:
# from math import sqrt

# def pole_szesciokota_foremnego_z_return(a):
#     return 3 * sqrt(3) * a ** 2 / 2

# pole = pole_szesciokota_foremnego_z_return(2)
# print(pole)

# #---------------------------------------

# def pole_szesciokota_foremnego_bez_return(a):
#     print(3 * sqrt(3) * a ** 2 / 2)

# pole_szesciokota_foremnego_bez_return(2)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Powitanie"
# Napisz funkcję tworzącą powitanie, które wykorzystuje jako argument imie a zwraca
# pełen tekst powitania.


# Zadanie "Graniastosłup"
# Napisz funkcję obliczającą objętość graniastosłupa prawidłowego, który w podstawie
# ma sześciokąt (foremny, wiemy to dzięki słowu “prawidłowy”).