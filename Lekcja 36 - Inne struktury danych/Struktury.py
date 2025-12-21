# Czym jest lista? (3 znane metody)
# Czym jest słownik? (3 znane metody)

# STRUKTURY DANYCH

print(f'Krotki:')
# 1. KROTKI (TUPLES) ------------------------------------------
# - „rekord”, który jest stały
# - dane logicznie tworzą jedną całość i nie chcesz ich zmieniać
# - np. punktu (x, y), daty (rok, miesiac, dzien), wyniku funkcji (kilka wartości na raz)
# - Można używać jako kluczy w słowniku (bo jest niemodyfikowalna)

krotka = (4,2,11,2,4)
krotka2 = (4,)
print(krotka)
print(krotka2)

# wycinek
# start, stop
print(krotka[1:4]) # 2,11,2

# element 
print(krotka[0]) # 4



# METODY
# 1. Zliczanie elementów o danej wartości [.count()]
ile = krotka.count(2) 
print(f"Ile '2' w kroptce: {ile}\n") # 2


# 2. Znalezienie pierwszego indeksu o danej wartości [.index()]
indeks = krotka.index(4)
print(f"Gdzie pierwsza '4': {indeks}\n") # 0



print(f'\n\n\nZbiory:')
# 2. ZBIORY (SETS) -----------------------------------------------
# - unikalne elementy + matematyka na zbiorach
# - usuwa duplikaty
# - operacje typu: część wspólna, różnica, suma zbiorów
# - nie może zawierać listy

zbior = {1,2,3,4,4,4,4,4}
pusty_zbior = set()
print(zbior)
print(pusty_zbior)




# METODY
# 1. Dodanie elementu do zbioru [.add()]
zbior.add(67)
print(f"Po dodaniu '67': {zbior}\n")




# 2. Usunięcie elementu o podaje wartości [.remove()]
# *sprawdzić, co jak zły klucz
zbior.remove(67)
print(f"Po usunięciu '67': {zbior}\n")



# 3. Usunięcie elementu jeżeli istnieje [.discard()]
zbior.discard(10)
print(f"Po usunięciu '10': {zbior}\n")



# 4. Usunięcie pierwszego elementu i zwrócenie go [.pop()]
element = zbior.pop()
print(f"Co usuwamy {element}\nPo usunięciu {element}: {zbior}\n")



# 5. Czyszczenie zbioru [.clear()]
zbior.clear()
print(zbior)


# ------------------- ZESTAWIENIE WSZYTSKICH DOTYCHCZASOWYCH STRUKTUR -------------------
print(f"\n\n\nKonwersje:\n")
# KONWERSJE MIĘDZY STRUKTURAMI

zbior = {1,2,3}
krotka = (4,5,6)
lista = [7,8,8,9]

print("\nZbiór na liste:")
print(f"{zbior}: {type(zbior)}")
print(f"{list(zbior)}: {type(list(zbior))}\n")


print("\nKrotka na liste:")
print(f"{krotka}: {type(krotka)}")
print(f"{list(krotka)}: {type(list(krotka))}\n")


print("\nZbiór na krotke:")
print(f"{zbior}: {type(zbior)}")
print(f"{tuple(zbior)}: {type(tuple(zbior))}\n")


print("\nLista na krotke:")
print(f"{lista}: {type(lista)}")
print(f"{tuple(lista)}: {type(tuple(lista))}\n")


print("\nKrotka na zbior:")
print(f"{krotka}: {type(krotka)}")
print(f"{set(krotka)}: {type(set(krotka))}\n")


print("\nLista na zbior:")
print(f"{lista}: {type(lista)}")
print(f"{set(lista)}: {type(set(lista))}\n")