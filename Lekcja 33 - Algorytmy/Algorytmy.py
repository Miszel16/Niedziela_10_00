# Algorytm 

# Lista wygenerowania do testowania
# - 20 losowych elementów
import random

my_list = []

for i in range(20):
    value = random.randint(1, 100)
    my_list.append(value)

# print(my_list)

# print("\n")
# print("\n")
# print("\n")
# print("\n")



# ------------------------------------------------------------------------
# Słownik - krótko
osoba = {
    "imie": "Jan",
    "nazwisko": "Kowalski",
    "wiek": 30,
    "adres": {
        "ulica": "Kwiatowa",
        "numer": 10,
        "miasto": "Kraków"
    }
}

# słownik: osoba, 4 klucze:
#   - imie (str)
#   - nazwisko (str)
#   - wiek (int)
#   - adres [słownik zagnieżdżony (3 klucze):
#                - ulica (str)
#                - numer (int)
#                - miasto (str)
#                ]
# print(osoba)

# # ----------------- OPERACJE NA SŁOWNIKACH -----------------
# # - dodanie nowej pary klucz - wartość:
# osoba["email"] = "jan.kowalski@example.com"

# print(osoba)

# print("\n")
# # - usunięcie pary klucz-wartość:
# del osoba["wiek"]
# print(osoba)

# print("\n")
# # # - dostęp do wartości na podstawie klucza:
# print(osoba["imie"])

# print("\n")
# # - iteracja przez pary klucz-wartość w słowniku:
# for klucz, wartosc in osoba.items():
#     print(klucz, wartosc)






# ------------------------------------------------------------------------

# 1. SORTOWANIE BĄBELKOWE (bubble sort)
# wizualizacja:
# https://commons.wikimedia.org/wiki/File:Bubble-sort.gif
# https://www.sortvisualizer.com/bubblesort/


def bubble_sort(lista):
    n = len(lista)
    # iterujemy po wszytskich elementach
    for i in range(n):
        # ostatnie i elementów jest juz posortowane
        for j in range(0, n-i-1):
            #     I           II
            if lista[j] > lista[j+1]:
                 lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


print(my_list)
bubble_sort(my_list)
print("Posortowana lista: ")
print(my_list)

# ------------------------------------------------------------------------

# 2. WYSZUKIWANIA

# 2.1 WYSZUKIWANIE LINIOWE
# - jak sprawdzić czy dana wartość znajduje się w naszej liście? 

def linear_search(lista, x):
    n = len(lista)
    for i in range(n): # indexy
        if lista[i] == x:
            return i
    return -1

print("\n")
print(my_list)
print(linear_search(my_list, 7))




# 2.2 WYSZUKIWANIE BINARNE
# - działa na posortowanym zbiorze !!
# - metoda dziel i zwyciężaj
# https://www.mathwarehouse.com/programming/gifs/binary-vs-linear-search.php

#0,1,2    len(lista) = 3
def binary_search(lista, x):
    low = 0
    high = len(lista) - 1
    mid = 0
    while low <= high:
        # wyliczamy środek
        mid = (high + low) // 2

        # czy mid to x
        if lista[mid] > x:
            high = mid - 1

        elif lista[mid] < x:
            low = mid + 1

        else:
            return mid
    return -1
 
print("\n")
print(my_list)
print(binary_search(my_list, 7))


# poszukać jaką złożonosć ma ten algorytm







# ------------------------------------------------------------------------
# ZADANIA DODATKOWE
# ZADANIE 1
# Zadaniem ucznia jest stworzenie programu, który będzie działał jak książka
# telefoniczna. Program powinien mieć następujące funkcjonalności:

#   ● Dodawanie nowego kontaktu - program powinien pytać użytkownika o imię i
#   nazwisko oraz numer telefonu i dodać te dane do listy kontaktów. Lista
#   kontaktów powinna być przechowywana w postaci listy słowników, gdzie
#   każdy słownik reprezentuje jeden kontakt.

#   ● Sortowanie kontaktów za pomocą metody sortowania bąbelkowego -
#   program powinien sortować listę kontaktów alfabetycznie według nazwisk z
#   wykorzystaniem funkcji bubble_sort.

#   ● Wyświetlanie listy kontaktów - program powinien wyświetlić listę kontaktów
#   w formacie: "imię nazwisko - numer telefonu". Kontakty powinny być
#   posortowane alfabetycznie według nazwisk.









# ------------------------------------------------------------------------

# ZADANIE 2
# Zadaniem ucznia jest napisanie programu, który losuje liczbę z zakresu od 1 do
# 100, a następnie komputer będzie zgadywał tę liczbę, a my będziemy mu udzielać
# podpowiedzi w postaci "za mało" lub "za dużo" w zależności od tego, czy
# zgadnięta liczba jest mniejsza czy większa od wylosowanej liczby.

# Komputer będzie korzystał z algorytmu binary search, a program zakończy się, gdy
# komputer zgadnie liczbę.

# * Rekurencja - proces wywoływania funkcji przez samą siebie. 
# 
# W tym konkretnym kodzie, funkcja binary_search można zastosować rekurencje.
# Funkcja sortowania binarnego może być rekurencyjna
# będzie wywoływać samą siebie w dwóch warunkach:
# - kiedy odpowiedź jest "za mało",
# - kiedy odpowiedź jest "za dużo".
# Proces rekurencyjny trwa tak długo, aż odpowiedź jest "tak",
# wtedy funkcja zwraca wartość guess.












# ------------------------------------------------------------------------
# PODSUMOWANIE:
#   ● Wyszukiwanie binarne - podziaŁ uporządkowanej listy na połowy i
#   iteracyjnE przeszukiwaniE jednej z nich w poszukiwaniu szukanej wartości.

#   ● Sortowanie bąbelkowe - porównywaniE sąsiednich elementów listy
#   i zamianie ich kolejności, jeśli są w niewłaściwej kolejności.

# Pytania powtórzeniowe:
#   ● W jaki sposób działa wyszukiwanie binarne?
#   ● Jak działa sortowanie bąbelkowe?