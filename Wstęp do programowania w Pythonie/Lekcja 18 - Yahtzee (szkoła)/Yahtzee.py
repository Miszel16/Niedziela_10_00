# ● Tabela z wynikami dla jednego gracza 
# ● Gra trwa dopóki wszystkie rubryki nie będą pełne (ilość tur = ilość kategorii w grze)
# ● Wykonamy gre z kategoriami SZKOŁY (jedynki, ... , szóstki)

# PLAN
# (+) Rzucanie wybranymi kośćmi 
# (+) Czy chcemy rzucić jeszcze raz?
# (+) Ponowne rzuty wybranymi koścmi (max. 2)
# (+) Wyświetlenie tabelki wyników
# Gdzie chcemy wpisać punkty?
# Wstawienie punktów do odpowiedniej rubryki
# Pętla gry, która wykonuje się odpowiednią ilość razy

import random
#        1,2,3,4,5
kosci = [0,0,0,0,0]
#        6,6,6,2,1

kategorie = ["Jedynki", "Dwójki", "Trójki", "Czwórki", "Piątki", "Szóstki"]
punkty = ['','','','','','']



def rzuc_koscmi(numery_kosci:str): #45
    for i in numery_kosci:
        index = int(i) - 1
        kosci[index] = random.randint(1,6)


def pokaz_kosci():
    print("_____________")
    for i in range(len(kosci)): #range(5)  #0 1 2 3 4
        print(f'   {i+1}. {kosci[i]}')
    print("_____________")

#TEST
# pokaz_kosci()
# rzuc_koscmi("12345")
# pokaz_kosci()

def sprawdz_czy_przerzucamy() -> bool:
    odp = input("Czy chcesz przerzucić któreś z kości? (t/n)").lower()
    if odp == 't':
        return True
    elif odp == 'n':
        return False
    else:
        print("Proszę podać poprawne dane.")
        sprawdz_czy_przerzucamy()


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
    


def punkty_w_szkole(pole: int):
    liczba_punktów = 0
    for kosc in kosci:
        if kosc == pole:
            liczba_punktów += kosc
    punkty[pole-1] = liczba_punktów



def wstaw_punkty():
    pole = int(input("Gdzie chcesz wpisać punkty? (Podaj numer wubryki): "))
    if punkty[pole-1] == '':
        if 1 <= pole <= 6:
            punkty_w_szkole(pole)
        else:
            print("Wybrane pole jest już uzupełnione.")
            wstaw_punkty()




pokaz_tabele_punktow()

for tura in range(len(kategorie)):
    print("Pierwszy rzut w turze: ")
    rzuc_koscmi("12345")
    pokaz_kosci()
    for i in range(2):
        przerzut = sprawdz_czy_przerzucamy()
        if przerzut:
            kosc_do_przerzutu = input("Które kości chcesz przerzucić? (Podaj numery bez spacji): ")
            rzuc_koscmi(kosc_do_przerzutu)
            pokaz_kosci()
        else:
            break 
    pokaz_tabele_punktow()
    pokaz_kosci()
    wstaw_punkty()
    pokaz_tabele_punktow()

print(f'Twój łączny wynik to: {sum(punkty)}')
