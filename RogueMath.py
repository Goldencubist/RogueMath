import sys
import os

import pygame
from golden_utils import true, false, none, rjson, wjson

from src.utils.states import state_sys, gs
from src.fonts import fonts
from src.utils.kerneldefs import initialization, GET_OUT

sys.stdout = open(os.path.join(".RogueMath_data", "log"), "w", encoding="utf-8")
sys.stderr = open(os.path.join(".RogueMath_data", "error_log"), "w", encoding="utf-8")

tamanho_tela, tela, tela_atual, jogando, tempo = initialization()

while jogando:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jogando = False
        elif evento.type == pygame.KEYDOWN:
            tela_atual = state_sys(tela_atual)
    
    print(tela_atual)
    tela.fill((103, 55, 192))
    pygame.display.flip()
    tempo.tick(30)

GET_OUT()
