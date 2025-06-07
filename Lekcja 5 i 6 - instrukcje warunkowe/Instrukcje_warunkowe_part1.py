#PRZYPOMNIENIE INFORMACJI Z OSTATNICH LEKCJI

#1. Funkcje input() i print()

#2. Rodzaje zmiennych i sposób ich zapisu

#3. Rodzaje komentarzy

#4. Zasady nazywania zmiennych:
#   - mogą być małe i duze litery, cyfry oraz '_'
#   - cyfra nie może być pierwszym znakiem
#   - nie mogą być kluczowe słowa w Python np. 'False'
#   - nie używamy polskich znaków

#5. Funkcja len()











# # #KONSTRUKCJA IF
# #(wcięcia w kodzie)
# wynik_warunku = True

# # if wynik_warunku:
# #     print('Warunek jest spełniony, dlatego wypisuję to zdanie.')

# # print('Jestem niezależnym zdaniem od warunku.')

# #Pusta instrukcja
# if wynik_warunku:
#     pass






# #PRZYKŁAD
# wiek = int(input('Podaj swój wiek: '))
# if wiek < 18:
#     print(f'Masz {wiek} lat, czyli jesteś niepełnoletni.')




#Zadanie 1 "Dzielenie"
#Program obliczający wynik z dzielenia, 
# ale z zabezpieczeniem dzielenia przez zero (dzielna/dzielnik)
# dzielna = int(input("Wprowadź dzielną: "))
# dzielnik = int(input("Wprowadź dzielnik: "))

# #Sprawdzamy czy dzielenie jest możliwy (dzielnik jest rożny od zera)
# if dzielnik != 0:
#     wynik = dzielna/dzielnik
#     print(f'{dzielna}/{dzielnik} = {wynik}')

# #Jeśli dzielnik jest równy zero to nie można dzielić
# if dzielnik == 0:
#     print("NIe można dzielić przez 0")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #Sprawdzamy czy dzielenie jest możliwy (dzielnik jest rożny od zera)
# if dzielnik != 0:
#     wynik = dzielna/dzielnik
#     print(f'Wynik z dzielenia: {wynik}')

# #Jeśli dzielnik jest równy zero to nie można dzielić
# if dzielnik == 0:
#     print('Nie wolno dzielić przez 0!')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# #KONSTRUKCJA IF-ELSE
# wynik_warunku = False

# if wynik_warunku:
#     print('Warunek jest spełniony.')
# else:
#     print('Warunek nie jest spełniony.')

# print('Jestem niezależnym zdaniem od warunku.')

# #PRZYKŁAD 
# wiek = int(input('Podaj swój wiek: '))
# if wiek < 18:
#     print(f'Masz {wiek} lat, czyli jesteś niepełnoletni.')
# else:
#     print(f'Masz {wiek} lat, czyli jesteś pełnoletni.')


# # #Zadanie 1 - ale lepiej
# # #Program obliczający wynik z dzielenia, ale z zabezpieczeniem dzielenia pzrze zero (dzielna/dzielnik)
# dzielna = int(input("Wprowadź dzielną: "))
# dzielnik = int(input("Wprowadź dzielnik: "))

# #Sprawdzamy czy dzielenie jest możliwy (dzielnik jest rożny od zera)
# if dzielnik != 0:
#     wynik = dzielna/dzielnik
#     print(f'{dzielna}/{dzielnik} = {wynik}')

# #Jeśli dzielnik jest równy zero to nie można dzielić
# if dzielnik == 0:
#     print("NIe można dzielić przez 0")




#Zadanie 2 "Rollercoaster"
# - minimalny akceptowalny wiek to 12 lat
# - minimalny akceptowalny wzrost to 130 cm
# - maksymalny akceptowalny wzrost to 195 cm
# - jeden zlożony warunek
# - wykorzystujemy operatory relacyjne i logiczne (and)

#pobieramy wzrost i wiek

#wiek musi większy lub równy 12 (>=12) (>11)
#wzrost musi być większy/rowny niż 130 i mniejszy/równy 195


# wiek = int(input("podaj wiek"))
# wzrost = int(input("podaj wzrost"))

# if wiek>=12 and wzrost>=130 and wzrost<=195:
#     print("Zapraszamy")
# else:
#     print("Nie można")     






# #Zadanie dodatkowe "turniej e-sportowy"
# #Czy przechodzimy do następnej fazy turnieju? Wymagania:
# #- liczba wygranych meczów musi wynosić minimum 10 i być większa od przegranych
# #- lub możemy zdobyć łącznie 7 MVP
# #Liczbę meczy wygranych, przegranych oraz liczbę odznaczeń MVP należy pobrać od użytkownika
# #Podpowiedź (lub = or, i = and)






# #KONSTRUKCJA IF-ELIF-ELSE
wynik_warunku_1 = True
wynik_warunku_2 = True

if wynik_warunku_1:
    print('Warunek 1 jest spełniony i koniec.')
elif wynik_warunku_2:
    print('Warunek 2 jest spełniony i koniec.')
else:
    print('Ani warunek 1 ani 2 nie został spełniony.')


# #Zadanie 3 "Znak liczby"
# #Jaka liczba całkowita zostałą wprowadzona?
# #Dodatnia, ujemne, a może 0?

#1. Wprowadzamy liczbe do programu (konwersja)
#2. if (zmienna mniejsza od 0):
#       Twoja liczba jest ujemna
#   elif (czy zmienna równa jest 0):
#       Zmienna wynosi zero
#   else:
#       Zmienna jest dodatnia

# x = int(input("Podaj liczbę: "))

# if x<0 :
#     print("Liczba ujemna.")
# elif x==0 :
#     print("Liczba jest rowna zero.")
# else:
#     print("Liczba jest dodatnia.")



#Zadanie 4 "Prosty Kalkulator"
#Program prosi o podanie liczby a
#Program prosi o wybór działania wyświetlając dostępne opcje +,-,*,/,%
#Program prosi o podanie liczby b
#Obliczenie wyniku dla danej operacji

# from colorama import Fore
# a = int(input("Podaj liczbę a: "))

# print("+ dodawanie")
# print("- odejmowanie")
# print("* mnożenie")
# print("/ dzielenie")
# print("% modulo")

# wybor = input("Podaj znak: ")
# b = int(input("Podaj liczbę b: "))

# if wybor == '+':
#     print(f"{a} + {b} = {a+b}")
# elif wybor == '-':
#     print(f"{a} - {b} = {a-b}")
# elif wybor == '*':
#     print(f"{a} * {b} = {a*b}")
# elif wybor == '/':
#     print(f"{a} / {b} = {a/b}")
# elif wybor == '%':
#     print(f"{a} % {b} = {a%b}")
# else:
#     print(Fore.RED + "Błąd" + Fore.RESET)

# #MATCH CASE
# znak = input("Podaj numer: ")

# match znak:
#     case '1':
#         print('Wybrano numer 1')
#     case '2':
#         print('Wybrano numer 2')
#     case _:
#         print('Niepoprawny numer')

# #Zadanie 4 "Prosty Kalkulator" - ale lepsze



#Zadanie domowe dla chętnych za plusa:
'''
Kierownik parku rozrywki zauważył, że nasz system decyzyjny działa świetnie i
postanowił pójść o krok dalej. Poprosił nas o stworzenie programu, który
automatycznie informuje klientów o cenie biletu w zależności od miesiąca, w
którym chcą odwiedzić atrakcję. Naszym zadaniem jest napisać program, który
informuje użytkownika o koszcie atrakcji turystycznej w zależności od miesiąca.
Program powinien zapytać o numer miesiąca, a następnie powinien wyświetlić

informację według poniższej zasady:
- w styczniu oraz lutym: $150
- w marcu oraz kwietniu: $199
- w maju oraz czerwcu: $249
- w lipcu, sierpniu oraz wrześniu: $299
- w październiku: $249
- w listopadzie oraz grudniu: $199

Ile przypadków należy stworzyć? (13, 12, 7, 6, 5, 4?)
Jak zabezpieczyć się przed niepoprawną nazwą miesiąca?

Rozwiązanie brute-force: 12 przypadków (if-ów/elif-ów) + informacja o złym miesiącu
Rozwiązanie optymalne: 4 przypadki + informacja o złym miesiącu

Wskazówka: Pamiętajmy o konwersji pobranego numeru miesiąca na int.
'''