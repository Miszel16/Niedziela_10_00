import os
os.chdir(os.path.dirname(__file__))
#CEL: zbieranie bonusów z ekranu

import pygame
from random import choice, randint
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pierwsza gra")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   FUNCKJE DO OBRAZÓW ↓
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_image(img_path: str, position):
    image = pygame.image.load(img_path)
    surface = image.convert()

    transparent_color = (0,0,0)
    surface.set_colorkey(transparent_color)

    rect = surface.get_rect(center = position)

    return [image, surface, rect]

def print_image(img_list) -> None: 
    image, surface, rect = img_list
    screen_surface.blit(surface, rect)
    pass

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   PORUSZANIE GRACZA ↓
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def set_position_image(img_list, position):
    image, surface, rect = img_list
    rect = surface.get_rect(center = position)
    return [image, surface, rect]

def calculate_player_movement(keys):
    speed = 10
    delta_x = 0
    delta_y = 0
    
    if keys[pygame.K_LSHIFT]:
        speed *= 2
    if keys[pygame.K_w]:
        delta_y -= speed
    if keys[pygame.K_s]:
        delta_y += speed
    if keys[pygame.K_d]:
        delta_x += speed
    if keys[pygame.K_a]:
        delta_x -= speed
    return [delta_x, delta_y]

def limit_position(position): 
    x, y = position
    x = max(0, min(x, SCREEN_WIDTH))
    y = max(0, min(y, SCREEN_HEIGHT))
    return [x, y]





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   OBIEKTY BONUSOWE ↓
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ◆ Utworzenie listy grafik bonusowych
# ◆ Utworzenie obiektów bonusowych - obiekty gotowe do wstawienia [image, surface, rect]

# ◆ FUNCJA DO PRZYGOTOWANIA OBIEKTÓW:
# ◆ dodanie na samej górze: "from random import choice, randint"
def generate_bonus_object():
    # Losuje nazwę obrazka bonusowego z listy grafik
    image_name = choice(bonus_images)

    # Losuje współrzędne
    x = randint(0, SCREEN_WIDTH)
    y = randint(0, SCREEN_HEIGHT)
    # Tworzy listę z wylosowaną pozycją
    position = [x, y]
    # Tworzy gotowy obiekt z [image, surface, rect]
    new_obj = load_image(image_name, position)

    # Dodaje nowo utworzony obiekt bonusowy do listy 'bonus_objects', która przechowuje wszystkie
    # aktywne bonusy w grze (czyli te, które mają być wyświetlone i mogą zostać zebrane).
    bonus_objects.append(new_obj)
    pass

# ◆ FUNKCJA WYŚWIETLAJĄCA OBIEKTY BONUSOWE
def print_bonus_objects():
    for obj in bonus_objects:
        print_image(obj)
        pass
    pass

#-----------------TESTY------------------
# ◆ stworzenie zmiennej FRAMES_PER_SECOND = 60
# ◆ podmiana liczby klatek w clock.tick(FRAMES_PER_SECOND)
# ◆ przygotowanie zmiennej 'frames_cnt = 0', która zlicza wyświetlane klatki
# ◆ zliczamy klatki po 'pygame.display.update()', 'frames_cnt += 1'
# ◆ zmiana formy generowania bonusów na tą z 'if..'

#-----------------TESTY------------------

# ◆ USUWANIE OBIEKTÓW BONUSOWYCH PO DOTKNIĘCIU
def check_collisions():
    # Pobierz prostokąt (rect) gracza z listy 'player'; element [2] to właśnie rect.
    rect_player = player[2]

    # Iteruj po indeksach od końca listy 'bonus_objects' do początku.
    # To ważne, ponieważ usuwanie elementów od końca nie psuje indeksowania listy.
    for i in range(len(bonus_objects)):
        index = len(bonus_objects) - i - 1  # Przeliczanie indeksu na odwrotną kolejność

        # Pobierz obiekt bonusowy o wyliczonym indeksie.
        obj = bonus_objects[index]

        # Pobierz prostokąt (rect) tego obiektu — używany do detekcji kolizji.
        rect = obj[2]

        # Sprawdź, czy prostokąt gracza koliduje z prostokątem bonusu.
        # Funkcja 'colliderect()' zwraca True, jeśli prostokąty się nachodzą.
        if rect.colliderect(rect_player):
            # Jeśli doszło do kolizji, usuń dany obiekt bonusowy z listy.
            # Dzięki temu nie będzie już rysowany ani wykrywany.
            bonus_objects.pop(index)
            pass
        pass
    pass

# ◆ przed 'print_bonus_objects()' dodać 'check_collisions()'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   PĘTLA GRY ↓
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image(r'grafiki\player.png', player_pos)
background_color = [9, 42, 121]

FRAMES_PER_SECOND = 60
frames_cnt = 0

clock = pygame.time.Clock()

#Lista grafik obiektów bonusowych
bonus_images = [
    r'grafiki\bonus_1.png',
    r'grafiki\bonus_2.png',
    r'grafiki\bonus_3.png'
]

bonus_objects = [] #gotowy obiekt to 3-elementowa lista z funkcji load_image

game_status = True

while game_status:
    events = pygame.event.get()
    for event in events:
        #print(event)
        if event.type == pygame.QUIT:
            game_status = False
        pass
    
    #--------------PODSTAWA---------------
    pressed_keys = pygame.key.get_pressed()

    delta_x, delta_y = calculate_player_movement(pressed_keys)
    player_pos[0] += delta_x
    player_pos[1] += delta_y
    
    player_pos = limit_position(player_pos)
    player = set_position_image(player, player_pos)

    screen_surface.fill(background_color)
    #--------------------------------------
    print_image(player)


    #------------ROZSZERZENIE--------------
    # generate_bonus_object()
    # print_bonus_objects()
    #TESTY
    if frames_cnt % (FRAMES_PER_SECOND * 1) == 0: #mnożnik mówi co ile sekund generować
        generate_bonus_object()
        pass
    check_collisions()
    print_bonus_objects()
    #--------------------------------------

    pygame.display.update()
    frames_cnt += 1

    clock.tick(FRAMES_PER_SECOND)
    pass

pygame.quit()
quit()