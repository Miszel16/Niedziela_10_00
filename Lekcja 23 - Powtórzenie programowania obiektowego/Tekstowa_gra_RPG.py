#QUIZ
# https://quiz.giganciprogramowania.edu.pl/wdp-python2-q1

# PRZYPOMINAJKA:
# 1. Jak zbudowana jest deklaracja funkcji?

# 2. Jak działa funkcja range()?
#     - start, 
#     - stop,
#     - step,


# 3. Pętle
#     - jakie są rodzaje?
#     - jak napisać pętle?
#     - pętla nieskończona


# 4. Czym jest klasa i obiekt?
#     - jak napisać klasę/obiekt?
#     - czym jest konstruktor?
#     - czym jest dziedziczenie?


# TEKSTOWA GRA RPG
# PLAN
# - import random +
# - klasa bazowa: Postac +
#   - konstruktor nazwa, życie, max_życie +
#   - metoda atakuj (losowe obrażenia) +

# - klasa pochodna z Postac: Potwor +
#   - konstruktor [zombie, szkielet, creeper, enderman, boss*] +

# - klasa pochodna z Postac: Gracz
#   - konstruktor
#   - metoda odpocznij (regeneracja życia)
#   - metoda walki 

# - pętla gry

from random import randint, choice

# KLASA BAZOWA
class Postac():
    def __init__(self, nazwa:str, zycie:int):
        self.nazwa = nazwa
        self.zycie = zycie
        self.max_zycie = zycie
    

    def atakuj(self, przeciwnik: "Postac"):
        atak = randint(0, 3)

        if atak == 0:
            print(f"{przeciwnik.nazwa} unika ataku {self.nazwa}.")
        else:
            print(f"{self.nazwa} atakuje {przeciwnik.nazwa}, zadając {atak} obrażeń.")
            przeciwnik.zycie -= atak


class Potwor(Postac):
    def __init__(self, gracz:"Gracz"):
        nazwa = choice(["zombie", "szkielet", "creeper", "enderman"])
        zycie = randint(1, gracz.max_zycie)
        super().__init__(nazwa, zycie)


class Gracz(Postac):
    def __init__(self):
        nazwa = input("Podaj nazwę gracza: ")
        super().__init__(nazwa, 10)
    

    def odpocznij(self):
        if self.zycie < self.max_zycie:
            self.zycie += 1
        print(f"{self.nazwa} odpoczywa, aktualne życie: {self.zycie}/{self.max_zycie}")
    

    def walka(self, przeciwnik:"Potwor") -> bool:
        walka = True
        while walka:
            print()
            print(f"życie {self.nazwa}: {self.zycie}")
            print(f"życie {przeciwnik.nazwa}: {przeciwnik.zycie}")

            akcja_walki = input("Akcja (atak/uciekaj): ")

            if akcja_walki == "atak":
                self.atakuj(przeciwnik)
                if przeciwnik.zycie <= 0:
                    print(f"{self.nazwa} zabija {przeciwnik.nazwa}")
                    return True # przeżyliśmy 
                przeciwnik.atakuj(self)
            
            elif akcja_walki == "uciekaj":
                print(f"{self.nazwa} ucieka")
                przeciwnik.atakuj(self)
                print(f"życie {self.nazwa}: {self.zycie}")
                walka = False
            
            else:
                print("Nieznana akcja")

            if self.zycie <= 0:
                print(f"{self.nazwa} ginie przez {przeciwnik.nazwa}")
                return False # nie przeżyliśmy

gracz = Gracz()
gra = True
while gra:
    akcja = input("Akcja (zwiedzaj/odpocznij): ")

    if akcja == "zwiedzaj":
        if randint(0,1) == 0:
            print(f"{gracz.nazwa} znalazł jaskinię!")
        else:
            potwor = Potwor(gracz)
            print(f"{gracz.nazwa} napotyka na {potwor.nazwa}")
            gra = gracz.walka(potwor)
    elif akcja == "odpocznij":
        gracz.odpocznij()
    else:
        print("Nieznana akcja")