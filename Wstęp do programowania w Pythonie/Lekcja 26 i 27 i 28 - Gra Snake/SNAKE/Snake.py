import pygame
from Direction import Direction
import copy
from Segment import Segment


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        self.original_image = pygame.image.load("images/head.png")
        self.image = pygame.transform.rotate(self.original_image, 0)
        self.rect = self.image.get_rect(center=(12*32 + 16, 9*32 + 16))
        self.direction = Direction.UP
        self.new_direction = Direction.UP
        self.last_position = self.rect 
        self.add_segment = False # flaga
        self.segments = [] # lista ze wszytskimi segmentami


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

        self.last_position = copy.deepcopy(self.rect)
        if self.direction == Direction.UP:
            self.rect.move_ip(0, -32)
        if self.direction == Direction.RIGHT:
            self.rect.move_ip(32, 0)
        if self.direction == Direction.LEFT:
            self.rect.move_ip(-32, 0)
        if self.direction == Direction.DOWN:
            self.rect.move_ip(0, 32)

        #poruszanie
        for i in range(len(self.segments)):
            if i==0:
                #ostatnia pozycja głowy
                self.segments[i].move(self.last_position)
            else:
                self.segments[i].move(self.segments[i-1].last_position)
        
        #dodawanie nowego segmentu
        if self.add_segment:
            new_segment = Segment()

            new_position = None

            if len(self.segments)>0:
                new_position = copy.deepcopy(self.segments[-1].position)
            else:
                new_position = copy.deepcopy(self.last_position)
            
            new_segment.position = new_position
            self.segments.append(new_segment)
            self.add_segment = False
    

    def draw_segments(self, screen):
        for segment in self.segments:
            screen.blit(segment.image, segment.position)
    

    def eat_apple(self):
        self.add_segment = True
    
# ---------------------------------------- kolizja ze ścianami oraz z ogonem węża -------------
    def detect_collision(self):
        # ugryzienie ogona
        # jeśli głowa węża będzie miec kolizję z którąkolwiek cześcią ogona -> przegrana
        for segment in self.segments:
            #topleft - zwraca współrzędne lewego górnego roku prostokąta
            if self.rect.topleft == segment.position.topleft:
               return True
       
        # wyjście poza ekran
        # jesli wąż będzie znajdować się poza granicami ekranu -> przegrana
        if self.rect.top < 0 or self.rect.top >= 608:
            return True
        if self.rect.left < 0 or self.rect.left >= 800:
            return True
        return False
# ---------------------------------------------------------------------------------------------