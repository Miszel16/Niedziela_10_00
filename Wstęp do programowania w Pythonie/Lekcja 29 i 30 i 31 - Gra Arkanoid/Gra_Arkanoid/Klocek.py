import pygame
import copy

class Klocek(pygame.sprite.Sprite): # klasa nadrzędna
    def __init__(self, x, y, hp_klocka):
        super(Klocek, self).__init__()
        # image surface rect
        self.obraz_oryginalny = pygame.image.load('images/brick.png')
        self.rect = pygame.Rect(x, y, 96, 48)
        self.hp_klocka = hp_klocka # 1, 2, 3
    
    def aktualizuj(self):
        maska_z_kolorem = 0
        if self.hp_klocka == 3:
            maska_z_kolorem = (128, 0, 0) # czerwone
        if self.hp_klocka == 2:
            maska_z_kolorem = (0, 128, 0) # zielone
        if self.hp_klocka == 1:
            maska_z_kolorem = (0, 0, 128) # niebieskie
        self.obraz = copy.copy(self.obraz_oryginalny)
        self.obraz.fill(maska_z_kolorem, special_flags=pygame.BLEND_ADD)
    
    # metoda do zarządzania grupą
    def update(self):
        self.aktualizuj()
    
    def uderzenie(self):
        self.hp_klocka -= 1
        if self.hp_klocka <= 0:
            self.kill()


