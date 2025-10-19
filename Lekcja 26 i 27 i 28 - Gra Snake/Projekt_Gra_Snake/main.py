# 1. SNAKE III (2005) na telefonie NOKIA
# 2. Prezentacja
# 3. Nasz projekt docelowy

# GRAFIKI: https://drive.google.com/drive/folders/1qyu5_Kfb7YEJkNOJWXns0lrbWvz9Ohmw
#----------------------------------------------------------------------------------
import os
os.chdir(os.path.dirname(__file__))
import pygame
import random
import time
# nazwa pliku    nazwa klasy
from Apple import Apple
from Direction import Direction
from Snake import Snake
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 608

# 25 x 19 kafelków
background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
# 32 x 32 pixele
for i in range(25): # 0 - 24
    for j in range(19): # 0 - 18
        image = pygame.image.load("images/background.png")
        # R G B 
        mask = (random.randrange(0, 20), random.randrange(0, 20), random.randrange(0, 20))
        image.fill(mask, special_flags=pygame.BLEND_ADD)
        background.blit(image, (i*32,j*32))


screen_surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock =pygame.time.Clock()


apple = Apple() 
apple_group = pygame.sprite.Group()
apple_group.add(apple)


snake = Snake()
# tworzymy nowe zdarzenie
MOVE_THE_SNAKE = pygame.USEREVENT + 1
# uruchamiamy je co 200 ms
pygame.time.set_timer(MOVE_THE_SNAKE, 200)



# PĘTLA GRY
game_status = True
while game_status:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game_status = False
        pass

    screen_surface.blit(background, (0,0)) # wyświetlanie tła

    for apple in apple_group:
        screen_surface.blit(apple.image, apple.rect)
    
    screen_surface.blit(snake.image, snake.rect)


    pygame.display.flip() # pełen odświeżenie całego ekranu
    clock.tick(30)
    pass

time.sleep(3)
pygame.quit()
quit()
