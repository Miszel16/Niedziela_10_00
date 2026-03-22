#Zadanie "Logowanie"
#Użytkownik musi podać poprawnie po kolei: PIN, rok_urodzenia, haslo
#Jeżeli jakiekolwiek dane zostaną podane źle, program zaczyna się od nowa
#Dopiero jeśli wszytskie dane zostaną podane poprawnie to pętla się kończy i daje komunikat o zalogowaniu

PIN = "2345"
YEAR_OF_BIRTH = "2005"
PASSWORD = "zaqwsx"

while True:
    input_pin = input("PIN: ")
    if input_pin != PIN:
        print("Odmowa dostępu - zaczynamy od nowa")
        continue

    print("Etap 1 zrealizowano poprawnie (poprawny PIN).")
    input_year = input("Rok urodzenia: ")
    if input_year != YEAR_OF_BIRTH:
        print("Odmowa dostępu - zaczynamy od nowa")
        continue
    
    print("Etap 2 zrealizowano poprawnie (poprawny rok urodzenia).")
    input_password = input("Hasło: ")
    if input_password != PASSWORD:
        print("Odmowa dostępu - zaczynamy od nowa")
        continue

    print("Etap 3 zrealizowano poprawnie (poprawne).")
    print("Zalogowano poprawnie")
    break

print("Tajne treści i inne takie, dostępne po zalogowaniu - czyli tutaj")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#ROZGRZEWKA
# Napisz program, który będzie pytać użytkownika o liczby i zliczać ich sumę, aż do
# wprowadzenia przez użytkownika hasła “koniec”.
# Po wpisaniu tego hasła program, powinien opuścić pętle while i wyświetlić sumę tych ocen.
suma = 0

while True:
    dane = input("Wprowadź liczbę: ")

    if dane == "koniec":
        break
    else:
        dane = int(dane)
        suma += dane

print(f"Uzbierana suma to {suma}")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Zadanie 1 "Kalendarz"
# Napisz program, który wypisze ile lat miałeś/aś w kolejnych latach kalendarzowych od
# Twojego roku urodzenia. Program powinien wykorzystać zmienną wiek oraz pętle for z
# instrukcją range.
wiek_rocznikowo = int(input("Podaj swój wiek rocznikowo: "))

for i in range(wiek_rocznikowo+1):
    rok = 2025 - wiek_rocznikowo + i
    wiek_w_danym_roku = i
    print(f"W roku {rok} miałeś {wiek_w_danym_roku} lat")
    pass
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Zadanie 2 "Tabliczka mnożenia"
# Napisz program, który wypisze w konsoli tabliczkę mnożenia.
# Wykorzystaj funkcję str(liczba).center(liczba_znaków) do wyrównania tekstu.

for a in range(1, 11):
    line = ""
    for b in range(1, 11):
        line += str(a*b).center(4) + "|"
    
    print(line)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Zadanie 3 "Choinka"
# Napisz program, który zapyta użytkownika o wysokość (liczbę linijek), a następnie
# wyświetli choinkę o podanej wysokości. Choinka ma składać się z gwiazdek ‘*’ oraz spacji.

#       *
#      * *
#     * * *
#    * * * *
#   * * * * *

lines = int(input("Podaj wysokośc choinki: "))

for i in range(lines):
    spaces = " " * (lines - i - 1)
    stars = "* " * (i + 1)

    print(spaces + stars)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Zadanie 4 "Prostokąt" - DO DOMU
# Napisz program, który wczyta od użytkownika dwie liczby: wysokość i szerokość, a
# następnie wypisze w konsoli prostokąt składający się z gwiazdek.
# Przygotuj dwie wersje programu: prostokąt pusty w środku i wypełniony. 
# Zapytaj użytkownika, którą wersję chciałby zobaczyć lub wyświetl obie jeden po drugim.

print("Wersje: \n")
print("1 - prostokąt pusty \n")
print("2 - prostokąt pełny \n")

version = int(input("Wybierz wersję: "))

width = int(input("Podaj szerokość: "))
height = int(input("Podaj wysokość: "))

if version == 1:
    for i in range(height):
        if i == 0 or i == height-1:
            print("*" * width)
        else:
            print('*' + ' '*(width-2) + '*')
elif version == 2:
    for i in range(height):
        print("*" * width)
else:
    print("Nie ma takiej opcji")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#Zadanie 5 "Fibonacci"
# Napisz program, który zapyta użytkownika o liczbę dodatnią (sprawdzi jej poprawność)
# a następnie wypisze podaną liczbę elementów ciągu Fibonacciego w konsoli.

# Dodatkowe: Program, który wypisze wszystkie elementy ciągu Fibonacciego, które są
# mniejsze od wprowadzonej liczby.

number = int(input("Podaj liczbę dodatnią: "))

while number < 1:
    number = int(input("Błąd. Wprowadź ponownie: "))

a, b = 0, 1

for i in range(number):
    print(a, end=" ")
    a, b = b, a+b

print("\n")
#Dodatkowe:

a, b = 0, 1
while a < number:
    print(a, end=" ")
    a, b = b, a+b