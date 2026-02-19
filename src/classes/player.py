import pygame

from golden_utils import true, false, none

class player:
    def __init__(self):
        self.posx = 350
        self.posy = 350
        self.coins = 0
        self.speed = 1

    def movement(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w]:
            self.posy -= 1
        if teclas[pygame.K_a]:
            self.posx -= 1
        if teclas[pygame.K_s]:
            self.posy += 1
        if teclas[pygame.K_d]:
            self.posx += 1
