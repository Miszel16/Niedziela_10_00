# Gra Arkanoid - pokaz gotowego projektu
# grafiki: 
# https://drive.google.com/drive/folders/16fuwuD8Fmd3M_Uq5xATWO16AUvNRu_eM
# - prezentacja króków działania projektu

# ETAP I:
# - szablon aplikacji z tłem 
# - sterowanie platformą
import os
os.chdir(os.path.dirname(__file__))
from Platforma import Platforma # !!!!!!!!!!
import pygame
pygame.init()

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load('images/background.png')

platforma = Platforma() # !!!!!!!!


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

    ekran.blit(obraz_tla, (0,0))
    ekran.blit(platforma.obraz, platforma.rect)

    pygame.display.flip() # odświeżanie ekranu
    zegar.tick(30)

pygame.quit()
quit()
