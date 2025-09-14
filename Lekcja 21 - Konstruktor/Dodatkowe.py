# Zadanie
# Celem zadania jest stworzenie 2 klas: Kolo i Kwadrat.
# Klasy mają być odpowiedzialne za przechowywanie odpowiednich dla danej figury
# geometrycznej wymiarów oraz posiadać metody wyświetlające pole i obwod tych figur.

class Kolo():
    def __init__(self, r):
        self.promien = r


kolo1 = Kolo(4)
kolo2 = Kolo(5)


class Kwadrat():
    def __init__(self, bok):
        self.bok = bok

kwadrat1 = Kwadrat(7)
kwadrat2 = Kwadrat(9)