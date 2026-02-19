import pygame

from golden_utils import true, false, none
from src.fonts.fonts import fontetítulo

textotítulo = fontetítulo.render("RogueMath", false, (255, 255, 255))

def draw(tela_atual, tela, tamanho_tela, player):
    mousepos = pygame.mouse.get_pos()
    match tela_atual:
        case "menu":
            tela.fill((0, 0, 0))
            tela.blit(textotítulo, (tamanho_tela/2 - textotítulo.get_width()/2, tamanho_tela/2 - textotítulo.get_height()/2))
        case "gameplay":
            tela.fill((255, 255, 0))
            pygame.draw.rect(tela, (255, 255, 0), (player.posx - 30, player.posy - 30, 30, 30))
            pygame.draw.rect(tela, (0, 0, 0), (player.posx - 30, player.posy - 30, 30, 30), 3)
        case _:
            tela.fill((103, 55, 192))
    pygame.draw.circle(tela, (255, 255, 255), mousepos, 4)
    pygame.draw.circle(tela, (0, 0, 0), mousepos, 5, 1)
    pygame.display.flip()
