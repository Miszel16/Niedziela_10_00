import os  #importuje moduł os, który pozwala pracować z folderami i plikami
os.chdir(os.path.dirname(__file__)) #zmienia bieżący folder roboczy programu na folder, w którym znajduje się ten plik .py
# nie trzeba wtedy podawać pełnych ścieżek dostępu do np. plików graficznych, jesli są w tym samym folderze

import pygame #importuje bibliotekę pygame, żeby można było jej używać
pygame.init() #uruchamia wszystkie potrzebne moduły pygame (np. ekran, dźwięk, itd.)

SCREEN_WIDTH = 800 #szerokość ekranu w pikselach
SCREEN_HEIGHT = 600 #wysokośc ekranu w pikselach

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #tworzy okno gry o podanych rozmiarach
pygame.display.set_caption("Pierwsza gra") #ustawia tytuł okna gry (pokazuje się na górnym pasku okna)

clock = pygame.time.Clock() #Tworzysz zegar, który pozwoli Ci ustawić ile klatek na sekundę będzie miała Twoja gra (czyli jak szybko będzie działać)

game_status = True #zmienna, która mówi, czy gra ma dalej działać. Dopóki jest True, gra trwa

while game_status: #pętla gry
    events = pygame.event.get() #pobiera wszystkie zdarzenia, np. naciśnięcie klawisza, ruch myszy, zamknięcie okna

    for event in events: #przegląd każdego zdarzenia
        print(event) #wypisuje zdarzenie w konsoli
        if event.type == pygame.QUIT: #sprawdza, czy gracz kliknął "X" żeby zamknąć grę
            game_status = False #wyłącza pętlę - kończy grę
        pass

    pygame.display.update() #Odświeża ekran gry – wszystko, co zostało narysowane, pojawia się na ekranie
    clock.tick(60) #Sprawia, że gra działa maksymalnie z prędkością 60 klatek na sekundę – nie za szybko.
    pass

pygame.quit() #wyłącza wszystkie moduły pygame (np. ekran, dźwięk)
quit() #kończy działanie programu Pythona