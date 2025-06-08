#ROZGRZEWKA
# Napisz program, który będzie pytać użytkownika o liczby i zliczać ich sumę, aż do
# wprowadzenia przez użytkownika hasła “koniec”.
# Po wpisaniu tego hasła program, powinien opuścić pętle while i wyświetlić sumę tych ocen.

# suma = 0

# while True:
#     dane = input("Wprowadź liczbę: ")

#     if dane == 'koniec':
#         break
#     else:
#         dane = int(dane)
#         suma = suma + dane

# print(f"Uzbierana suma to {suma}")



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# #PĘTLA FOR - powtarzanie kodu w określoną liczbę razy

# napis = "NAPIS"

# for elem in object:
#     #zrób cos z elem
#     pass

# #elem - zmienna, która przy kazdym obrocie przyjmuje kolejną wartość z object
# #object - to coś, po czym można "przechodzić krok po kroku", np. range(), lista, string


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#FUNKCJA RANGE - tworzy ciąg liczb, np. od 0 do 9 

#WERSJA 1 (STOP)
# range(10) #generuje liczby od 0 do 9
# # 0 1 2 3 4 5 6 7 8 9

# for i in range(10):
#     print(i)


#WERSJA 2 (START, STOP)
# range(2, 10) #generuje liczby od 2 do 9
# # 2 3 4 5 6 7 8 9

# for i in range(2, 10):
#     print(i)


# #WERSJA 3 (START, STOP, STEP - DOMYŚLNIE (+1))
# range(3, 11, 2) #generuje liczby od 3 do 9, co 2 (dodaje 2)
# # 3 5 7 9

# for i in range(3, 11, 2):
#     print(i)


# # #PRZYKŁADY - CO POKAŻE PĘTLA?
# range(4) #0 1 2 3
# range(2, 6) #2 3 4 5
# range(1, 10, 3) #1 4 7
# range(10, 0, -2) # 10 8 6 4 2
# range(0) # nic
# range(7, 7) # nic
# range(3, 15, 4) #3 7 11 
# range(6, 0, -1) # 6 5 4 3 2 1
# range(0, 20, 5) # 0 5 10 15


# for i in range(0, 20, 5):
#     print(i)


#PRZYKŁADY - UZUPEŁNIJ FUNKCJE
#0 1 2 3 4 range(0, 5, 1) / range(5)
#3 4 5 6 7 range(3, 8, 1) / range(3,8)
#1 4 7 10 range(1, 11, 3)
#10 8 6 4 range(10, 3, -2)
#5 10 15 20 range(5, 21, 5)
#9 8 7 6 5 range(9, 4, -1)
#2 2 2 2 range() - nie da się
#0 2 4 6 8 10 range(0, 11, 2)
#7 range(7,8,1)

# for i in range(7,8,1):
#     print(i)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie 1 "Kalendarz"
# Napisz program, który wypisze ile lat miałeś/aś w kolejnych latach kalendarzowych od
# Twojego roku urodzenia. Program powinien wykorzystać zmienną wiek oraz pętle for z
# instrukcją range.

# Rocznikowo mam 20


# W roku 2005 miałaś 0 lat
# W roku 2006 miałaś 1 lat
# ....
# W roku 2025 miałaś 20 lat

# wiek_rocznikowo = int(input("Ile masz rocznikowo lat?: "))


# for i in range(wiek_rocznikowo+1):
#     rok = 2025 - wiek_rocznikowo + i
#     print(f"W roku {rok} miałaś {i} lat")




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#ZAGNIEŻDŻANIE

# for a in range(5): # 0 1 2 3 4
#     print(f"a = {a}")
#     for b in range(20, 70, 10): # 20 30 40 50 60
#         print(f"\tb = {b}")


#Zadanie 2 "Tabliczka mnożenia"
# Napisz program, który wypisze w konsoli tabliczkę mnożenia.
# Wykorzystaj funkcję str(liczba).center(liczba_znaków) do wyrównania tekstu.

# for a in range (1,11,1):
#     line = ""
#     for b in range(1,11,1):
#         line += str(a*b).center(4) + '|'
#     print(line)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#ELSE DLA PĘTLI
# instruk zawarte w else wykonają się tylko wtedy jesli pętla zakończy się naturalnie 
# lub nie wykonan się wcale
# value = int(input("Podaj liczbę: "))

# for a in range(value):
#     print(f"a = {a}")
#     if a > 4:
#         break
# else:
#     print("Pętla for wykonała się bez instrukcji break")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#ZADANIE POWTÓRZENIOWE - PRACA DOMOWA

#Zadanie 3 "Choinka"
# Napisz program, który zapyta użytkownika o wysokość (liczbę linijek), a następnie
# wyświetli choinkę o podanej wysokości. Choinka ma składać się z gwiazdek ‘*’ oraz spacji.

#       *
#      * *
#     * * *
#    * * * *
#   * * * * *

lines = int (input("Podaj wysokośc choinki: "))

for i in range(lines):
    spaces = " " * (lines - i -1)
    stars = "* " * (i+1)

    print(spaces + stars)


#Zadanie 4 "Prostokąt" - DO DOMU
# Napisz program, który wczyta od użytkownika dwie liczby: wysokość i szerokość, a
# następnie wypisze w konsoli prostokąt składający się z gwiazdek.
# Przygotuj dwie wersje programu: prostokąt pusty w środku i wypełniony. 
# Zapytaj użytkownika, którą wersję chciałby zobaczyć lub wyświetl obie jeden po drugim.



#Zadanie 5 "Fibonacci"
# Napisz program, który zapyta użytkownika o liczbę dodatnią (sprawdzi jej poprawność)
# a następnie wypisze podaną liczbę elementów ciągu Fibonacciego w konsoli.

# Dodatkowe: Program, który wypisze wszystkie elementy ciągu Fibonacciego, które są
# mniejsze od wprowadzonej liczby.
