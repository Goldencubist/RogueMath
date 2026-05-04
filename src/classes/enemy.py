from math import atan2, cos, sin
import random

from golden_utils import true, false

class enemy:
    def __init__(self, maxhealth):
        self.x, self.y = random.choice(((0,0), (0, 650), (650, 650), (650, 0)))
        self.hp = random.randint(max(1, maxhealth - 49), maxhealth + 1)
        self.alive = true
        self.coins_at_death = max(self.hp / 10, 1)
        self.iticks = 0

    def movement(self, player):
        px, py = player.x, player.y
        dx = (px - 15) - self.x
        dy = (py - 15) - self.y
        an = atan2(dy, dx)
        self.x += cos(an)
        self.y += sin(an)

    def die(self, player):
        self.alive = false; player.coins += 1; player.kills += 1

