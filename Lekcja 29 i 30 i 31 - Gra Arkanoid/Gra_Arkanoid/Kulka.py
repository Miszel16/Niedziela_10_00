import pygame
import random

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800


# czym jest wektor?
# - ma kierunek (w którą stonę coś się porusza)
# - ma długość (jak szybko się coś porusza)

# "Idź w tę stronę z taką prędkością"
#vector 
vec = pygame.math.Vector2 # 2D (x, y)
predkosc = 15

class Kulka(pygame.sprite.Sprite):
    def __init__(self): 
        super(Kulka, self).__init__()
        self.obraz = pygame.image.load("images/ball.png") # image, surface, rect
        self.zresetuj_pozycje() # napiszemy zaraz
        self.r = 16
        self.przegrana = False # czy kulka spadła na dół ekranu (flaga)


    def zresetuj_pozycje(self):
        self.wspolrzedne = vec(SZEROKOSC_EKRANU/2, WYSOKOSC_EKRANU-140)
        self.rect = self.obraz.get_rect(center=self.wspolrzedne)

        self.wektor = vec(0, -predkosc) # wektor przesunięcia
        self.kat_nachylenia = random.randrange(-30, 30) # pod jakim kątem poleci kulka

        self.wektor.rotate_ip(self.kat_nachylenia)
        self.przegrana = False
    

    def aktualizuj(self, platforma):
        # przesuwaie się kulki o 15 pikseli/klatke w wyznaczonym kierunku (wektor)
        self.wspolrzedne += self.wektor 
        self.rect.center = self.wspolrzedne
        self.sprawdz_kolizje(platforma) #!!!!!!!!!!!!!!!!

    
    def sprawdz_kolizje(self, platforma):
        # krawedzie ekranu
        # lewa krawędź
        if self.rect.left <= 0:
            self.wektor.x *= -1 # zmiana kierunku

        # prawa krawędź
        if self.rect.right >= SZEROKOSC_EKRANU:
            self.wektor.x *= -1

        # górna krawędź
        if self.rect.top <= 0:
            self.wektor.y *= -1
        
        # dolna krawędź
        if self.rect.bottom >= WYSOKOSC_EKRANU:
            self.przegrana = True

        # platforma
        if self.rect.colliderect(platforma.rect): # jeśli dotknie platformy
            # zmiana zwrotu
            self.wektor.y *= -1
            # kąt odbicia i prędkosci kulki
            self.wektor.x += platforma.porusza_sie*5
            
            # jeden kierunek (góra)
            if self.wektor.x < -predkosc:
                self.wektor.x = -15

            # drugi kierunek (dół)
            if self.wektor.x > predkosc:
                self.wektor.x = 15
