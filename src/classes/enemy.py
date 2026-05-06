from math import atan2, cos, sin
import random

from golden_utils import true, false

from src.fonts.fonts import fonteinimigo

class enemy:
    def __init__(self, maxhealth):
        self.x, self.y = random.choice(((0,0), (0, 650), (650, 650), (650, 0)))
        self.hp = random.randint(max(1, maxhealth - 49), maxhealth + 1)
        self.font = fonteinimigo
        self.image = self.font.render(f"{self.hp}", false, (255, 0, 0))
        self.alive = true
        self.coins_at_death = max(self.hp / 10, 1)
        self.width, self.height = self.image.get_width(), self.image.get_height()

    def movement(self, player):
        px, py = player.x, player.y
        dx = px - self.x
        dy = py - self.y
        an = atan2(dy, dx)
        self.x += cos(an)
        self.y += sin(an)

    def die(self, player):
        self.alive = false; player.coins += 1; player.kills += 1

