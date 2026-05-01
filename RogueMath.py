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
from src.utils.kerneldefs import initialization, GET_OUT, rsave, wsave, music, music_s, collide
from src.classes.enemy import enemy

sys.stdout = open(os.path.join(".RogueMath_data", "log"), "w", encoding="utf-8")
sys.stderr = open(os.path.join(".RogueMath_data", "error_log"), "w", encoding="utf-8")
music_s()

tamanho_tela, tela, tela_atual, jogando, tempo = initialization()
pygame.mouse.set_visible(false)
player = rsave()
player.lastshot = 0
enemy_delay = random.randint(1500, 4000)
last_enemy = 0
balas, inimigos = [], []

while jogando:
    eventos = pygame.event.get()
    Now = pygame.time.get_ticks()
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
        player.movement()
        if len(balas) + len(inimigos) > 0:
            for inimigo in inimigos:
                if inimigo.hp < 1: inimigo.die(player)
                for bala in balas:
                    if collide(inimigo.x, inimigo.y, 30, bala.x, bala.y, 4): bala.hit(player, inimigo)
        if len(balas) != 0:
            for bala in balas: bala.movement()
        if len(inimigos) != 0:
            for inimigo in inimigos:
                inimigo.movement(player)
        if Now - last_enemy >= enemy_delay:
            inimigos.append(enemy(player.kills))
            last_enemy = Now
            enemy_delay = random.randint(1500, 4000)
        balas = [b for b in balas if b.inbounds and bala.perfsleft > 0]
        inimigos = [i for i in inimigos if i.alive]
    else:
        inimigos = []
        player.kills = 0
        player.x, player.y = 325, 325
    draw(tela_atual, tela, tamanho_tela, player, balas, inimigos)
    print(tela_atual)
    tempo.tick(30)

wsave(player)
GET_OUT()
