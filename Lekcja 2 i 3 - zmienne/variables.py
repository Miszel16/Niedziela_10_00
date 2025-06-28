
#Komentarze
#komentarz liniowy

'''
komentarz
blokowy
'''

"""
komentarz blokowy 2
"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# #ZMIENNE
# #int - liczby całkowite
# a = 19
# print(a)
# print(type(a))
# print("\n")

# #float - liczby zmiennoprzecinowkowe
# b = 18.6
# print(b)
# print(type(b))
# print("\n")


# #bool - True/False
# c = True
# print(c)
# print(type(c))
# print("\n")


# #string - napisy
# d = "8734t6248adnjads"
# e = 'false - zdanie'
# print(d)
# print(type(d))
# print("\n")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#METODY NAZYWANIA ZMIENNYCH
#- mogą być małe i duze litery, cyfry oraz '_'
#- cyfra nie może być pierwszym znakiem
#- nie mogą być kluczowe słowa w Python np. 'False'
#- nie używamy polskich znaków

# toJestNazwaZmiennej = 0 #Camel Case
# ToJestNazwaZmiennej = 0 #Pascal Case
# to_jest_nazwa_zmiennej = 0 #Snake Case
# TO_JEST_NAZWA_ZMIENNEJ = 0 #UpperCase

# #case-sensitive
# liczba = 3
# Liczba = 4
# LICZBA = 5
# LiczbA = 11
# print(liczba, Liczba, LICZBA, LiczbA)

# a = 6
# a = 8
# a = 11
# print(a)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# #KONWERSJE MIĘDZY TYPAMI ZMIENNYCH
# print("Konwersje między typami\n")
# #NA INT
# #float -> int (zostaje tylko część całkowita)
# a = 3.99
# a = int(a)
# print(a, type(a))


# #bool -> int (1/0)
# b = True
# b = int(b)
# print(b, type(b))


# #string -> int (only if string składa się z samych cyfr i białych znaków (ale nie pomiędzy cyframi))
# c = "132345  "
# c = int(c)
# print(c, type(c))



# #NA FLOAT
# #int -> float 
# d = 7
# d = float(d)
# print(d, type(d))


# #bool -> float 1/0
# e = False
# e = float(e)
# print(e, type(e))


# #string -> float (only if string składa się z samych cyfr i białych znaków (ale nie pomiędzy cyframi) może być kropka)
# f = "123.45   "
# f = float(f)
# print(f, type(f))



# # #NA BOOL
# #int -> bool (0 - fałsz, wszytsko inne - prawda)
# g = 0
# g = bool(g)
# print(g, type(g))

# #float -> bool (0 - fałsz, wszytsko inne - prawda)
# h = 0.00000000000004
# h = bool(h)
# print(h, type(h))

# #string -> bool (pusty string - fałsz, inaczej - prawda)
# i = ""
# i = bool(i)
# print(i, type(i))



# #NA STRING
# #int -> string
# j = 123
# j = str(j)
# print(j, type(j))

# #float -> string
# k = 12.34
# k = str(k)
# print(k, type(k))

# #bool -> string
# l = False
# l = str(l)
# print(l, type(l))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Zadanie 1
# Stworzyć 4 zmienne w których zapiszemy swoje: imię (str), wzrost (w metrach), wiek (w
# latach) i to czy jesteśmy pełnoletni (bool). Następnie wypisujemy je na konsoli (zmienne
# powinny być odpowiednio ponazywane).


# imie = str(input("Podaj mi swoje imie: "))
# print(f"Twoje imie to {imie}, {type(imie)}")

# wzrost = float(input("Podaj mi swoj wzrost: "))
# print(f"Twój wzrost to {wzrost}, {type(wzrost)}")

# wiek = int(input("Podaj wiek: "))
# print(f"Twój wiek to {wiek}, {type(wiek)}")

# pelnoletni = bool(input("Czy jesteś pełnoletni/a? "))
# print(f"{pelnoletni}, {type(pelnoletni)}")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#Kontynuacja 

#WAŻNNE O INPUT() przyjmuje wszystko jako string
# wiek = input('Podaj swój wiek: ')
# print(type(wiek))
# print("\n")
# wiek = int(input('Podaj swój wiek: '))
# print(type(wiek))

# #OPERACJE MATEMATYCZNE
# a = 10
# b = 7
# print(+a) # jednoargumentowy operator pozytywny, wynik 10 (tak naprawdę nic nie robi, istnieje tylko ze względu na kompletność)
# print(a + b) # dwuargumentowy operator dodawania, wynik 17
# print(-a) # jednoargumentowy operator negacji, wynik -10
# print(a - b) # dwuargumentowy operator odejmowania, wynik 3
# print(a * b) # operator mnożenia, wynik 70
# print(a / b) # operator dzielenia, wynik 1.4285714285...
# print(10 / 1) # operator dzielenia ZAWSZE zwraca wartość typu float, nawet gdy liczby są przez siebie podzielne, wynik 10.0
# print(a % b) # operator dzielenia modulo, zwraca resztę z dzielenia pierwszej liczby przez drugą,wynik 3
# print(a // b) # operator dzielenia całkowitoliczbowego, zwraca dzielenie pierwszej liczby przez drugą, zaokrąglonego do w dół do liczby całkowitej, wynik 1
# print(3 ** 2) # operator potęgowania, wynik 9
# print("\n")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# #UPROSZCZENIA
# a = 3
# b = 4
# # jak zwiększyć a o 2?
# a = a + 2
# print(a) # a = 5
# #szybciej
# a += 2

# print(a) # a = 7
# # to samo działa dla innych operatorów
# a -= 5 # tak samo jak a = a - 5

# print(a) # a = 2
# b *= a # tak samo jak b = b * a
# print(b) # b = 8

# b /= 2 # tak samo jak b = b / 2
# print(b) # b = 4.0

# a %= 2 # to samo co a = a % 2
# print(a) # a = 0

# a = 7
# a //= 2 # to samo co a = a // 2
# print(a) # a = 3

# b **= a # to samo co b = b ** a
# print(b) # b = 64.0

# print("\n")
# #True i False jako 1 i 0
# print(True + True) # 2
# print(False + True) # 1
# print(False + False) # 0
# print(3*True) # 3
# print("\n")


# #DZIAŁANIA NA STRINGU
# # dodawanie stringów łączy je w jeden string (do stringa możemy dodawać tylko stringa)
# print('Witaj ' + 'Gigancie!') # 'Witaj Gigancie!'

# # możemy mnożyć string przez int (i na odwrót), tworzy wiele kopii naszego stringa
# print(3 * 'test ') # 'test test test '
# print('test ' * 3) # 'test test test '
# tekst = 'tekst'
# nowy_tekst = 'nowy '
# nowy_tekst += tekst
# print(nowy_tekst) # 'nowy tekst'
# print("\n")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# #FUNKCJE WBUDOWANE
# #1. MATEMATYCZNE
# print(abs(-10)) # wartość bezwzględna z liczby, tutaj 10
# print(max(1, 2, 3, 2, 8, -5)) # największa wartość ze wszystkich podanych jako argumenty, tutaj 8
# print(min(1, 2, 3, 2, 8, -5)) # najmniejsza wartość ze wszystkich podanych jako argumenty, tutaj -5
# print(round(3.5644)) # zaokrąglenie liczby, tutaj 4

# #2. ITEROWALNE
# print(len('Hello World!')) # zwraca długość obiektu - dla stringa jest to ilość znaków, tutaj 12

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Zadanie 1 "Jan Kowalski ma rocznikowo 25 lat"
#Program pobiera od użytkownika imie, nazwisko, rok urodzenia
#Wypisuje wzorcowe zdanie z nazwy zadania i obliczony wiek
#*Używamy fstring'a, czyli print(f)



#Zadanie 2 "Dzielenie"
#Program pobiera od użytkownika 2 liczby (a i b), a następnie podaje wynik w następujący sposób:
#np. dla liczb 48 i 10:
#"48 dzielone przez 10 jest równe 4 i 8 reszty"
#*Używamy fstring'a, czyli print(f)
#*używamy dzielenia całkowitoliczbowego oraz modulo



#Zadanie 3 "Procent"
#Program pobiera liczbę, a następnie procent jaki chcemy z tej liczby uzyskać.
#*Używamy fstring'a, czyli print(f)


#Zadanie 4 "Sześcian"
#Program oblicza objętość oraz pole powierzchni sześcianu dla podanej długości boku
#*Używamy fstring'a, czyli print(f)


#Zadanie 5 "Średnia prędkość"
#Program pobiera od użytkownika odległość (drogę)(m) oraz czas (s) i wylicza średnią prędkość (m/s)
#*Używamy fstring'a, czyli print(f)


#Zadanie 6 "Przelicznik z m/s na km/h"


#Zadanie 7 "Kompy na osobę"
#Program pobiera ilość osób i komputerów, a następnie wylicza ile średnio przypada komputerów na osobę