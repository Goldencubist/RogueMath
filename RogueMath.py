import pygame
import sys
from states import state_sys, gs
import UI.fonts
from kerneldefs import initialization, GET_OUT

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
