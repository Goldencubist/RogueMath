import sys
import os
import random
import threading
from time import sleep as sl
from math import atan2, cos, sin

import pygame
from golden_utils import true, false, none, rjson, wjson

from src.utils.states import state_sys, gs
from src.utils.draw import draw
from src.fonts import fonts
from src.utils.kerneldefs import initialization, GET_OUT, rsave, wsave, music, music_s

sys.stdout = open(os.path.join(".RogueMath_data", "log"), "w", encoding="utf-8")
sys.stderr = open(os.path.join(".RogueMath_data", "error_log"), "w", encoding="utf-8")
music_s()

tamanho_tela, tela, tela_atual, jogando, tempo = initialization()
pygame.mouse.set_visible(false)
player = rsave()
player.lastshot = 0
balas = []

while jogando:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jogando = False
        elif evento.type == pygame.KEYDOWN:
            tela_atual = state_sys(tela_atual)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                balanova = player.shoot(pygame.mouse.get_pos())
                if balanova is not None and balanova != none:
                    balas.append(balanova)
    if tela_atual == "gameplay":
        player.movement() #type: ignore (isso é pra meu IDE problemático que acha que o rsave vai dar None)
        if len(balas) != 0:
            for bala in balas:
                bala.movement()
            balas = [b for b in balas if b.inbounds]
    draw(tela_atual, tela, tamanho_tela, player, balas)
    print(tela_atual)
    tempo.tick(30)

wsave(player)
GET_OUT()
