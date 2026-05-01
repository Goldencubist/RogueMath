from golden_utils import true, false, none

class bullet:
    def __init__(self, x, y, speedx, speedy, perfs):
        self.x = x
        self.y = y
        self.sx = speedx
        self.sy = speedy
        self.inbounds = true
        self.perfsleft = perfs
    
    def movement(self):
        self.x += self.sx
        self.y += self.sy
        if self.x >= 649 or self.x <= 4 or self.y >= 649 or self.y <= 4:
            self.inbounds = false

    def hit(self, player, enemy):
        enemy.hp -= player.base_damage
        self.perfsleft -= 1

