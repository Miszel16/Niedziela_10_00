#Czym jest pętla? Co nam daje używanie pętli?



# PĘTLA WHILE
# wykonuje się dopóki warunke jest spełniony
# wynik_warunku = True


# while wynik_warunku:
#     print("Warunek jest spełniony")
#     print("thftgadfg")

# Korzyści korzystania z pętli:
# 1. Znacznie mniej linijek do napisania
# PRZYKŁAD - chcemy przywitać się 10 razy

# #bez pętli:
# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")

# #z pętlą
# i=0
# while i<25:
#     print("Dzień dobry")
#     i+=1

# #2. Elastyczny kod
# #PRZYKŁAD - chcemy przywitać się jednak 25 razy

# #3. Czytelność kodu


# #Zadanie 1 "Wyświetlanie komunikatów"
# #Program wypisze tyle przywitac ile nakaże mu użytkownik



# #Zadanie 2 "Timer bomby"
# #Program wykonuje odliczanie od podanej przez użytkownika liczby
# #Następnie pojawia się napis "BOOM!"
# import time #praca w czasem
# time.sleep(1) #sekundy
# import time

# #1. Podajemy czas odliczania
# #2. pozostaly_czas = czas
# #3. while (czy wiekszy od 0 ):
# #4.     wypisz pzostaly_czas
# #5.     czekaj sekunde
# #6.     zmiejsz pozostaly_czas o jeden

# #7. Wybuch

# czas = int(input("Podaj czas: "))

# while czas>0:
#     print(czas)
#     time.sleep(1)
#     czas-=1

# print("BOOM")



# #Zadanie 3 "Zgadywanka"
# #Zgadujemy liczbę jaką wylosował komputer
# #Program, dopóki nie zgadniemy, daje nam odpowiedzi "za dużo", "za mało", lub "ZGADŁEŚ" jest uda nam się zgadnąć
# import random #losowanie wartości
import random

MINIMUM = 0
MAXIMUM = 100

number = random.randint(MINIMUM, MAXIMUM)

print(number)

answer = None #nasza odpowiedź na start pusta
counter = 0 #licznik tur

while answer != number:
    answer = int(input("Zgadnij wylosowaną liczbę: "))
    counter +=1

    if answer < number:
        print("Za mało")
    elif answer > number:
        print("Za dużo")

print(f"Udało Ci sie zgadnąć liczbę: {number}")
print(F"Liczba prób: {counter}")


#PĘTLA NIESKOŃCZONA
#przydatna np. do stacji pogodowych
import time

# while True:
#     print("Nie zatrzymam się")
#     time.sleep(1)


#BREAK - przerwij pętle 
# import time

# i=0
# while True:#2
#     i+=1
#     if(i==3):
#         break
#     print("sdifujhvs")

# print("Żart, jednak się zatrzymam")

#PRZYKŁAD
#Zadanie "Echo"
#wariant bez 'break':
# print("Będe twoim echem")

# while (True):
#     odp = input("Napisz slowo: ")

#     if odp=="exit":
#         break

#     print("Echo: " + odp)

# print("Do zobaczenia")






#CONTINUE - pomiń ten krok i przejdź do następnego, czyli zakończ ten obrót pętli i sprawdź warunek od nowa
#PRZYKŁAD
# i=0
# while True:
#     if(i==5):
#         i+=2
#         continue
    
#     i+=1
#     print(i)
#     time.sleep(1)



#Zadanie "Logowanie"
#Użytkownik musi podać poprawnie po kolei: PIN, rok_urodzenia, haslo
#Jeżeli jakiekolwiek dane zostaną podane źle, program zaczyna się od nowa
#Dopiero jeśli wszytskie dane zostaną podane poprawnie to pętla się kończy i daje komunikat o zalogowaniu

# PIN = "2345"
# YEAR_OF_BIRTH = "2005"
# PASSWORD = "zaqwsx"

# while True:
#     input_pin = input("PIN: ")
#     if input_pin != PIN:
#         print("Odmowa dostępu - zaczynamy od nowa")
#         continue

#     print("Etap 1 zrealizowano poprawnie (poprawny PIN).")
#     input_year = input("Rok urodzenia: ")
#     if input_year != YEAR_OF_BIRTH:
#         print("Odmowa dostępu - zaczynamy od nowa")
#         continue
    
#     print("Etap 2 zrealizowano poprawnie (poprawny rok urodzenia).")
#     input_password = input("Hasło: ")
#     if input_password != PASSWORD:
#         print("Odmowa dostępu - zaczynamy od nowa")
#         continue

#     print("Etap 3 zrealizowano poprawnie (poprawne).")
#     print("Zalogowano poprawnie")
#     break

# print("Tajne treści i inne takie, dostępne po zalogowaniu - czyli tutaj")
