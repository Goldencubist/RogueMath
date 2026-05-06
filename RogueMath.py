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
            if tela_atual == "gameplay":
                if evento.button == 1:
                    balanova = player.shoot(pygame.mouse.get_pos())
                    if balanova is not None and balanova != none: balas.append(balanova)
            elif tela_atual == "loja":
                if evento.button == 1 and player.coins >= 30 and player.base_damage <= 9:
                    player.base_damage += 1; player.coins -= 30
                elif evento.button == 2 and player.coins >= 10 and player.speed <= 4.9:
                    player.speed *= 10; player.speed += 1; player.speed /= 10; player.coins -= 10
                elif evento.button == 3 and player.coins >= 50 and player.perfs <= 4:
                    player.perfs += 1; player.coins -= 50
    match tela_atual:
        case "gameplay":
            player.movement()
            if player.iticks >= 1: player.iticks -= 1
            if len(balas) + len(inimigos) > 0:
                for inimigo in inimigos:
                    if collide(inimigo.x, inimigo.y, inimigo.width, inimigo.height, player.x, player.y, 30, 30) and player.iticks <= 0:
                        player.hp -= 1; player.iticks = 15
                        pygame.mixer.Sound(os.path.join("assets", "sfx", "playerhurt.mp3")).play()
                    for bala in balas:
                        if collide(inimigo.x, inimigo.y, inimigo.width, inimigo.height, bala.x, bala.y, 4, 4) and not inimigo in bala.hitten:
                            bala.hit(player, inimigo)
                            if inimigo.hp < 1: inimigo.die(player)
            if len(balas) != 0:
                for bala in balas: bala.movement()
            if len(inimigos) != 0:
                for inimigo in inimigos:
                    inimigo.movement(player)
            if Now - last_enemy >= enemy_delay:
                inimigos.append(enemy(player.kills))
                last_enemy = Now
                enemy_delay = random.randint(1500, 4000)
            balas = [b for b in balas if b.inbounds and b.perfsleft > 0]
            inimigos = [i for i in inimigos if i.alive]
        case "loja": pass
        case _:
            inimigos = []
            player.kills = 0
            player.x, player.y = tamanho_tela/2, tamanho_tela/2
            player.hp = 20
    draw(tela_atual, tela, tamanho_tela, player, balas, inimigos)
    print(tela_atual)
    if player.hp <= 0: tela_atual = "menu"; pygame.mixer.Sound(os.path.join("assets", "sfx", "playerdeath.mp3")).play()
    tempo.tick(30)

wsave(player)
GET_OUT()

