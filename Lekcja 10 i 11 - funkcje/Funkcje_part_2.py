#https://github.com/Miszel16/Niedziela_10_00


#Zadanie "Dzielenie"
# Napisz funkcję, która otrzyma dwa argumenty pierwszym będzie liczba, którą chcemy
# podzielić bez reszty a drugim argumentem będzie dzielnik. Należy sprawdzić czy
# można dokonać dzielenia a jeśli tak zwrócić informację czy liczba jest podzielna bez reszty czy nie.

def dzielenie(dzielna, dzielnik):
    if dzielnik == 0:
        return "Nie można dzielić przez 0."
    elif dzielna % dzielnik == 0:
        return f"Liczba {dzielna} jest podzielna przez {dzielnik}."
    else:
        return f"Liczba {dzielna} nie jest podzielna przez {dzielnik}."

# dzielna =input()
# dzielnik = input()

# wynik = dzielenie(int(dzielna), int(dzielnik))
# print(wynik)

# print(dzielenie(9, 3))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#TYPE HINTING

def prostokat(a: float, b: float) -> float:
    obwod = 2*a + 2*b
    return obwod

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Szablon osoby"
# Napisz funkcję, która przyjmuje następujące argumenty:
# imie (str), wiek (int), wzrost_m (float), 
# a zwraca napis: “Jan, lat 20, 1.75 m wzrostu” - oczywiście argumenty należy podstawić do szablonu. 
# Wzrost ma zawsze pokazywać dwa miejsca po przecinku.

def osoba(imie: str, wiek: int, wzrost_m: float) -> str:
    return f"{imie}, lat {wiek}, {wzrost_m} m wzrostu."

# imie = input("Podja imie: ")
# wiek = int(input("Podaj wiek: "))
# wzrost_m = float(input("Podaj wzrost: "))

# wynik = osoba(imie, wiek, wzrost_m)

# print(wynik)

# print(osoba("Alicja", 20, 1.74))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Unikalna lista"
# Napisz funkcję, która jako argument otrzymuje listę elementów, w której mogą
# występować powtórzenia, a zwraca listę unikalnych elementów.
# elem in lista
# Dla [1,2,3,3,3,3,4,5] oczekujemy [1, 2, 3, 4, 5]

def unikalna_lista(lista):
    wynik = [] #pusta lista wynikowa
    for elem in lista: #elem = 2
        if not elem in wynik: # 2, 3, 5
            wynik.append(elem)
    return wynik

# lista = [2,3,5,5,3,2]

# print(unikalna_lista(lista))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Suma cyfr"
# Napisz funkcję, która otrzymuje liczbę całkowitą, a zwraca sumę jej cyfr.
# Dla liczby 249 otrzymujemy 2+4+9 czyli 15

#string to lista znaków

[2, 4, 9]

def suma_cyfr(liczba: int) -> int:
    liczba_str = str(abs(liczba)) #abs() - wartość bezwzględna (zawsze na plus)\
    suma = 0
    for cyfra in liczba_str:
        suma += int(cyfra)
    return suma

# a = 195639
# print(suma_cyfr(a))
# print(suma_cyfr(-12))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Liczby losowe"
# Napisz funkcję, która zwraca listę losowych liczb. Rozmiar listy zależy od argumentu.
# Dodatkowo: Funkcja powinna otrzymać dwa dodatkowe argumenty: minimalna i
# maksymalna wartość, która może zostać wylosowana.
import random

def losowa_lista(rozmiar: int, minimum: int, maksimum: int):
    lista = []
    for i in range(rozmiar):
        liczba = random.randint(minimum, maksimum)
        lista.append(liczba)
    return lista

# print(losowa_lista(10, 0, 10))


#a = random.randint(0, 10)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Logowanie"
# Napisz funkcję, która zapyta użytkownika o hasło i login. Funkcja ma zwrócić 'True', jeśli
# podano poprawne hasło i login lub 'False' w innym przypadku.


# Zadanie "Logowanie z określoną liczba prób"
# Wykorzystaj powyższą funkcję w funkcji, która pozwala na 'n' prób logowań.
# Zwraca 'True' jeśli udało się zalogować lub 'False' jeśli przekroczono liczbę prób.
# Funkcja również musi przyjmować poprawne hasło i login.
# Wprowadzenie niepoprawnej wartości 'n' powinno zostać obsłużone (zapytanie
# jednorazowe dla takich przypadków) - czyli jeśli n < 1 to przyjmujemy, że n=1.