# KLASA BAZOWA

class Zwierze():
    def __init__(self, wiek, imie):
        self.wiek = wiek
        self.imie = imie
    
    def spij(self):
        print(f"{self.imie} śpi")
    
    def wydaj_dzwiek(self):
        print(f"{self.imie} wydaje dźwięk")



# KLASY DZIEDZICZĄCE PO KLASIE BAZOWEJ "Zwierze"

class Krolik(Zwierze):
    # konstruktor
    def __init__(self, wiek, imie):
        # wywołujemy konstruktor klasy bazowej
        super().__init__(wiek, imie)
        self.dlugosc_uszu_km = 2
    
    def kicaj(self):
        print(f"{self.imie} kica")

    def pokaz_uszy(self):
        print(f"Uszy królika {self.imie} to {self.dlugosc_uszu_km} km")


krolik1 = Krolik(2, "Marcin")
krolik1.wydaj_dzwiek()
krolik1.kicaj()
krolik1.spij()
krolik1.pokaz_uszy()

print()
print()


class Lew(Zwierze):
    def __init__(self, wiek, imie):
        super().__init__(wiek, imie)
        self.kolor_grzywy = "brązowy"
        self.waga = 200

    def zarycz(self):
        print(f"{self.imie} ryczy")
    
    def pokaz_wage(self):
        print(f"{self.imie} waży {self.waga} kg")
    
lew1 = Lew(6, "Mufasa")
lew1.zarycz()
lew1.pokaz_wage()
lew1.spij()


print()
print()
# ZADANIE
# 1. Stworzyć klasę Ptak dziedziczącą po klasie Zwierze, która ma mieć:
#    - konstruktor wywołujkący konstruktor klasy bazowej,
#    - metodę lec()
# 2. Stworzyć kolejną klasę Orzel, dziedziczącą po Ptak, która ma mieć:
#    - konstruktor wywołujkący konstruktor klasy nadrzędnej,
#    - metodę poluj(), w której wywołujemy metodę lec() z klasy nadrzędnej.
# 3. Następnie tworzymy obiekt klasy Orzel i wywołajmy wszystkie metody

# Zwierze -> Ptak -> Orzel
#         -> Krolika
#         -> Pies


# Figura (pole, objetosc) -> Prostokat -> Kwadrat

class Ptak(Zwierze):
    def __init__(self, wiek, imie):
        super().__init__(wiek, imie)
    
    def lec(self):
        print(f"")
