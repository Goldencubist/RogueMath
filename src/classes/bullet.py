from golden_utils import true, false, none

class bullet:
    def __init__(self, x, y, speedx, speedy, perfs):
        self.x = x
        self.y = y
        self.sx = speedx
        self.sy = speedy
        self.inbounds = true
        self.perfsleft = perfs
        self.hitten = []
    
    def movement(self):
        self.x += self.sx
        self.y += self.sy
        if self.x >= 649 or self.x <= 4 or self.y >= 649 or self.y <= 4:
            self.inbounds = false

    def hit(self, player, enemy):
        self.hitten.append(enemy)
        enemy.hp -= player.base_damage
        enemy.image = enemy.font.render(f"{enemy.hp}", false, (255, 0, 0))
        enemy.width, enemy.height = enemy.image.get_width(), enemy.image.get_height()
        self.perfsleft -= 1

