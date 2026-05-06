import pygame

from golden_utils import true, false, none
from src.fonts.fonts import fontetítulo, fontestats, fonteloja

textotítulo = fontetítulo.render("RogueMath", false, (255, 255, 255))
textomoedas, textoloja = none, none
lastcoin, lastspeed, lastdamage, lastperf = none, none, none, none
#CÓDIGO DE IA {
def render_multiline(font, text, color, line_spacing=0, antialias=false):
    lines = text.splitlines() or [""]
    surfs = [font.render(line, antialias, color) for line in lines]
    w = max(s.get_width() for s in surfs)
    h = sum(s.get_height() for s in surfs) + line_spacing * (len(surfs)-1)
    out = pygame.Surface((w, h), pygame.SRCALPHA)
    y = 0
    for s in surfs:
        out.blit(s, (0, y))
        y += s.get_height() + line_spacing
    return out

def draw(tela_atual, tela, tamanho_tela, player, balas, inimigos):
    global lastcoin, lastspeed, lastdamage, lastperf, textoloja, textomoedas
    mousepos = pygame.mouse.get_pos()
    if player.speed != lastspeed or player.coins != lastcoin or player.base_damage != lastdamage or player.perfs != lastperf:
        textoloja = render_multiline(fonteloja, f"""Clique com o botão esquerdo do mouse para aumentar o dano, com o direito
para aumentar a perfuração e com o do meio para aumentar a velocidade
velocidade atual: {player.speed}, dano atual: {player.base_damage}, perfuração atual: {player.perfs}
velocidade: 10 moedas, dano: 30 moedas, perfuração: 50 moedas, moedas: {player.coins}""", (255, 255, 255), 5)
        textomoedas = fontestats.render(f"Moedas: {player.coins}", false, (0, 0 ,0))
        lastspeed, lastcoin, lastdamage, lastperf = player.speed, player.coins, player.base_damage, player.perfs
    match tela_atual:
        case "menu":
            tela.fill((0, 0, 0))
            tela.blit(textotítulo, (tamanho_tela/2 - textotítulo.get_width()/2, tamanho_tela/2 - textotítulo.get_height()/2))
        case "gameplay":
            tela.fill((255, 255, 0))
            pygame.draw.rect(tela, (255, 255, 0), (player.x - 15, player.y - 15, 30, 30))
            pygame.draw.rect(tela, (0, 0, 0), (player.x - 15, player.y - 15, 30, 30), 3)
            if len(balas) != 0:
                for bala in balas:
                    pygame.draw.rect(tela, (0, 0, 0), (bala.x - 2, bala.y - 2, 4, 4))
            if len(inimigos) != 0:
                for inimigo in inimigos:
                    tela.blit(inimigo.image, (inimigo.x - 15, inimigo.y - 15))
            tela.blit(textomoedas, (50, 25))
            pygame.draw.rect(tela, (0, 0, 0), (tamanho_tela - 251, 24, 202, 27))
            pygame.draw.rect(tela, (0, 255, 0), (tamanho_tela - 250, 25, player.hp * 10, 25))
        case "loja":
            tela.fill((100, 100, 100))
            tela.blit(textoloja, (tamanho_tela/2 - textoloja.get_width()/2, tamanho_tela/2 - textoloja.get_height()/2))
        case _:
            tela.fill((255, 0, 0))
    pygame.draw.circle(tela, (255, 255, 255), mousepos, 4)
    pygame.draw.circle(tela, (0, 0, 0), mousepos, 5, 1)
    pygame.display.flip()

