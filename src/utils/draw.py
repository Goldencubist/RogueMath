import pygame

from golden_utils import true, false, none
from src.fonts.fonts import fontetítulo

textotítulo = fontetítulo.render("RogueMath", false, (255, 255, 255))

def draw(tela_atual, tela, tamanho_tela):
    match tela_atual:
        case "menu":
            tela.fill((0, 0, 0))
            tela.blit(textotítulo, (tamanho_tela/2 - textotítulo.get_width()/2, tamanho_tela/2 - textotítulo.get_height()/2))
        case _:
            tela.fill((103, 55, 192))
    pygame.display.flip()
