import sys
import os

import pygame
from golden_utils import true, false, none, rjson, wjson

sys.stdout = open(os.path.join(".RogueMath_data", "log"), "w", encoding="utf-8")
sys.stderr = open(os.path.join(".RogueMath_data", "error_log"), "w", encoding="utf-8")

def rsave():
    try:
        return rjson(os.path.join(".", ".RogueMath_data", "data.dat"))
    except Exception:
        try:
            return rjson(os.path.join(".", ".RogueMath_data", "data.bak"))
        except Exception:
            try:
                return rjson(os.path.join(".", ".RogueMath_data", "data.old"))
            except Exception as e:
                print(f"Error: {e}")

def initialization():
    pygame.init()
    pygame.font.init()
    tamanho_tela = 700
    tela = pygame.display.set_mode((tamanho_tela, tamanho_tela))
    pygame.display.set_caption("RogueMath")
    return tamanho_tela, tela, "menu", true, pygame.time.Clock()

def GET_OUT():
    pygame.quit()
    sys.exit()
