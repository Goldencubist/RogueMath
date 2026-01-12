import pygame
import pickle
import sys
import os

def initialization():
    pygame.init()
    pygame.font.init()
    tamanho_tela = 700
    tela = pygame.display.set_mode((tamanho_tela, tamanho_tela))
    pygame.display.set_caption("RogueMath")
    return tamanho_tela, tela, "menu", True, pygame.time.Clock()

def GET_OUT():
    pygame.quit()
    sys.exit()


