# NumPy - Numerical Python

# - tablice wielowymiarowe (miacierze) [ndarray = N-Dimensional Array]
# - dużo złożonych funkcji matematycznych
# - operacje na duzych zbiorach danych
# - szybkość - zoptymalizowane operacje (oparte na językach niższego poziomu)
# - !tablice szybsze od list!


# 1. Tablica vs Lista





# 2. Ćwiczenia
import numpy as np


# Zadanie 1
# Stwórz funkcję print_array() w której zaimplementowana zostanie dwuwymiarowa
# tablica oraz wyświetlone zostaną:
# a)Tablica    [[-1,   2,  -3] 
#               [ 4,   5,   6]
#               [ 7,   8,   9]]

# b)Pierwszy element tablicy
# c)Pierwszy zagnieżdżony element tablicy
# d)Typ utworzonego obiektu
# e)Kształt utworzonego obiektu
# Funkcja powinna zwracać utworzoną tablicę.
print("\n\n\n")

def print_array():
    arr = np.array([[-1,   2,  -3], [ 4,   5,   6], [ 7,   8,   9]])
    print(f"Tablica:\n {arr}")
    print(f"Pierwszy element:\n {arr[0]}")
    print(f"Pierwszy zagnieżdżony:\n {arr[0][0]}")
    print(f"Typ: {type(arr)}")
    print(f"Kształt: {arr.shape}")
    return arr

tablica = print_array()







# ------------------------------------------------------------------------------------
# Zadanie 2
# Stwórz funkcję shapeshifter która przyjmuje jako argument utworzoną wcześniej
# tablicę. 
# Funkcja powinna:
# a)Zmienić rozmiar tablicy na 9x1
# b)Zmienić rozmiar tablicy na 1x9
# c)Zmienić rozmiar tablicy na 3x3
# d)Zmienić rozmiar tablicy na -1x9
# e)Zmienić rozmiar tablicy na 3x-1
# f)Podzielić tablicę na 3 nowe tablice
print("\n\n\n")
# '-1' : wstawiamy kiedy nie wiemy ile i komputer liczby sam
# (wiersze, kolumny)
# (ile_'list', ile_elementów_w_'liście')

def shapeshifter(arr):
    print(f"Rozmiar  9 x 1:\n {arr.reshape(9,1)}")
    print(f"Rozmiar  1 x 9:\n {arr.reshape(1,9)}")
    print(f"Rozmiar  3 x 3:\n {arr.reshape(3,3)}")
    print(f"Rozmiar -1 x 9:\n {arr.reshape(-1,9)}")
    print(f"Rozmiar  3 x-1:\n {arr.reshape(3,-1)}")
    new_arr = np.array_split(arr.reshape(-1,3), 3)
    print(f"Nowe:\n {new_arr}")


shapeshifter(tablica)




# ------------------------------------------------------------------------------------
# Zadanie 3
# Utwórz funkcję data_format, która zawierać będzie tablicę zawierającą dane
# różnych typów - wcześniej wspomniane zostało że tablice mogą przechowywać dane
# tylko 1 typu, dlatego należy obsłużyć ewentualny wyjątek. Dodatkowo utwórz tablice
# w których dane rzutowane będą kolejno na stringi, inty i floaty.

# dtype = ...
# | Kategoria | Zalecany `dtype` | Kod literowy | Opis                                      |
# | --------- | ---------------- | ------------ | ----------------------------------------- |
# | Integer   | `int64`          | `'i'`, `'u'` | Liczby całkowite (ze znakiem / bez znaku) |
# | Float     | `float64`        | `'f'`        | Liczby zmiennoprzecinkowe                 |
# | Boolean   | `bool`           | `'?'`        | Wartości logiczne                         |
# | Complex   | `complex128`     | `'c'`        | Liczby zespolone                          |
# | String    | `str` / `'U'`    | `'U'`        | Napisy Unicode                            |
# | Daty      | `datetime64`     | `'M'`        | Daty i czas                               |
# | Czas      | `timedelta64`    | `'m'`        | Różnice czasu                             |
# | Obiekty   | `object`         | `'O'`        | Dowolne obiekty Pythona                   |

# [[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]] - do zmiany formatu
print("\n\n\n")

def data_format():
    try:
        arr = np.array([[1, 2, 3], ["kot", 12, "ola"], [True, 'b', '5']], dtype="U")
        print(arr)
        print(type(arr[0][0]))
    except Exception as e:
        print(e)
    
    arr = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]], dtype="U")
    print(arr)
    print(type(arr[0][0]))

    arr = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]], dtype='int64')
    print(arr)
    print(type(arr[0][0]))

    arr = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]], dtype='f')
    print(arr)
    print(type(arr[0][0]))


data_format()






# ------------------------------------------------------------------------------------
# Zadanie 4
# Utwórz funkcję sorted_ndarray w której utworzona zostanie tablica, a następnie
# wyświetlona, oraz posortowana i ponownie wyświetlona.
print("\n\n\n")

def sorted_ndarray():
    arr = np.array([[3,1,2], [8,1,14], [50,30,64]])
    print(f"Tablica przed sortowaniem:\n {arr}")
    print(f"Tablica posortowana:\n {np.sort(arr)}")

sorted_ndarray()




# ------------------------------------------------------------------------------------
# Zadanie 5
# Stwórz funkcję generate_random_numbers która wygeneruje 10 losowych liczb
# całkowitych od 0 do 100, oraz 10 losowych liczb typu float z zakresu od 0 do 1.
print("\n\n\n")







# ------------------------------------------------------------------------------------
# Zadanie 6
# Stwórz funkcję pick_random_numbers która:
# a) wygeneruje tablicę losowych liczb z zakresu od 0 do 1 o wymiarach 3x5.
# b) wybierze losową liczbę ze zbioru liczb 3,5,7,9
# c) utworzy tablicę o wymiarach 3x5 z losowych elementów ze zbioru liczb 3,5,7,9
# d) wygeneruj 100 losowych liczb, korzystając ze zbioru liczb 3,5,7,9, 
# gdzie szansa na: 3 wynosi 10%, na 5-30 %, na 7-60%, a na 9-0%.
print("\n\n\n")







# ------------------------------------------------------------------------------------
# Zadanie 7
# Stwórz funkcję shuffle_ndarray w której przemieszasz tablicę oraz utworzysz
# permutację tablicy.
print("\n\n\n")







# shuffle - tasuje oryginalną tablicę
# permutacja - tworzy nową pomieszaną tablicę z podanej


# ------------------------------------------------------------------------------------
# Zadanie 8
# Stwórz funkcję array_functions w której:
# a)Wygenerujesz tablicę z 11 wartościami równo rozmieszczonymi na przedziale od 0 do 10
# b)Wyświetlisz tą tablicę
# c)Wyświetlisz sumę elementów tej tablicy
# d)Wyświetlisz najmniejszy element tablicy
# e)Wyświetlisz największy element tablicy
# f) Wyświetlisz średnią wartość tablicy
# g)Wyświetlisz wariancje elementów tablicy (jak daleko, przeciętnie, elementy są od średniej)
# (https://pogotowiestatystyczne.pl/slowniki/wariancja/)
# h)Wyświetlisz odchylenie standardowe elementów tablicy (typowa odległość od średniej)
# (https://pogotowiestatystyczne.pl/slowniki/odchylenie-standardowe/)
print("\n\n\n")







# ------------------------------------------------------------------------------------
# Zadanie 9
# Utwórz funkcję mathematical_functions w której:
# a)Wyświetlisz wartość liczby pi
# b)Wyświetlisz wartość liczby eulera
# c)Wyświetlisz wartość kwadratu liczby eulera
# d)Wyświetlisz wartość sinus pi/2
# e)Wyświetlisz wartość cosinus pi/2
# f)Wyświetlisz wartość tangens pi/2
# g)Wyświetlisz wartość pi/2 zamienioną na stopnie i 360 stopni zamienioną na radiany.
print("\n\n\n")




