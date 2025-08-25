# ● Tabela z wynikami dla jednego gracza 
# ● Gra trwa dopóki wszystkie rubryki nie będą pełne (ilość tur = ilość kategorii w grze)
# ● Wykonamy gre z kategoriami SZKOŁy (jedynki, ... , szóstki)

# PLAN OGÓLNY:
# 1. Rzucanie wybranymi kośćmi
# 2. Wyświetlenie co wyrzuciliśmy
# 3. Czy chcemy rzucić jeszcze raz?
# 4. Ponowne rzuty wybranymi kośćmi (max. 2)
# 5. Wyświetlenie górnej części tabeli wyników (kategorii)
# 6. Gdzie chcemy wpisać punkty?
# 7. Wstawienie punktów do odpowiedniej rubryki
# 8. Pętla gry, która wykonuje się odpowiednią ilość razy

import random
kosci = [1,2,3,4,5] #dla testów

# 5a.
kategorie = ["Jedynki", "Dwójki", "Trójki", "Czwórki", "Piątka", "Szóstki"]
punkty = ['','','','','','']


# 1.
def rzuc_koscmi(numery_kosci:str):
    for i in numery_kosci:
        index = int(i) - 1
        kosci[index] = random.randint(1,6)

#TEST po 1
# print(kosci)
# rzuc_koscmi("12345")
# print(kosci)

# 2. 
def pokaz_kosci():
    print("_____________")
    for i in range(len(kosci)):
        print(f'   {i+1}. {kosci[i]}')
    print("_____________")

#TEST po 2
# pokaz_kosci()

# 3.
def sprawdz_czy_przerzucamy() -> bool:
    odp = input("Czy chcesz przerzucić któreś z kości? (t/n)").lower()
    if odp == 't':
        return True
    else:
        return False



# 5b.
def pokaz_tabele_punktow():
    pierwszy_wiersz = ""
    drugi_wiersz = ""
    
    for i in range(len(kategorie)):
        pierwszy_wiersz += str(i+1) + '. ' + kategorie[i] + ' | '
        drugi_wiersz += str(punkty[i]).center(len(kategorie[i]) + 3) + ' | '
    
    print("__________________________________________________________________________")
    print(pierwszy_wiersz)
    print("--------------------------------------------------------------------------")
    print(drugi_wiersz)
    print("__________________________________________________________________________")


# 7.
def punkty_w_szkole(pole: int):
    liczba_punktów = 0
    for kosc in kosci:
        if kosc == pole:
            liczba_punktów += kosc
    punkty[pole-1] = liczba_punktów


# 6a.
def wstaw_punkty():
    pole = int(input("Gdzie chcesz wpisać punkty? (Podaj numer rubryki): "))
    if punkty[pole-1] == '':
        if 1 <= pole <= len(kategorie):
            punkty_w_szkole(pole)
    else:
        print("Wybrane pole jest już uzupełnione.")
        wstaw_punkty()


# 4.
# GŁÓWNY KOD PĘTLI
pokaz_tabele_punktow()
for tura in range(len(kategorie)):
    print("Pierwszy rzut w turze: ")
    rzuc_koscmi("12345")
    # 5c.
    pokaz_kosci()
    for i in range(2):
        przerzut = sprawdz_czy_przerzucamy()
        if przerzut:
            kosci_do_przerzutu = input("Które kości chcesz przerzucić? (Podaj numery bez spacji): ")
            rzuc_koscmi(kosci_do_przerzutu)
            pokaz_kosci()
        else:
            break

    # 5c.
    pokaz_tabele_punktow()
    pokaz_kosci()
    # 6b.
    wstaw_punkty()
    pokaz_tabele_punktow()

print(f"Twój łączny wynik to: {sum(punkty)}")