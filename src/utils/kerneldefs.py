import sys
import os
import random
import threading
from time import sleep as sl

import pygame
from golden_utils import true, false, none, rjson, wjson

from src.classes.player import player

sys.stdout = open(os.path.join(".RogueMath_data", "log"), "w", encoding="utf-8")
sys.stderr = open(os.path.join(".RogueMath_data", "error_log"), "w", encoding="utf-8")

def rsave():
    playerr = player()
    savemain = rjson(os.path.join(".", ".RogueMath_data", "data.dat"))
    saveBAcKup = rjson(os.path.join(".", ".RogueMath_data", "data.bak"))
    OLDbackup = rjson(os.path.join(".", ".RogueMath_data", "data.old"))
    def updatesave(playerarg, data):
        playerarg.__dict__.update(data)

    if savemain != none:
        updatesave(playerr, savemain)
        return playerr
    elif saveBAcKup != none:
        updatesave(playerr, saveBAcKup)
        return playerr
    elif OLDbackup != none:
        updatesave(playerr, OLDbackup)
        return playerr
    else:
        return playerr

def wsave(player):
    try:
        os.remove(os.path.join(".", ".RogueMath_data", "data.old"))
        os.rename(os.path.join(".", ".RogueMath_data", "data.bak")), os.path.join(".", ".RogueMath_data", "data.old")
        os.rename(os.path.join(".", ".RogueMath_data", "data.dat")), os.path.join(".", ".RogueMath_data", "data.bak")
        wjson(player.__dict__, os.path.join(".", ".RogueMath_data", "data.dat"))
    except FileNotFoundError:
        with open(os.path.join(".", ".RogueMath_data", "data.dat"), "a"):
            pass
        with open(os.path.join(".", ".RogueMath_data", "data.bak"), "a"):
            pass
        with open(os.path.join(".", ".RogueMath_data", "data.old"), "a"):
            pass
        os.remove(os.path.join(".", ".RogueMath_data", "data.old"))
        os.rename(os.path.join(".", ".RogueMath_data", "data.bak"), os.path.join(".", ".RogueMath_data", "data.old"))
        os.rename(os.path.join(".", ".RogueMath_data", "data.dat"), os.path.join(".", ".RogueMath_data", "data.bak"))
        wjson(player.__dict__, os.path.join(".", ".RogueMath_data", "data.dat"))
    except Exception as e:
        sys.stderr.write(f"Error: {e}")

def initialization():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    sl(0.5)
    music_s()
    tamanho_tela = 650
    tela = pygame.display.set_mode((tamanho_tela, tamanho_tela))
    pygame.display.set_caption("RogueMath")
    return tamanho_tela, tela, "menu", true, pygame.time.Clock()

def music():
    play_folder = os.path.join(".", "assets", "music")
    musicas = [os.path.join(play_folder, f) for f in os.listdir(play_folder)]
    while true:
        if not musicas: break
        i = random.randint(0, len(musicas) - 1)
        pygame.mixer.music.load(musicas[i])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            sl(1)

def music_s():
    music_t = threading.Thread(target = music, daemon = true)
    music_t.start()

def collide(tgx, tgy, tgwidth, tgheight, etcx, etcy, etcwidth, etcheight):
    tgu, tgd, tgr, tgl = tgy - tgheight/2, tgy + tgheight/2, tgx + tgwidth/2, tgx - tgwidth/2
    etcu, etcd, etcr, etcl = etcy - etcheight/2, etcy + etcheight/2, etcx + etcwidth/2, etcx - etcwidth/2
    return (etcd > tgu
        and etcu < tgd
        and etcr > tgl
        and etcl < tgr)

def GET_OUT():
    pygame.quit()
    sys.exit()

