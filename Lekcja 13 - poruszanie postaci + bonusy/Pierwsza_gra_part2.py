# ROZGRZEWKA
# Przygotowanie własnej grafiki gracza, np. w paincie. Wymiary 40x40 pikseli
# Przygotowany plik wrzucić do folderu projektu oraz podmienić nazwę wczytywanego
# pliku w kodzie gry.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GRAFIKI
# https://drive.google.com/file/d/1fkajJRymiESpV4i3Yut81VnuNYMIWy4c/view?usp=drive_link

import pygame
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

    return [image, surface, rect] # oryginalny obraz, gotowy do wyśweitlenia, pozycja i rozmiar


def print_image(img_list) -> None: 
    #[image, surface, rect]
    image, surface, rect = img_list
    screen_surface.blit(surface, rect)
    pass

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   PORUSZANIE GRACZA ↓
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#1. Zmiana położenia grafiki

def set_position_image(img_list, position):
    image, surface, rect = img_list
    rect = surface.get_rect(center =  position)
    return [image, surface, rect]

# dodanie do pętli gry wykrywania klawiszy

#2. Reakcja na klawisze

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
    

#3. odświeżanie tła
#4. Ograniczenei wychodzenai poza ekran

# dla x = <0; 800> 800 = SCREEN_WIDTH
# dla y = <0; 600> 600 = SCREEN_HEIGHT

#min(6, 345) -> 6
#max(6, 345) -> 345

def limit_position(position):
    x, y = position
    x = min(x, SCREEN_WIDTH) # zawsze weźmie mniejszą liczbę, czyli (poprawny_x albo 800)
    x = max(0, x) # zawsze weźmie większą liczbę, czyli (0 albo poprawny_x)

    y = max(0, y) #wiemy, że 'y' nie będzie za mały
    y = min(y, SCREEN_HEIGHT) #wiemy, że 'y' nie będzie za duży

    return [x, y]


player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image(r'C:\Users\aplac\Desktop\Projekty Python\Lekcja 12 - pygame - pierwsza aplikacja\grafiki\player.png', player_pos)

background_color = [9, 42, 121]

clock = pygame.time.Clock()
game_status = True

while game_status:
    events = pygame.event.get()
    for event in events:
        print(event)
        if event.type == pygame.QUIT:
            game_status = False
        pass
    
    #odczytywanie wciśniętych klawiszy
    pressed_keys = pygame.key.get_pressed()

    #zmiana współrzędnych
    delta_x, delta_y = calculate_player_movement(pressed_keys)
    player_pos[0] += delta_x
    player_pos[1] += delta_y

    #korygujemy pozycję
    player_pos = limit_position(player_pos)

    player = set_position_image(player, player_pos)

    #odświeżanie tła
    screen_surface.fill(background_color)

    print_image(player)

    pygame.display.update()

    clock.tick(60)
    pass

pygame.quit()
quit()