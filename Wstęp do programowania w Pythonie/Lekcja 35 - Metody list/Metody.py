# * Co było ostatnio?
# - słownik w pythonie
# - JSON to format globalny


# Rozgrzewka
# Napisz listę zawierająca 10 różnych wartości, a następnie wypisz co drugą:
# xxxx


rozgrzewka = [1,2,3,4,5,6,7,8,9,10]
#             0,1,2,3,4,5,6,7,8,9

# start stop step
# for i in range(10): # 0,1,2,3,4,5,6,7,8,9
#     if i % 2 == 0:
#         print(rozgrzewka[i])




# 1. Co znamy do tej pory?
# - iterowanie
# - różne typy wartości (listy w liście, różne zmienne)
# - indeksowanie (w począrtku i od końca)
# - modyfikowanie po utworzeniu
# - dynamiczny rozmiar

# .append() - dodawanie na koniec
# .pop() - ??





# 2. METODY
#--------------------------------------------------------------------------------
# 1) utworzenie listy
moja_lista = [16, "kot", 7.5, True, "Alicja"]
print(f"Moja lista: {moja_lista}\n")


#--------------------------------------------------------------------------------
# 2) dodawanie elementów na koniec listy [.append()]
moja_lista.append("zima")
print(f"{moja_lista}\n")


#--------------------------------------------------------------------------------
# 3) !! poszerzenie listy o element po którym można iterować [.extend()]
top_uczniowie = ["Antonio", "Lena", "Kacper", "Mati", "Piotrek"]
moja_lista.extend(top_uczniowie)
print(f"{moja_lista}\n")


#--------------------------------------------------------------------------------
# 4) !! dodawanie pod wskazany indeks [.insert()]
print(f"{list(enumerate(moja_lista))}\n") # (indeks, wartość)

moja_lista.insert(5, "Minecraft")
print(f"Lista po dodaniu elementu: {list(enumerate(moja_lista))}\n")


#--------------------------------------------------------------------------------
# 5) !! usuwanie elementu o konkretnej wartości [.remove()]
# * usuwa pierwszy pasujący
# * co jeśli nie znajdzie?
moja_lista.remove("zima") # "mango"
print(f"Lista po usunięciu:\n {moja_lista}\n")

# moja_lista.remove("mango") # "mango"
# print(f"Lista po usunięciu:\n {moja_lista}\n")


#--------------------------------------------------------------------------------
# 6) !! usunięcie elementu spod wskazanego indeksu i ZWRÓCENIE GO [.pop()]
# * co jeśli nie znajdzie?
element = moja_lista.pop(2)
print(f"Lista po usunięciu: {element}\n {moja_lista}\n")


#--------------------------------------------------------------------------------
# 7) !! znajdowanie indeksu dla podanej wartości [.index()]
# * zwraca pierwszy pasujący
# * co jeśli nie znajdzie?
print(f"{list(enumerate(moja_lista))}\n") # (indeks, wartość) #  Minecraft - 4

#I - pierwszy znaleziony
id = moja_lista.index("Minecraft")
print(f"{id}\n")


#II - szuka od indeksu
id = moja_lista.index("Minecraft", 4) # start stop
print(f"{id}\n")


#III - szukaj w przedziale 
id = moja_lista.index("Minecraft", 0, 5) # start stop
print(f"{id}\n")


#--------------------------------------------------------------------------------
# 8) zliczanie wsytąpień danej wartości [.count()]
moja_lista.append("Minecraft")

ile = moja_lista.count("Minecraft")
print(ile) # 2


#--------------------------------------------------------------------------------
# 9) !! sortowanie listy [.sort()]
# * elementy muszą dać się ze sobą porównać (str != int -> nie zadziała)

nowa_lista = [3,2,45,5,6,0,23,0,0,0]
print(f"{nowa_lista}\n")
nowa_lista.sort()
print(f"{nowa_lista}\n")



#--------------------------------------------------------------------------------
# 10) !! odwrócenie kolejności listy [.reverse()]
print(f"{moja_lista}\n")

moja_lista.reverse()

print(f"{moja_lista}\n")


#--------------------------------------------------------------------------------
# 11) !! kopiowanie listy [.copy()]
# * kopiowanie płytkie - kto znajdzie i wytłumaczy ma plusa
kopia_moja_lista = moja_lista.copy()

print(f"Moja lista:\n{moja_lista}\n")

print(f"Kopia mojej listy:\n {kopia_moja_lista}\n")


#--------------------------------------------------------------------------------
# 12) czyszczenie listy [.clear()]
moja_lista.clear()
print(moja_lista) # []