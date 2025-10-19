import pygame
from Direction import Direction

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        # oryginalny obraz
        self.original_image = pygame.image.load("images/head.png")
        # obraz pomocniczy do zmiany kierunku 
        self.image = pygame.transform.rotate(self.original_image, 0)
        self.rect = self.image.get_rect(center=(12*32 + 16, 9*32 + 16))
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.direction = Direction.UP # obecny kierunek
        self.new_direction = Direction.UP # gotowy do wprowadzenia




    def change_direction(self, direction):
        is_possible = True
        if self.direction == Direction.UP and direction == Direction.DOWN:
            is_possible = False
        if self.direction == Direction.DOWN and direction == Direction.UP:
            is_possible = False
        if self.direction == Direction.RIGHT and direction == Direction.LEFT:
            is_possible = False
        if self.direction == Direction.LEFT and direction == Direction.RIGHT:
            is_possible = False
        if is_possible:
            self.new_direction = direction
    

    def update(self):
        self.direction = self.new_direction
        self.image = pygame.transform.rotate(self.original_image, (self.direction.value*90))

        if self.direction == Direction.UP:
            self.rect.move_ip(0, -32)
        if self.direction == Direction.RIGHT:
            self.rect.move_ip(32, 0)
        if self.direction == Direction.LEFT:
            self.rect.move_ip(-32, 0)
        if self.direction == Direction.DOWN:
            self.rect.move_ip(0, 32)
        
        