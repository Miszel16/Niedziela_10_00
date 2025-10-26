import pygame
import random

# Sprite
# - klasa wbudowana 
# - lepsza manipulacja obrazkami
# - tworzenie rysowanych obiektów w grze

# klasa - > obiekt

class Apple(pygame.sprite.Sprite):
    # konstruktor tworzy obiekt
    def __init__(self):
        super(Apple, self).__init__()
        # image surface rect
        self.image = pygame.image.load("images/apple.png")
        self.rect = pygame.Rect(random.randint(0, 24)*32, random.randint(0, 18)*32, 32, 32)

        
