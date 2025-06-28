#Zadanie dodatkowe: 
# Przygotuj program, który zapyta użytkownika o 3 różne liczby, każdą z nich wpisz do zmiennych: a, b, c.
# Przygotuj trzy zmienne typu bool: czy_a_to_max, czy_b_to_max, czy_c_to_max.
# Dodatkowe wymaganie: do obliczenia wartości czy_c_to_max wykorzystaj tylko
# zmienne czy_a_to_max i czy_b_to_max - (nie wykorzystujemy a, b, c).

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
c = int(input("Podaj liczbę c: "))

czy_a_to_max = a > b and a > c
czy_b_to_max = b > a and b > c
czy_c_to_max = not (czy_a_to_max or czy_b_to_max)

print(czy_a_to_max)
print(czy_b_to_max)
print(czy_c_to_max)