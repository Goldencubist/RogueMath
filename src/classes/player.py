from math import atan2, cos, sin

import pygame

from golden_utils import true, false, none

from src.classes.bullet import bullet

class player:
    def __init__(self):
        self.x = 325
        self.y = 325
        self.coins = 0
        self.speed = 1
        self.lastshot = 0
        self.delay = 1000
        self.base_damage = 1
        self.perfs = 1
        self.kills = 0

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

    def shoot(self, mousepos):
        now = pygame.time.get_ticks()
        if now - self.lastshot >= self.delay:
            mousex, mousey = mousepos
            dx = mousex - (self.x - 15)
            dy = mousey - (self.y - 15)
            an = atan2(dy, dx)
            sx = cos(an) * 5
            sy = sin(an) * 5
            self.lastshot = now
            return bullet(self.x - 15, self.y - 15, sx, sy, self.perfs)
        else:
            return none

