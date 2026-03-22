# Zadanie "Prostokąt"
# Przygotuj funkcję obliczającą pole prostokąta.
# Funkcja ma przyjmować długości boków, a następnie obliczać i wyświetlać pole figury.

def pole_prostokata(bok_a, bok_b):
    print(f"Pole wynosi {bok_a * bok_b}")
    pass

a = int(input("Podaj bok a: "))
b = int(input("Podaj bok b: "))

pole_prostokata(a, b)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Zadanie "Pole koła"
# Program oblicza pole koła dla podanej listy promieni.
# Wzór na pole koła: pi * promień**2
import math

lista_promieni = [1, 2, 3, 4]

def pole_kola(lista_promieni):
    for promien in lista_promieni:
        print(math.pi * promien ** 2)
    pass

pole_kola(lista_promieni)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Kwadraty Liczb"
# Napisz funkcję, która przyjmuje dwa argumenty: n - liczba powtórzeń, a - liczba startowa.
# Funkcja ma generować kolejne kwadraty liczb, zaczynając od a.
# Ma wyświetlić n kolejnych liczb.

def kwadraty(n, a):
    for i in range(a, a+n):
        print(f"{i} ** 2 = {i**2}")
    pass

kwadraty(5, 4)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Powitanie"
# Napisz funkcję tworzącą powitanie, które wykorzystuje jako argument imie a zwraca
# pełen tekst powitania.

def powitanie(imie):
    return f"Hej, {imie}! :)"

imie = input("Podaj imie: ")
odpowiedz = powitanie(imie)
print(odpowiedz)





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Graniastosłup"
# Napisz funkcję obliczającą objętość graniastosłupa prawidłowego, który w podstawie
# ma sześciokąt (foremny, wiemy to dzięki słowu “prawidłowy”).
from math import sqrt

def pole_szesciokota_foremnego(a):
    return 3 * sqrt(3) * a ** 2 / 2

def obj_gran(bok_pods, wysokosc):
    pole = pole_szesciokota_foremnego(bok_pods)
    return wysokosc * pole

wynik = obj_gran(6, 8)
print(wynik)