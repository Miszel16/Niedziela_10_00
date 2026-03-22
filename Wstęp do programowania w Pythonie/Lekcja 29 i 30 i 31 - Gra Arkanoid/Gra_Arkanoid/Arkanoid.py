# Gra Arkanoid
# grafiki: 
# https://drive.google.com/drive/folders/16fuwuD8Fmd3M_Uq5xATWO16AUvNRu_eM

#!!!!!!!!!!!!!!!!!
# https://quiz.giganciprogramowania.edu.pl/wdp-python2-q3
#!!!!!!!!!!!!!!!!!

# ETAP III:
# - dodanie cegiełek do zbijania i poziomów
# - kolizja kulki z klockami
import os
os.chdir(os.path.dirname(__file__))
from Platforma import Platforma
#     plik          klasa
from Klocek import Klocek # !!!!!!!!!!!!!
from Kulka import Kulka
import pygame
pygame.init()



SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800
Poziom = 0 #!!!!!!!!!!!!!!1
Zycia = 3


ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load('images/background.png')

platforma = Platforma()
kulka = Kulka()

# Poziomy -------------------------------

poziom1 = [
    [0,0,1,1,1,1,1,1,0,0], #1
    [0,1,1,1,1,1,1,1,1,0], #2
    [0,1,1,1,1,1,1,1,1,0], #3
    [0,0,1,1,1,1,1,1,0,0], #4 
    [0,0,0,0,0,0,0,0,0,0], #5
    [0,0,0,0,0,0,0,0,0,0], #6
    [0,0,0,0,0,0,0,0,0,0]  #7
]

poziom2 = [
    [0,0,1,1,0,0,1,1,0,0], #1
    [0,1,2,2,1,1,2,2,1,0], #2
    [0,1,2,2,2,2,2,2,1,0], #3
    [0,0,1,1,2,2,1,1,0,0], #4 
    [0,0,0,0,1,1,0,0,0,0], #5
    [0,0,0,0,0,0,0,0,0,0], #6
    [0,0,0,0,0,0,0,0,0,0]  #7
]

poziom3 = [
    [0,0,3,2,3,1,2,3,2,0], #1
    [0,1,3,2,3,1,2,3,2,0], #2
    [0,1,3,2,3,1,2,3,2,0], #3
    [0,0,3,2,3,1,2,3,2,0], #4 
    [0,0,0,0,0,0,1,2,1,0], #5
    [0,0,0,0,0,0,0,0,0,0], #6
    [0,0,0,0,0,0,0,0,0,0]  #7
]

klocki = pygame.sprite.Group()
def dodaj_klocki():
    wczytany_poziom = None
    if Poziom == 0:
        wczytany_poziom = poziom1
    if Poziom == 1:
        wczytany_poziom = poziom2
    if Poziom == 2:
        wczytany_poziom = poziom3
    
    for i in range(10):
        for j in range(7):
            if wczytany_poziom[j][i] != 0:
                klocek = Klocek(32+i*96, 32+j*48, wczytany_poziom[j][i])
                klocki.add(klocek)

dodaj_klocki()
#----------------------------------------


status_gry = True
while status_gry:
    zdarzenia = pygame.event.get()
    for zdarzenie in zdarzenia:
        if zdarzenie.type == pygame.QUIT:
            status_gry = False
        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                status_gry = False

    # --------- sterowanie-------------
    klawisze = pygame.key.get_pressed() # wszystkie wciśnięte klawisze
    if klawisze[pygame.K_a]:
        platforma.ruszaj_platforma(-1)
    if klawisze[pygame.K_d]:
        platforma.ruszaj_platforma(1)
    # ---------------------------------

    #----------------------------------------------------!!!!!!!
    if len(klocki.sprites()) == 0:
        Poziom += 1
        if Poziom >= 3:
            break
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()
        dodaj_klocki()
    #----------------------------------------------------!!!!!!!!!!

    kulka.aktualizuj(platforma, klocki) #!!!!!!!!!
    # czy przegraliśmy
    if kulka.przegrana:
        Zycia -= 1
        if Zycia <= 0:
            break
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    klocki.update()
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    ekran.blit(obraz_tla, (0,0))

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for klocek in klocki:
        ekran.blit(klocek.obraz, klocek.rect)
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


    ekran.blit(platforma.obraz, platforma.rect)

    #           surface        rect
    ekran.blit(kulka.obraz, kulka.rect)
    # kolizja z krawędziami i platformą

    pygame.display.flip() # odświeżanie ekranu
    zegar.tick(30)

pygame.quit()
quit()
