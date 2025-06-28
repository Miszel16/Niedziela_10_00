#Operatory porównania (relacyjne >, >=, <, <=, ==, !=)

# print(250 > 42.01) #True
# print(490 <= 450) #False
# print(24 == 12) #False
# print(40 != 23) #True
# print(40 > 40) #False
# print(99 < 98.5) #False




#Zadanie 1
# print(12 == 15) # Fałsz # ==, <, !=, <=

# print(5  <=  15000) # Prawda # ==, >, >=, <=

# print(120 != 120) # Fałsz # ==, >=, !=, <=

# print(60 <  15) # Fałsz # ==, <, !=, >=
# print(60 == 15) # Fałsz # ==, <, !=, >=

# print(25.3421 <= 25.3421) # Prawda # ==, <, !=, <=
# print(25.3421 == 25.3421) # Prawda # ==, <, !=, <=



#Zadanie rollercoaster
# wzrost w cm musi byc wiekszy niż 164

# print("Czy możesz skorzystać z roller-coastera?")
# print("True - możesz skorzystać z roller-coastera")
# print("False - nie możesz skorzystać z roller-coastera")

# wzrost = int(input("Podaj wzrost: "))

# print(wzrost > 164) #True wzrost będzie wieksezy niż 164



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Działania logiczne - łączenie warunków razem

#OPERATOR JEDNOARGUMENTOWY NOT - negacja
# print(not True) #Wynik: False
# print(not False) #Wynik: True

# Przykłady
# print(not(50 == 50.001)) #True
# print(not(2 < 10)) #False
# print(not(4 > 10)) #True
# print(not(24 == 12)) #True
# print(not(34 >= 12)) #False
# print(not(4 <= 0.7384)) #True



#OPERATOR DWUARGUMENTOWY AND - oba warunki musza byc spełnione (True)
# print(True and True) #Wynik: True
# print(True and False) #Wynik: False
# print(False and True) #Wynik: False
# print(False and False) #Wynik: False
#Przykłady
# print(20 < 25 and 24 == 0) # True and False = False
# print(4 != 4.0 and 2 <= 0) # False and False = False
# print(2 < 5 and 50 != 50.001) # True and True = True 
# print(10 > 5 and 3 == 3) # True and True = True
# print(7 <= 2 and 100 != 100) # False and False = False
# print(-1 < 0 and 5 >= 5) # True and True = True
# print(9 == 9 and 8 < 7) # True and False = False
# print(15 != 20 and 0 >= -5) # True and True = True 


#OPERATOR DWUARGUMENTOWY OR - wystarczy jeden spełniony warunek (True)
# print(True or True) #Wynik: True
# print(True or False) #Wynik: True
# print(False or True) #Wynik: True
# print(False or False) #Wynik: False
#Przykłady
# print(20 < 25 or 24 == 0) # True or False = True
# print(4 != 4.0 or 2 <= 0) # False or False = False
# print(2 < 5 or 50 != 50.001) #True or True = True
# print(10 > 5 or 3 == 4) # True or False = True
# print(7 <= 2 or 100 != 100) # False or False = False
# print(-1 > 0 or 5 >= 5) # False or True = True
# print(9 == 8 or 8 < 7) #False or False = False
# print(15 != 20 or 0 < -5) #True or False = True


#Tabela Prawdy

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# #Zadanie rollercoaster 2.0
# # wzrost w cm musi byc wiekszy niż 150 i mniejszy niz 215

# print("Czy możesz skorzystać z roller-coastera?")
# print("True - możesz skorzystać z roller-coastera")
# print("False - nie możesz skorzystać z roller-coastera")

# wzrost = int(input("Podaj wzrost: "))

# print(wzrost > 150 and wzrost < 215)

# print(150 < wzrost < 215)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# #Zadanie 3: wstaw and/or/not
# #kolejność: (), not, and, or

# print(True, 25 < 140  and  10 == 10) # True , True (and, or)

# print(True, 100 >= 1  or  2 > 10) #True, False

# print(False, 25 < 14  or  10 != 10) #False, False (and, or)

# print(False, -1 < 3  and  2 < 9  and  10 == 15) #True, True, False
# print(False, (-1 < 3  or  2 < 9)  and  not(10 == 15)) #True, True, False

# print(True, 20.05 < 21 < 10   or  -10 < 20 < 150 <= 150) #False, True

# print(False, 1 < 10  and   2 < 15   and  -50 == 42)#True, True, False

# print(True,  not(2 == 10)) 


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# #Złożone działania logiczne
# #Kolejnośc wykonywanych operatorów  1. not  2. and  3. or
# print(False, not (10 < 10 or 20 <= 20))
# print(True, not 10 < 10 and 20 <= 20)



#Zadanie - zabezpieczenie przed dzieleniem przez zero: 
# a = int(input("Podaj liczbę całkowitą: "))

# werdykt = a != 0 and 100 / a > 5

# werdykt2 = (a != 0 and (100 / a) > 5)

# print(werdykt)




# #Zadanie dodatkowe: 
# # Przygotuj program, który zapyta użytkownika o 3 różne liczby, każdą z nich wpisz do zmiennych: a, b, c.
# # Przygotuj trzy zmienne typu bool: czy_a_to_max, czy_b_to_max, czy_c_to_max.
# # Dodatkowe wymaganie: do obliczenia wartości czy_c_to_max wykorzystaj tylko
# # zmienne czy_a_to_max i czy_b_to_max - (nie wykorzystujemy a, b, c).

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# # Operatory relacyjne i napisy
# print("Napis" == "Napis2") # Czy oba napisy są dokładnie takie same?
# print("Napis" != "Napis2") # Czy napisy są różne?

# print("a" > "A") #True

# UNICODE
# print(ord("a")) #97
# print(ord("A")) #65
# print(ord('😀')) #128512

# print(chr(97)) #a
# print(chr(65)) #A
# print(chr(128512))