class Samochod():
    # ATRYBUTY DLA CAŁEJ KLASY
    licznik1 = 0 # zlicza ilość stworzonych obiektów (aut)
    # marka = ""
    # kolor = ""
    # model = ""
    # moc_silnika = 0

    def __init__(self, marka, kolor, model, moc_silnika):
        #ATRYBUTY DLA KAŻDEGO OBIEKTU INDYWIDUALNIE
        print("Utworzono nowy obiekt samochodu.")
        Samochod.licznik1 += 1
        self.licznik2 = 5
        self.marka = marka
        self.kolor = kolor
        self.model = model
        self.moc_silnika = moc_silnika


    def wyswietl(self):
        print(self.marka)
        print(self.kolor)
        print(self.model)
        print(self.moc_silnika)
        print(f"Licznik2: {self.licznik2}")


# auto1 = Samochod()
# auto1.marka = "Volvo"
# auto1.kolor = "Czarny"
# auto1.model = "xc40"
# auto1.moc_silnika = 200

# auto1.wyswietl()

print(Samochod.licznik1) # 0

auto1 = Samochod("Ferrari", "biały", "SF90", 650)
auto1.wyswietl()
print(auto1.licznik2) # 5

print(Samochod.licznik1) # 1

auto2 = Samochod("Lamborgini", "Czerwony", "Huracan", 2200)
auto2.wyswietl()
print(auto2.licznik2) # 5

print(Samochod.licznik1) # 2