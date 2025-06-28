# https://github.com/Miszel16/Niedziela_11_45

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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # #KONSTRUKCJA IF
#(wcięcia w kodzie)
# wynik_warunku = True


# if wynik_warunku:
#     print('Warunek jest spełniony, dlatego wypisuję to zdanie.')
#     print()

# print('Jestem niezależnym zdaniem od warunku.')

#Pusta instrukcja
# if wynik_warunku:
#     pass

# print("jsdfh")



# #PRZYKŁAD
# wiek = int(input('Podaj swój wiek: '))

# if wiek < 18:
#     print(f'Masz {wiek} lat, czyli jesteś niepełnoletni.')



#Zadanie 1 "Dzielenie"
#Program obliczający wynik z dzielenia, 
# ale z zabezpieczeniem dzielenia przez zero (dzielna/dzielnik)

# dzielna = int(input("Podaj dzielną: "))
# dzielnik = int(input("Podaj dzielnik: "))

# if dzielnik != 0:
#     print(dzielna/dzielnik)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


# #Zadanie 1 - ale lepiej
# #Program obliczający wynik z dzielenia, ale z zabezpieczeniem dzielenia pzrze zero (dzielna/dzielnik)
# dzielna = int(input("Podaj dzielną: "))
# dzielnik = int(input("Podaj dzielnik: "))

# if dzielnik != 0:
#     print(dzielna/dzielnik)
# else:
#     print("NIe mozna dzielić przez 0.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Zadanie 2 "Rollercoaster"
# - minimalny akceptowalny wiek to 12 lat #mamy
# - minimalny akceptowalny wzrost to 130 cm
# - maksymalny akceptowalny wzrost to 195 cm
# - jeden zlożony warunek
# - wykorzystujemy operatory relacyjne i logiczne (and)

# wiek = int(input("Podaj swój wiek: "))
# wzrost = int(input("Podaj wzrost: "))

# if wiek >= 12 and 130 <= wzrost <= 195:
#     print("Możesz zjechać na rollercoasterze!")
# else:
#     print("Niestety nie spełniasz warunków bezpieczeństwa")
   



# #Zadanie dodatkowe "turniej e-sportowy"
# #Czy przechodzimy do następnej fazy turnieju? Wymagania:
# #- liczba wygranych meczów musi wynosić minimum 10 i być większa od przegranych
# #- lub możemy zdobyć łącznie 7 MVP
# #Liczbę meczy wygranych, przegranych oraz liczbę odznaczeń MVP należy pobrać od użytkownika
# #Podpowiedź (lub = or, i = and)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# #KONSTRUKCJA IF-ELIF-ELSE
# wynik_warunku_1 = True
# wynik_warunku_2 = True

# if wynik_warunku_1:
#     print('Warunek 1 jest spełniony i koniec.')
# elif wynik_warunku_2:
#     print('Warunek 2 jest spełniony i koniec.')
# elif wynik_warunku_2:
#     print('Warunek 2 jest spełniony i koniec.')
# elif wynik_warunku_2:
#     print('Warunek 2 jest spełniony i koniec.')
# else:
#     print('Ani warunek 1 ani 2 nie został spełniony.')


# #Zadanie 3 "Znak liczby"
#Jaka liczba całkowita została wprowadzona?
#Dodatnia, ujemne, a może 0?

# liczba = int(input("Podaj liczbę: "))

# if liczba == 0:
#     print("Twoja liczb wynosi zero.")
# elif liczba > 0:
#     print("Twoj liczba jest dodatnia.")
# else:
#     print("Twoja liczba jest ujemna.")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie dodatkowe "Cena atrakcji"
# Naszym zadaniem jest napisać program, który
# informuje użytkownika o koszcie atrakcji turystycznej w zależności od miesiąca.
# Program powinien zapytać o numer miesiąca, a następnie powinien wyświetlić

# informację według poniższej zasady:
# w styczniu oraz lutym: $150
# w marcu i kwietniu: $199
# w maju oraz czerwcu: $249
# w lipcu, sierpniu oraz wrześniu: $299
# w październiku: $249
# w listopadzie oraz grudniu: $199




# Zadanie 4 "Prosty Kalkulator"
# Program prosi o podanie liczby a
# Program prosi o wybór działania wyświetlając dostępne opcje +,-,*,/,%
# Program prosi o podanie liczby b
# Obliczenie wyniku dla danej operacji

a = float(input("Podaj pierwszą liczbę: "))

print("dodawania - '+'")
print("mnożenie - '*'")
print("dzielenie - '/'")
print("odejmowanie - '-'")
print("potęgowanie - '**'")

znak = input("Wybierz działanie: ")

b = float(input("Podaj drugą liczbę: "))


if znak == '+':
    print(f"{a} {znak} {b} = {a+b}")
elif znak == '*':
    print(f"{a} {znak} {b} = {a*b}")
elif znak == '/':
    print(f"{a} {znak} {b} = {a/b}")
elif znak == '-':
    print(f"{a} {znak} {b} = {a-b}")
elif znak == '**':
    print(f"{a} {znak} {b} = {a**b}")
else:
    print("Podano niepoprawny znak.")
    pass


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# MATCH CASE
znak = input("Podaj numer: ")

match znak:
    case '+':
        print('Wybrano numer 1')
    case '-':
        print('Wybrano numer 2')
    case _:
        print('Niepoprawny numer')

# Zadanie 4 "Prosty Kalkulator" - ale lepsze

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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