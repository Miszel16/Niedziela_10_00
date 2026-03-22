# Najlepiej sprawdzić instalację przed kazdymi zajęciami!
# # python -m pip install pygame

# Link do grafik: 
# https://drive.google.com/drive/folders/1XL7yD6J1TFTIHzx9kZtD43VT1aNHUV9G
import os
os.chdir(os.path.dirname(__file__))

import pygame
import Elementy
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

background = pygame.image.load("Images/background.png")
body_base = pygame.image.load("Images/base.png")
screen_surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

czcionka = pygame.font.SysFont("Comis Sans MS", 30) #!!!!!!

def wypisz_tekst(screen_surface, tekst, pozycja):
    napis = czcionka.render(tekst, False, (255,255,255))
    screen_surface.blit(napis, pozycja)


#                  plik      klasa
nakrycie_glowy = Elementy.NakrycieGlowy()
ubranie = Elementy.Ubranie()
oczy = Elementy.Oczy()
bron = Elementy.Bron()



game_status = True
while game_status:
    events = pygame.event.get()

    for event in events: #iterowanie po wydarzeniach
        if event.type == pygame.QUIT:
            game_status = False
        
        # Sterowanie
        # Q - nakrycie głowy,
        # W - oczy
        # E - ubranie
        # R - bron
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                nakrycie_glowy.wybierzNastepny()
            if event.key == pygame.K_w:
                oczy.wybierzNastepny()
            if event.key == pygame.K_e:
                ubranie.wybierzNastepny()
            if event.key == pygame.K_r:
                bron.wybierzNastepny()

    
    screen_surface.blit(background, (0,0))
    screen_surface.blit(body_base, (270, 130))
    screen_surface.blit(nakrycie_glowy.wybranyObraz(), (270, 130))
    screen_surface.blit(ubranie.wybranyObraz(), (270, 130))
    screen_surface.blit(oczy.wybranyObraz(), (270, 130))
    screen_surface.blit(bron.wybranyObraz(), (270, 130))

    # sterowanie
    wypisz_tekst(screen_surface, f"[Q] Nakrycie głowy: {nakrycie_glowy.wybrany + 1}/3", (100, 100))
    wypisz_tekst(screen_surface, f"[W] Oczy: {oczy.wybrany + 1}/3", (100, 140))
    wypisz_tekst(screen_surface, f"[E] Ubranie: {ubranie.wybrany + 1}/3", (100, 180))
    wypisz_tekst(screen_surface, f"[R] Broń: {bron.wybrany + 1}/3", (100, 220))


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
    
