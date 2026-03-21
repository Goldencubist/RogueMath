from math import atan2, cos, sin
import random

class enemy:
    def __init__(self):
        self.x, self.y = random.choice(((0,0), (0, 650), (650, 650), (650, 0)))
        self.hp = 1
    def movement(self, player):
        px, py = player.x, player.y
        dx = (px - 15) - self.x
        dy = (py - 15) - self.y
        an = atan2(dy, dx)
        self.x += cos(an)
        self.y += sin(an)

