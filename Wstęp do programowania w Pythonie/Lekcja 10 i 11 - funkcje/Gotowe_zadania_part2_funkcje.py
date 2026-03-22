#Zadanie "Dzielenie"
# Napisz funkcję, która otrzyma dwa argumenty pierwszym będzie liczba, którą chcemy
# podzielić bez reszty a drugim argumentem będzie dzielnik. Należy sprawdzić czy
# można dokonać dzielenia a jeśli tak zwrócić informację czy liczba jest podzielna bez reszty czy nie.

def dzielenie(dzielna, dzielnik):
    if dzielnik == 0:
        return "Nie można dzielić przez zero!"
    elif dzielna % dzielnik == 0:
        return f"Liczba {dzielna}  jest podzielna całkowicie przez {dzielnik}."
    else:
        return f"Liczba {dzielna} nie jest podzielna przez {dzielnik}."

print(dzielenie(34, 4))
print(dzielenie(8, 2))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Szablon osoby"
# Napisz funkcję, która przyjmuje następujące argumenty:
# imie (str), wiek (int), wzrost_m (float), 
# a zwraca napis: “Jan, lat 20, 1.75 m wzrostu” - oczywiście argumenty należy podstawić do szablonu. 
# Wzrost ma zawsze pokazywać dwa miejsca po przecinku.

def osoba(imie: str, wiek: int, wzrost_m: float):
    return f"{imie}, lat {wiek}, {wzrost_m:2.2f} wzrostu."

#:N.Mf  N miejsc na liczbe całkowitą . M miejsca na ułamek, f -> float
print(osoba("Alicja", 20, 1.74))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Unikalna lista"
# Napisz funkcję, która jako argument otrzymuje listę elementów, w której mogą
# występować powtórzenia, a zwraca listę unikalnych elementów.
# Dla [1,2,3,3,3,3,4,5] oczekujemy [1, 2, 3, 4, 5]

def unikalna_lista(lista):
    wynik = [] #pusta lista wynikowa
    for elem in lista:
        if not elem in wynik:
            wynik.append(elem)
    
    return wynik

moja_lista = [4, 6, 2, 5, 5, 5, 4, 7, 4]
wynik = unikalna_lista(moja_lista)
print(wynik)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Suma cyfr"
# Napisz funkcję, która otrzymuje liczbę całkowitą, a zwraca sumę jej cyfr. (249 -> 2+4+9=15)

#pamiętamy, że string to lista znaków

def suma_cyfr(liczba: int) -> int:
    liczba_str = str(abs(liczba))
    wynik = 0
    for cyfra in liczba_str:
        wynik += int(cyfra)
    return wynik

a = 26834
print(suma_cyfr(a))
print(suma_cyfr(-7463))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Liczby losowe"
# Napisz funkcję, która zwraca listę losowych liczb. Rozmiar listy zależy od argumentu.
# Dodatkowo: Funkcja powinna otrzymać dwa dodatkowe argumenty: minimalna i
# maksymalna wartość, która może zostać wylosowana.

import random

def losowa_lista(rozmiar: int, mininum: float, maximum: float):
    lista = []
    for i in range(rozmiar):
        lista.append(random.randint(mininum, maximum))
    return lista

print(losowa_lista(10, 0, 20))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Logowanie"
# Napisz funkcję, która zapyta użytkownika o hasło i login. Funkcja ma zwrócić 'True', jeśli
# podano poprawne hasło i login lub 'False' w innym przypadku.

def logowanie(pop_login: str, pop_haslo: str) -> bool:
    login = input("Podaj login: ")
    haslo = input("Podaj hasło: ")

    #wersja 1
    if login == pop_login and haslo == pop_haslo:
        return True
    else:
        return False
    
    #wersja 2
    # return login == pop_login and haslo == pop_haslo

print(logowanie("login", "haslo"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Logowanie z określoną liczba prób"
# Wykorzystaj powyższą funkcję w funkcji, która pozwala na 'n' prób logowań.
# Zwraca 'True' jeśli udało się zalogować lub 'False' jeśli przekroczono liczbę prób.
# Funkcja również musi przyjmować poprawne hasło i login.
# Wprowadzenie niepoprawnej wartości 'n' powinno zostać obsłużone (zapytanie
# jednorazowe dla takich przypadków) - czyli jeśli n < 1 to przyjmujemy, że n=1.

def logowanie_n(n: int, p_login: str, p_haslo: str) -> bool:
    n = max(1, n)

    for i in range(n):
        if logowanie(p_login, p_haslo):
            return True
        print(f"Niepoprawna próba numer {i+1}.")

    print("Logowanie nieudane - przekroczono liczbę prób.")
    return False

print(logowanie_n(3, "login", "haslo"))