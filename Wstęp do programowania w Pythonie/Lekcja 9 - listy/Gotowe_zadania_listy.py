# Rozgrzewka
# Napisz program, który zapyta użytkownika o N ocen cząstkowych, a następnie wyliczy średnią z przedmiotu.
# Na koniec wypisze wynik z zaokrągleniem do całości

N = int(input("Podaj ilość ocen: "))
wynik = 1

for i in range(N):
    ocena = int(input())
    wynik += ocena

print(wynik / N)
print(wynik // N)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Średnia z podanych ocen"
# Program musi wczytywać oceny, aż napotka znak ‘q’ mówiący, że wprowadzono wszystkie oceny.
# Dodać je do listy i na koniec obliczyc średnią.
# Po każdej dodanej ocenie pokaz całą listę
# Krok po kroku:

oceny = []

while True:
    ocena = input("Podaj ocenę: ")

    if ocena == 'q':
        break

    ocena = int(ocena)
    oceny.append(ocena)
    print(oceny)

suma = sum(oceny)
srednia = suma / len(oceny)
print(f"Średnai z podanych ocen to : {srednia}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Komunikaty"
# Program zapyta o liczbę elementów, które ma przyjąć, a następnie odczyta od
# użytkownika tyle komunikatów. Na koniec wyświetli je w tej samej kolejności.
# Elementy musza byc zapisane w liście. Należy wykorzystać indeksy.

liczba_elementow = int(input("Podaj liczbe elementów: "))

elementy = []

for i in range(liczba_elementow):
    komunikat = input(f"Podaj elemnt numer {i}: ")
    elementy.append(komunikat)

for i in range(len(elementy)):
    print(elementy[i], end=' ')











#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Mnożenie"
# Napisz program, który wymnoży ze sobą wszystkie elementy w liście.
# Lista ma zawierać tylko liczby (całkowite lub float).

liczby = [5, 6, -7, 5.23, 0.1]

wynik = 1

for i in liczby:
    wynik *= i

print(wynik)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Bez powtórzeń"
# Napisz program, który pyta użytkownika o 10 liczb, ale w liście nie mogą wystąpić
# powtórzenia. Jeżeli użytkownik poda liczbę, która została podana wcześniej program
# powinien wyświetlić stosowny komunikat oraz zapytać ponownie o liczbę.
# Należy wykorzystać pętle while

liczby = []

while len(liczby) < 10:
    a = int(input("Podaj liczbę: "))

    if a in liczby:
        print("Wprowadzono juz taką liczbę.")
    else:
        print("Nie mam jeszcze takiej liczby, dodaje ją do listy.")
        liczby.append(a)
    print(liczby)

print("Mamy wszystkie 10 liczb!")
print(liczby)