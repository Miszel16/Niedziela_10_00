# Funkcje bankomatu:
# - logowanie (karta i PIN)
# - wypłata
# - wpłata
# - zobaczyć stan konta

# Etap 1
# - wypłata
# - wpłata
# - zobaczyć stan konta


def menu_glowne():
    print("Wybierz opcje: ")
    print("1. Wpłata")
    print("2. Wypłata")
    print("3. Sprawdzenie stanu konta")
    print("4. Zakończ")


def pobierz_wybor_klienta():
    return int(input("Podaj numer wybranej opcji: "))


def pobierz_kwote(tekst):
    return float(input(tekst))


# Wpłata
# - pobiera gotówke (+)
# - zabezpieczenie przed wpłatą ujemnej ilośći gotówki (+)
# - dodanie do salda (+)
# - wyświelenie salda po transakcji 

def pokaz_stan_konta(saldo):
    print(f"Stan konta wynosi {saldo} złotych")


def wplata(saldo):
    kwota_wplaty = pobierz_kwote("Ile chcesz wpłacić?: ")
    while kwota_wplaty <= 0:
        print("Niepoprawne dane")
        kwota_wplaty = pobierz_kwote("Ile chcesz wpłacić?: ")

    saldo = saldo + kwota_wplaty
    print(f"Wpłacono {kwota_wplaty} złotych")
    pokaz_stan_konta(saldo)
    return saldo


# Wypłata
# - pobranie kwoty
#   - mnijesza/równa niż saldo
#   - dodatnia
# - odjęcie od salda
# - wyświelenie salda po transakcji 

def wyplata(saldo):
    kwota_wyplaty = pobierz_kwote("Ile chcesz wypłacić?: ")
    while kwota_wyplaty <= 0:
        print("Niepoprawne dane")
        kwota_wyplaty = pobierz_kwote("Ile chcesz wypłacić?: ")
    
    if kwota_wyplaty <= saldo:
        saldo = saldo - kwota_wyplaty
        print(f"Wypłacono {kwota_wyplaty} złotych")
        pokaz_stan_konta(saldo)
    else:
        print("Brak środków na koncie")

    return saldo


# Etap 2 - Karta i PIN
# - sprawdzanie poprawnościu wpisanejj karty i PINU
# - poprosić o podanie danych
# - weryfikacja

def pobierz_dane(dana):
    return input(f"Podaj numer {dana}: ")


def sprawdz_zgodnosc_danych(baza, pobrane) -> bool:
    return baza == pobrane


KARTA = "0001"
PIN = "1234"
saldo = 0
wybor = 0 #None

pobrana_karta = pobierz_dane("karta")
pobrany_pin = pobierz_dane("PIN")



if sprawdz_zgodnosc_danych(KARTA, pobrana_karta) and sprawdz_zgodnosc_danych(PIN, pobrany_pin):
    while wybor != 4:
        menu_glowne()
        wybor = pobierz_wybor_klienta()

        if wybor == 1:
            #wpłata
            saldo = wplata(saldo)
            pass
        elif wybor == 2:
            #wypłata
            saldo = wyplata(saldo)
            pass
        elif wybor == 3:
            #stan konta
            pokaz_stan_konta(saldo)
            pass
        elif wybor == 4:
            #zakończ
            print("Wyłączanie bankomatu")
            pass
        else:
            print("Niepoprawne dane")
            pass
        pass
else:
    print("Błąd logowania")
