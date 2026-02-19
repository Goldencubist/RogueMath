import sys
import os

import pygame
from golden_utils import true, false, none, rjson, wjson

from src.utils.states import state_sys, gs
from src.utils.draw import draw
from src.fonts import fonts
from src.utils.kerneldefs import initialization, GET_OUT, rsave, wsave

sys.stdout = open(os.path.join(".RogueMath_data", "log"), "w", encoding="utf-8")
sys.stderr = open(os.path.join(".RogueMath_data", "error_log"), "w", encoding="utf-8")

tamanho_tela, tela, tela_atual, jogando, tempo = initialization()
pygame.mouse.set_visible(false)
player = rsave()

while jogando:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jogando = False
        elif evento.type == pygame.KEYDOWN:
            tela_atual = state_sys(tela_atual)
    if tela_atual == "gameplay":
        player.movement() #type: ignore (isso é pra meu IDE problemático que acha que o rsave vai dar None)
    draw(tela_atual, tela, tamanho_tela, player)
    print(tela_atual)
    tempo.tick(30)

wsave(player)
GET_OUT()
