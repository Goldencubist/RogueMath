import sys
import os

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
        os.rename(os.path.join(".", ".RogueMath_data", "data.bak"), os.path.join(".", ".RogueMath_data", "data.old"))
        os.rename(os.path.join(".", ".RogueMath_data", "data.dat"), os.path.join(".", ".RogueMath_data", "data.bak"))
        wjson(player.__dict__, os.path.join(".", ".RogueMath_data", "data.dat"))
    except FileNotFoundError:
        with open(os.path.join(".", ".RogueMath_data", "data.dat"), "r"):
            pass
        with open(os.path.join(".", ".RogueMath_data", "data.bak"), "r"):
            pass
        with open(os.path.join(".", ".RogueMath_data", "data.old"), "r"):
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
    tamanho_tela = 700
    tela = pygame.display.set_mode((tamanho_tela, tamanho_tela))
    pygame.display.set_caption("RogueMath")
    print("Duro de calcular")
    return tamanho_tela, tela, "menu", true, pygame.time.Clock()

def GET_OUT():
    pygame.quit()
    sys.exit()
