import random
import os
import colorama
colorama.init()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def rysuj_plansze(plansza: list) -> None:
    for wiersz in plansza:
        line = "["
        for i, znak in enumerate(wiersz):
            if znak == 'x':
                znak_kolor = colorama.Fore.BLUE + znak + colorama.Style.RESET_ALL
                line += f' {znak_kolor} '
            elif znak == 'o':
                znak_kolor = colorama.Fore.RED + znak + colorama.Style.RESET_ALL
                line += f' {znak_kolor} '
            else:
                line += (znak).center(3)
            if i < len(wiersz) - 1:
                line += '|'
        print(line + ']')


def dekoduj(znak: str, plansza: list) -> list:
    for i, wiersz in enumerate(plansza):
        for j, znak_w_planszy in enumerate(wiersz):
            if znak_w_planszy == znak:
                return [i, j]


def ruch(plansza: list, pole: str, aktualny_gracz: str) -> list:
    w, k = dekoduj(pole, plansza)
    plansza[w][k] = aktualny_gracz
    return plansza


def pobierz_ruch(aktualny_gracz: str, zaznaczone: list) -> str:
    ruch = input(f"Gracz '{aktualny_gracz}': Podaj nazwę pola, które chcesz zaznaczyć: ")
    while not((ruch not in zaznaczone) and ruch in "abcdefghi"):
        print("Niepoprawny ruch!")
        ruch = input("Podaj poprawne pole:")
    zaznaczone.append(ruch)
    return ruch


def wygrana(aktualny_gracz: str, plansza: list) -> bool:
    for i in plansza:
        if i.count(aktualny_gracz) == 3:
            return True
    for i in range(3):
        if plansza[0][i] == plansza[1][i] == plansza[2][i] == aktualny_gracz:
            return True
    
    if plansza[0][0] == plansza[1][1] == plansza[2][2] == aktualny_gracz:
        return True
    if plansza[0][2] == plansza[1][1] == plansza[2][0] == aktualny_gracz:
        return True
    return False


def zmiana_gracza(aktualny_gracz: str) -> str:
    if aktualny_gracz == 'x':
        return 'o'
    return 'x'


def gra():
    plansza = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]
    brak_wygranej = True
    zaznaczone = []
    rundy = 0
    aktualny_gracz = random.choice(['x', 'o'])

    rysuj_plansze(plansza)
    print(f"Gracz, który rozpoczyna grę to '{aktualny_gracz}'")

    while brak_wygranej:
        pole = pobierz_ruch(aktualny_gracz, zaznaczone)
        rundy += 1
        plansza = ruch(plansza, pole, aktualny_gracz)
        clear_console()
        rysuj_plansze(plansza)

        if wygrana(aktualny_gracz, plansza):
            brak_wygranej = False
            print(f"GRATULACJE! Wygrywa gracz '{aktualny_gracz}'!")
        elif rundy >=9:
            brak_wygranej = False
            print("REMIS")
        aktualny_gracz = zmiana_gracza(aktualny_gracz)


game_status = True
while game_status:
    print("Żeby zagrać wpisz: 'GRAJ'")
    print("Żeby zakończyć wpisz: 'KONIEC'")
    odpowiedz = input("Wpisz: ")

    while odpowiedz not in ("GRAJ", "KONIEC"):
        print("Brak takiej opcji.")
        odpowiedz = input("Wpisz ponownie: ")
    
    if odpowiedz == "GRAJ":
        gra()
    else:
        print("Do zobaczenia.")
        break
    