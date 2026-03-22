# Przypominajka - słowniki (klucz-wartość)
# Tworzenie słownika


uczen = {
    'imie': 'Alicja',
    'wiek': 20,
    }

# -----------------------------------------------------------------------------

# FORMAT JSON (JavaScript Object Notation)
# - lekki format wymiany danych, 
# - łatwy do odczytu i zapisu dla ludzi
# - łatwy do interpretacji i generowania przez maszyny
# - format tekstowy
# - używany do przesyłania danych między serwerem, a aplikacją internetową







# STRUKTURA
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

# 1. iterowanie
# - wartościach
for wartosc in gra.values():
    print(wartosc)

print("\n")
# - kluczach
for klucz in gra.keys():
    print(klucz)

print("\n")
# - klucz-wartość
for item in gra.items():
    print(item)
print("\n")

#----------------------------------------
# 2. Modyfikacje
# - dodanie pary klucz-wartosc
gra.setdefault("PEGI", 18)
print(gra)
print("\n")

# - usunąc pare i zwrócić ją (ostatnia z końca)
ostatni_item = gra.popitem()
print(ostatni_item) #PEGI
print(gra)

print("\n")
# - usunąc pare i zwrócić ją (spod danego klucza)
deleted = gra.pop('data_wydania')
print(deleted)
print(gra)

print("\n")
# - usunąć pare (spod danego klucza)
del gra['wydawca']
print(gra)

print("\n")
# - usunąć wszytskie pary
gra.clear()
print(gra)
#----------------------------------------
gra = {"nazwa_gry" : "CS",
       "data_wydania" : 1999,
       "wydawca" : "valve",
       "gatunek" : "strzelanka"}

# 3. Wypisywanie
import pprint

print(gra)
print("\n")

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
# load: (JSON -> Słownika)
# dump: (Słownika -> JSON)

# ------------------------- ĆWICZENIE ----------------------------
import pprint
import json



gra = {"nazwa_gry" : "CS",
       "data_wydania" : 1999,
       "wydawca" : "valve",
       "gatunek" : "strzelanka"}

# 1. Dodanie gry 'CS' do json l1

# otwieramy w trybie 'read'
with open("l1.json", "r") as file:
    spis_gier = json.load(file)

spis_gier["spis_gier"].append(gra)

pprint.pprint(spis_gier["spis_gier"])


# 2. Tworzymy nowy json
# otwieramy w trybie 'write'
with open("l2.json", 'w') as file:
    # zapisujemy do json naszą stworzoną listę
    json.dump(spis_gier, file, indent=4, sort_keys=True)












# ------------------------- CIEKAWOSTKA ----------------------------
# ŁACZENIE SŁOWNIKÓW

dict1 = {"a" : 4, "b": 3}
dict2 = {"c" : 1, "d": 2}

# sposób 1


# sposób 2


# print(dict3)
# print(dict4)

# ------------------------- ZADANIE DODATKOWE ----------------------------
# CIĄG FIBONACCIEGO
