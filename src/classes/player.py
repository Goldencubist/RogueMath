import pygame

from golden_utils import true, false, none

class player:
    def __init__(self):
        self.posx = 325
        self.posy = 325
        self.coins = 0
        self.speed = 1

    def movement(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] and self.posy >= 31:
            self.posy -= 1
        if teclas[pygame.K_a] and self.posx >= 31:
            self.posx -= 1
        if teclas[pygame.K_s] and self.posy <= 619:
            self.posy += 1
        if teclas[pygame.K_d] and self.posx <= 619:
            self.posx += 1
