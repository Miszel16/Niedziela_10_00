# https://github.com/Miszel16/Niedziela_10_00

# Discord




# Rozgrzewka
# Napisz program, który zapyta użytkownika o N ocen cząstkowych, a następnie wyliczy średnią z przedmiotu.
# Na koniec wypisze wynik z zaokrągleniem do całości

# n = int(input("Podaj liczbe ocen: "))
# wynik = 0

# for i in range(n):
#     ocena = int(input("Podaj ocene: "))
#     wynik += ocena

# print(wynik / n)
# print(wynik // n)








#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # LISTY - struktury danych, które służą do przechowywania wielu elementów w jednej zmiennej

# # PRZYKŁAD
ocena_nr_1 = 4
ocena_nr_2 = 5
ocena_nr_3 = 3
ocena_nr_4 = 4.5
ocena_nr_5 = 2
ocena_nr_6 = 1
ocena_nr_7 = 6
ocena_nr_8 = 5

oceny = [4, 5, 3, 4.5, 2, 1, 6, 5]

#~~~~~~~~

# # Zasady
# 1. Reguły nazywania listy = Reguły nazywania zmiennej
# 2. []
# 3. Wewnątrz listy - elementy
# 4. Kolejny element dopisujemy po przecinku; po ostatnim elemencie brak przecinka
# 5. Lista może pmiec elementy rożnego typu:

moja_lista = [2, "Napis", 'litera', 2.5, -10.001, True, 'a', ["Kolejna", 0, "Lista"], 10, -2]

#~~~~~~~~

# # Spodoby zapisywania
# 1. PŁASKO

plaska_lista = [1, "ala ma kota", True, 4, 7, 7.89]


# 2. OD NOWEJ LINII

od_nowej_linii_lista = [
    1,
    "ala ma kota",
    True,
    4,
    7,
    7.89
]

#~~~~~~~~

# # WYPISYWANIE - tak jak zmienne
# print(moja_lista)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#ĆWICZENIE
# 1) Przygotuj 3 listy, a następnie wyświetl się w konsoli, aby sprawdzić czy zostały poprawnie przygotowane.
# - Listę 5 losowych liczb, które przyjdą Ci do głowy (również z ułamkami)
# - Listę minimum 3 ulubionych gier / filmów / piosenek
# - Listę składającą się z 3 list, w których odpowiednio wpiszesz Imię, Nazwisko i Wiek trzech wymyślonych osób.

Ludzie = [
    ["Adam", "Nazwisko", "40"] , 
    ["Julek", "Nazwisko", "56"]
    ]

lista_danych = [Ludzie]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# #INDEKSY

# #        0  1  2   3   4  5  6  7
# oceny = [4, 5, 3, 4.5, 2, 1, 6, 5]

# print(oceny[4])

# moja_ocena = oceny[0]

# print(moja_ocena)

# # print(f"Próba wyciągnięcia indeksu spoza zakresu listy: {oceny[10]}")

# #Funkcja len() - ilośc elementów w liście
# print(len(oceny))
# print(oceny[len(oceny)-1])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# #DODAWANIE ELEMENTÓW DO LISTY

# #Funkcja append() - dodawanie nowego elementu na koniec listy

# alfabet = ["a", "b", "c", "d", "e", "f"]

# print(alfabet, len(alfabet))

# alfabet.append("g")
# print(alfabet, len(alfabet))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Średnia z podanych ocen"
# Program musi wczytywać oceny, aż napotka znak ‘q’ mówiący, że wprowadzono wszystkie oceny.
# Dodać je do listy i na koniec obliczyc średnią.
# Po każdej dodanej ocenie pokaz całą listę
# Krok po kroku:

# oceny = []

# while True:
#     ocena = input("Podaj ocene: ")

#     if ocena == 'q':
#         break
    
#     ocena = int(ocena)
#     oceny.append(ocena)

#     print(oceny)

# suma = sum(oceny)
# print(f"Średnia to {suma/len(oceny)}")



# Zadanie "Komunikaty"
# Program zapyta o liczbę elementów, które ma przyjąć, a następnie odczyta od
# użytkownika tyle komunikatów. Na koniec wyświetli je w tej samej kolejności.
# Elementy musza byc zapisane w liście. Należy wykorzystać indeksy.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#ITEROWANIE

# elementy = ["niebieski", "czerwony", "żółty", "zielony"]

# for elem in elementy:
#     print(elem)

# #najlepszy sposób jeśli nie interesuje nas numer indeksu tylko same elementy

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#INNE FUNKCJE LIST

# https://www.w3schools.com/python/python_ref_list.asp

# CLEAR() - usuwa wszystkie elemnty z listy i zostawia ja pustą

# pelna_lista = [1, 2, 3, 4]
# print(pelna_lista)

# pelna_lista.clear()
# print(pelna_lista)


# COUNT() - zlicza ile razy dany element występuje w liście

# cyfry = [1, 1, 1, 2, 1, 5]
# print(f"Ile '1' jest w liście?: {cyfry.count(1)}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#ZAKRES INDEKSÓW - CZYLI WYCIĄGAMY WIĘCEJ NIŻ JEDEN

# # Indeksy:0  1  2  3  4  5  6  7   8   9  10  11   12  13  14
# liczby = [9, 1, 0, 2, 0, 3, 4, 5, 10, -1, 20, 32, -20, -3, -4]

# print(liczby[11]) #32


# Zakres <start; stop) -> <2; 8) -> indeksy 2, 3, 4, 5, 6, 7

# start - pierwszy który wyciągamy
# stop - pierwszy, którego nie wyciągamy
# nowa_lista = liczby[2: 8]
# print(nowa_lista)

# #Przykłady:
# nowa_lista = liczby[10: 13]
# print(nowa_lista)

# nowa_lista = liczby[2: 20]  # 2 <=  indeks < 20
# print(nowa_lista)

# nowa_lista = liczby[10: 3]  # 10 <=  indeks < 3
# print(nowa_lista)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # UJEMNE INDEKSY - numerowanie od końca

# # Indeksy:   0   1  2   3   4   5   6  7   8   9  10  11   12  13  14
# liczby  =  [ 9,  1, 0,  2,  0,  3,  4, 5, 10, -1, 20, 32, -20, -3, -4] #len(liczby) = 15
# # Indeksy: -15 -14 -13 -12 -11 -10 -9 -8  -7  -6  -5  -4   -3  -2  -1


# nowa_lista = liczby[-13: -5] # <-13; -5)
# print(nowa_lista)


# nowa_lista = liczby[2: 10] # <2; 10)
# print(nowa_lista)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# OD POCZĄTKU LUB DO KOŃCA

# # Indeksy:   0   1  2   3   4
# liczby  =  [ 9,  1, 0,  2,  0]

# nowa_lista_od_poczatku = liczby[:3]

# print(nowa_lista_od_poczatku) # 9, 1, 0


# nowa_lista_do_konca = liczby[1:]
# print(nowa_lista_do_konca) # 1, 0,  2, 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ODCZYTYWANIE OD RAZU DO ZMIENNYCH

# # 1.
# oceny_z_3_sprawdzianow = [5, 4.5, 3]

# ocena1, ocena2, ocena3 = oceny_z_3_sprawdzianow

# print(ocena1)
# print(ocena2)
# print(ocena3)

# #Uwaga jeśli liczba zmiennych będzie się różnić od liczby elementów otrzymamy błąd!
# 2. 
# wszystkie_oceny = [3, 5, 6, 5, 4, 5, 5, 4, 3, 4, 5, 2]

# ocena1, ocena2 = wszystkie_oceny[:2]

# print(ocena1)
# print(ocena2)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie "Mnożenie"
# Napisz program, który wymnoży ze sobą wszystkie elementy w liście.
# Lista ma zawierać tylko liczby (całkowite lub float).

# liczby = [2, 5, -6, 8, 3.2]

# wynik = 1

# for i in liczby:
#     wynik = wynik * i
#     print(i)

# print(wynik)

#KONTYNUACJA ZA TYDZIEŃ


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# CZY ELEMENT ZNAJDUJE SIE W LIŚCIE?

# liczby = [5, 6, -7, 5.23, 0.1]

# if 2 in liczby:
#     # Kod wykonywany, jeśli dwójka znajduje się w liście

#     pass
# if 5 not in liczby:
#     # Kod wykonywany, jeśli piątka nie znajduje się w liście
#     pass


# Zadanie "Bez powtórzeń"
# Napisz program, który pyta użytkownika o 10 liczb, ale w liście nie mogą wystąpić
# powtórzenia. Jeżeli użytkownik poda liczbę, która została podana wcześniej program
# powinien wyświetlić stosowny komunikat oraz zapytać ponownie o liczbę.
# Należy wykorzystać pętle while


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# STRING - lista pojedynczych znaków, mozna iterować

# napis = "Ala ma kota"

# print(napis[5])

# print(len(napis))

# for znak in napis:
#     print(f"Znak {znak}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# TWORZENIE NAPISU Z LISTY NAPISÓW .join()

# napis_typu_str_lub_cudzysłów.join(lista_elementów)

# 1.
# slowa = ['Ala', 'ma', 'kota']
# tekst = ' '.join(slowa)
# print(tekst)

# 2.
# przecinek = ", "

# imiona = ['Tomek', 'Ola', 'Zuzia', 'Paweł']
# tekst = przecinek.join(imiona)
# print(tekst)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # ITEROWANIE PO NAPISACH

# napis = "Ciąg różnych znaków!"

# for c in napis:
#     print(c, end='.') #znaki oddzielone kropkami