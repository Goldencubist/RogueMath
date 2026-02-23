import pygame

from golden_utils import true, false, none

from src.classes.bullet import bullet

class player:
    def __init__(self):
        self.x = 325
        self.y = 325
        self.coins = 0
        self.speed = 1

    def movement(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] and self.y >= 31:
            self.y -= 1
        if teclas[pygame.K_a] and self.x >= 31:
            self.x -= 1
        if teclas[pygame.K_s] and self.y <= 649:
            self.y += 1
        if teclas[pygame.K_d] and self.x <= 649:
            self.x += 1

    def shoot(self):
        return bullet(self.x, self.y, 1, 1)
