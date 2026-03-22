#Zadania
# 1. Stwórz krotkę, listę, słownik i zbiór zawierający po 3 elementy
krotka = (5,8,3)
lista = [10,12,4]
slownik = {
    "klucz1": 1,
    "klucz2": 2,
    "klucz3": 3
}
zbior = {6,3,10}


# 2. Za pomocą funkcji len() sprawdź długości poszczególnych obiektów
print(f"Lista: {len(lista)}")
print(f"Krotka: {len(krotka)}")
print(f"Slownik: {len(slownik)}")
print(f"Zbior: {len(zbior)}")


# 3. Za pomocą pętli for wypisz wszystkie elementy każdego z obiektów
print("Krotka:")
for i in krotka:
    print(i)



# 4. Teraz wypisz wartości słownika zamiast kluczy



# 5. Wypisz te same elementy w odwrotnej kolejności, czy zawsze jest to możliwe bezpośrednio?
# * podpowiedzi:
# - [start:stop:step] np. [::1] - wypisze wszystkie elementy
# - tylko struktury z indeksami można iterowac od końca (konwersja)

for i in list(slownik)[::-1]:
    print(i)



# 6. Dodaj do listy elementy z krotki, zbioru i wartości słownika.

# 7. Dodaj do listy 2 liczby - wartość maksymalna i minimalna listy.

# 8. Sprawdź długość listy.

# 9.Zamień listę na krotkę- krotka2 i sprawdź jej długość.

# 10.Zamień krotkę na zbiór - zbior2 i sprawdź jego długość, z czego wynika różnica?