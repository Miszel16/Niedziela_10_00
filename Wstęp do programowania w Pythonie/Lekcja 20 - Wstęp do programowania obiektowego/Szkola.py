#nazwa klasy: Przedmiot
class Sigmy():
    #Atrybuty
    # oceny = []

    #metody
    def stworz_liste(self):
        self.oceny = []
    
    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)
    
    def wyswietl_oceny(self):
        print(f"Lista ocen: {self.oceny}")


matematyka = Sigmy()
matematyka.stworz_liste()
matematyka.dodaj_ocene(6)
matematyka.dodaj_ocene(6)
matematyka.dodaj_ocene(6)

informatyka = Sigmy()
informatyka.stworz_liste()
informatyka.dodaj_ocene(6)
informatyka.dodaj_ocene(5)
informatyka.dodaj_ocene(6)

matematyka.wyswietl_oceny()
informatyka.wyswietl_oceny()