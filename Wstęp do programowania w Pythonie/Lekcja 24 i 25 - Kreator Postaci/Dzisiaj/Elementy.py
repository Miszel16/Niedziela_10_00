import pygame

#1. Klasa pomocnicza [image, surface, rect]
class Obraz():
    def __init__(self, path):
        self.obraz = pygame.image.load(path).convert_alpha()


# 2. Klasa bazowa (Element)
class Element():
    def __init__(self, typ):
        self.wybrany = 0 
        self.lista_obrazow = [] #0,1,2

        for i in range(1, 4): #1,2,3
            sciezka = f"Images/{typ}{i}.png"
            wczytany_obraz = Obraz(sciezka)
            self.lista_obrazow.append(wczytany_obraz)
        
    def wybierzNastepny(self):
        self.wybrany += 1
        if self.wybrany > len(self.lista_obrazow)-1:
            self.wybrany = 0
    
    def wybranyObraz(self):
        return self.lista_obrazow[self.wybrany].obraz


# 3. Klasy pochodne
class NakrycieGlowy(Element):
    def __init__(self):
        super().__init__("head") # konstruktor klasy bazowej


class Ubranie(Element):
    def __init__(self):
        super().__init__("body")


class Oczy(Element):
    def __init__(self):
        super().__init__("eye")


class Bron(Element):
    def __init__(self):
        super().__init__("weapon")
