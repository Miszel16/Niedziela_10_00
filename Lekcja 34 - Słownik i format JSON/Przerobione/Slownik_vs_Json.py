# Przypominajka - słowniki (klucz-wartość)
# Tworzenie słownika
student = {
    'name': 'Jan Kowalski',
    'age': 22,
    }

# -----------------------------------------------------------------------------

# FORMAT JSON (JavaScript Object Notation)
# - lekki format wymiany danych, 
# - łatwy do odczytu i zapisu dla ludzi
# - łatwy do interpretacji i generowania przez maszyny
# - format tekstowy
# - używany do przesyłania danych między serwerem, a aplikacją internetową


# STRUKTORA
# - pary klucz - wartość,
#         - klucz: napis,
#         - wartość: napis, liczba, obiekt-zagnieżdżony JSON, tablica-lista, bool, null
# - uporządkowane listy wartości,



# PODOBIEŃSTWA
# ------------------------------------------------------------------
# 1. Mają klucz i wartość (np. "Imię": "Ala").
# 2. Mogą zawierać zagnieżdżone dane (pudełka w pudełkach).
# 3. Python łatwo zamienia słownik ↔ JSON.

# RÓŻNICE
# ------------------------------------------------------------------
# 1. Słownik: działa tylko w Pythonie.
#    JSON: działa wszędzie – jest światowym standardem.
# 2. Słownik: używany wewnątrz programu.
#    JSON: używany do wysyłania danych między komputerami.
# 3. JSON trzeba zamienić na tekst i z powrotem (serializacja/deserializacja).


# Zapoznanie z metodami obu struktur:
# * wrzucić do folderu:
# https://drive.google.com/file/d/1DUM6Ikkna_k59fIaWE8yt-WbB35nqDky/view


# ------------------------ METODY SŁOWNIKA ------------------------
#       klucze    :  wartość
gra = {"nazwa_gry" : "CS",
       "data_wydania" : 1999,
       "wydawca" : "valve",
       "gatunek" : "strzelanka"}


# - odwoływanie się do elementów:
# print(gra.get("nazwa_gry"))
# print(gra["nazwa_gry"])

# print(gra.get("nazwa_gy")) #None
# print(gra["nazwa_gy"]) # Błąd

print("\n")
# - iterowanie po wartościach:
for value in gra.values():
    print(value)


print("\n")
# - iterowanie po kluczach:
for key in gra.keys():
    print(key)


print("\n")
# - iterowanie po parach klucz-wartość:
for item in gra.items():
    print(item)


print("\n")
# - dodanie pary klucz-wartość:
gra.setdefault("PEGI", 18)
print(gra)


print("\n")
# - usunięcie i zwrócenie pary kluczy (spod podanego klucza)
delated = gra.pop("wydawca")
print(delated)
print(gra)


print("\n")
# - usunięcie i zwrócenie ostatniej pary klucz-wartość
last_item = gra.popitem()
print(last_item)
print(gra)


print("\n")
# - usunięcie pary klucz-wartość spod podanego klucza
del gra["gatunek"]
print(gra)





print("\n")
# - usunięcie wszystkich par klucz-wartość
gra.clear()
print(gra)


print("\n")
# - biblioteka pprint (pretty printer) estetyczniejsze wyświetlanie danych
import pprint
pprint.pprint(gra)

# ------------------------------------------------------------------

# ============================================
# 📚 BIBLIOTEKA json
# ============================================
# Biblioteka json pomaga:
# - zamieniać obiekty Pythona na tekst w formacie JSON (serializacja),
# - zamieniać tekst JSON na obiekty Pythona (deserializacja).
#
# To jest potrzebne np. gdy:
# - zapisujemy dane do pliku,
# - wysyłamy dane przez internet (np. do API),
# - chcemy, żeby inne programy mogły odczytać nasze dane.

# --------------------------------------------
# PODSTAWOWE FUNKCJE BIBLIOTEKI json
# --------------------------------------------
# 1. json.dumps()
#    - zamienia obiekt Pythona (np. słownik) na łańcuch znaków (string)
#      w formacie JSON.
#
# 2. json.loads()
#    - zamienia łańcuch znaków w formacie JSON na obiekt Pythona
#      (np. słownik).
#
# 3. json.dump()
#    - zapisuje obiekt Pythona do pliku w formacie JSON.
#
# 4. json.load()
#    - wczytuje dane JSON z pliku i zamienia je na obiekt Pythona.
# --------------------------------------------



# ------------------------- ĆWICZENIE ----------------------------
import pprint
import json

gra = {"nazwa_gry" : "CS",
       "data_wydania" : 1999,
       "wydawca" : "valve",
       "gatunek" : "strzelanka"}

# otwiera plik w trybie read (czytanie)
with open("l1.json","r" ) as file:

    #W słowniku szukamy listy pod kluczem "spis_gier"
    spis_gier = json.load(file)

# Dodajemy do listy nową grę którą wcześniej stworzyliśmy
spis_gier["spis_gier"].append(gra)

# Wyświetlamy zaktualizowaną listę gier
pprint.pprint(spis_gier["spis_gier"])


# Tworzymy lub otwieramy plik l1_2.json w trybie zapisu
with open("l1_2.json", "w") as file:

    # Zapisujemy cały słownik do pliku w formacie JSON
    json.dump(spis_gier, file, indent = 4, sort_keys = True)


# ------------------------- CIEKAWOSTKA ----------------------------
# ŁACZENIE SŁOWNIKÓW

dict1 = {"a" : 4, "b": 3}
dict2 = {"c" : 1, "d": 2}

# sposób 1
dict3 = {**dict1, **dict2}

# sposób 2
dict4 = dict1 | dict2

print(dict3)
print(dict4)

# ------------------------- ZADANIE DODATKOWE ----------------------------
# CIĄG FIBONACCIEGO

fib_json = {0:0, 1:1}
def fibonacci(n):
    if n in fib_json:
        return fib_json[n]
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        fib_json[n] = result
        return result

fibonacci(20)
for item in fib_json.items():
    print(item)