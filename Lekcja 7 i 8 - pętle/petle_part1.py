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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# #Zadanie 1 "Wyświetlanie komunikatów"
# #Program wypisze tyle przywitac ile nakaże mu użytkownik

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# #Zadanie 2 "Timer bomby"
# #Program wykonuje odliczanie od podanej przez użytkownika liczby
# #Następnie pojawia się napis "BOOM!"
# import time #praca z czasem
# time.sleep(1) #sekundy


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# #Zadanie 3 "Zgadywanka"
# #Zgadujemy liczbę jaką wylosował komputer
# #Program, dopóki nie zgadniemy, daje nam odpowiedzi "za dużo", "za mało", lub "ZGADŁEŚ" jest uda nam się zgadnąć
# import random #losowanie wartości
# import random

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#PĘTLA NIESKOŃCZONA
#przydatna np. do stacji pogodowych
import time

# while True:
#     print("Nie zatrzymam się")
#     time.sleep(1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#BREAK - przerwij pętle 
# import time
# i=0
# while True:
#     i+=1
#     if(i==3):
#         break
#     print(f"{i}")

# print("Żart, jednak się zatrzymam")

#PRZYKŁAD
# Zadanie "Echo"

# wariant bez 'break':
# print("Będe twoim echem")

# while True:
#     odp = input("Napisz slowo: ")
#     if odp=="exit":
#         break
#     print("Echo: " + odp)

# print("Do zobaczenia")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#CONTINUE - pomiń ten krok i przejdź do następnego, czyli zakończ ten obrót pętli i sprawdź warunek od nowa

#PRZYKŁAD
# i=0
# while True:
#     if i == 10:
#         break
#     if i==5:
#         i+=1
#         continue
#     i+=1
#     print(i)
#     time.sleep(1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Zadanie "Logowanie"
#Użytkownik musi podać poprawnie po kolei: PIN, rok_urodzenia, haslo
#Jeżeli jakiekolwiek dane zostaną podane źle, program zaczyna się od nowa
#Dopiero jeśli wszytskie dane zostaną podane poprawnie to pętla się kończy i daje komunikat o zalogowaniu
