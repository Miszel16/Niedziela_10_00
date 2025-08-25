# Zadania powtórzeniowe


# Zadanie 1 – FizzBuzz
# Celem zadania FizzBuz jest napisanie programu, który wypisze na ekranie liczby 1 do 100,
# - zamiast liczb podzielnych przez 3 ma napisać Fizz,
# - zamiast podzielnych przez 5 Buzz,
# - zamiast podzielnych przez 3 i 5 FizzBuzz.

# 1 od 100
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# Zadanie 2 - wzór
# Napisz program, który wyświetli na ekranie ten wzór, zależnie od liczby jaką podamy:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6

# liczba = int(input("Podaj liczbę: "))

# for i in range(1, liczba+1):
#     print((str(i) + " ") * i)

# def wzor(liczba: int) -> None:
#     for i in range(1, liczba+1):
#         print((str(i) + " ") * i)


# wzor(liczba)



# Zadanie 3 – min i max
# Należy napisać program, który z listy pokaże nam najmniejszą i największą liczbę

# lista = [1, 3, 7, 11, 2, -6, 0]

# najmniejsza = lista[0]
# najwieksza = lista[0]

# for i in lista:
#     if i > najwieksza:
#         najwieksza = i
#     if i < najmniejsza:
#         najmniejsza = i

# print(f"Największa wartość: {najwieksza}")
# print(f"Najmnijesza wartość: {najmniejsza}")




# Zadanie 4 – zliczanie liter
# Program ma zliczyć ile danych liter znajduje się w zdaniu
# Przykładowe wyświetlanie:
# "ABC przykladowy tekst na potrzeby naszego programu"

# Slowa: 7, Litery: 44, ilosc liter: {'a': 5, 'b': 2, 'c': 1, 'p': 3, 'r': 4, 'z': 3, 'y': 3,
#  'k': 2, 'l': 1, 'd': 1, 'o': 4, 'w': 1, 't': 3, 'e': 3, 's': 2, 'n': 2, 'g': 2, 'm': 1, 'u': 1}

# tekst = "ABC przykladowy tekst na potrzeby naszego programu"

# slowa = 0
# litery = 0
# slownik = {}
# ##         0,1,2,3,4
# # lista = [1,2,3,4,5]

# # slownik_2 = {"a": 0, "b": 5}

# for slowo in tekst.split(" "):
#     slowa += 1
#     litery += len(slowo)
#     for znak in slowo.lower():
#         if znak in slownik:
#             slownik[znak] += 1
#         else:
#             slownik[znak] = 1

# print(f"Słowa: {slowa}")
# print(f"Litery: {litery}")
# print(slownik)


# Zadanie 5 – orzeł i reszka
# Gracz będzie zgadywać co wypadnie następne, i punkty będzie dostawać albo gracz, albo komputer.

import time
import random

gracz = 0
komputer = 0

print("o - orzeł")
print("r - reszka")
print("0 - zakończenie gry")

while True:
    x = input("Co obstawiasz?: ").lower()

    if x == '0': break
    elif x == 'o': x = "orzeł"
    elif x == 'r': x = "reszka"
    else:
        print("Proszę dokonac prawidłowego wyboru!")
        print("o - orzeł")
        print("r - reszka")
        print("0 - zakończenie gry")
        time.sleep(1)
        continue

    w_komputer = random.choice(["orzeł", "reszka"])
    print(f"Komputer obstwaia: {w_komputer}")
    
    for i in range(3):
        print(3-i)
        time.sleep(1)

    moneta = random.choice(["orzeł", "reszka"])
    print(f"Wypadło: {moneta}")

    if x == moneta:
        gracz += 1
    if w_komputer == moneta:
        komputer += 1
    
    print("Obecny wynik:")
    print(f"Gracz: {gracz}")
    print(f"Komputer: {komputer}")
