import pygame

gs = [
    "menu",
    "gameplay",
    "loja"
    ]

def state_sys(current_screen):
    current_pressed_keys = pygame.key.get_pressed()
    match current_screen:
        case "menu":
            if current_pressed_keys[pygame.K_RETURN]:
                cs = 1
            elif current_pressed_keys[pygame.K_TAB]:
                cs = 2
            else:
                cs = 0
        case "gameplay":
            if current_pressed_keys[pygame.K_ESCAPE]:
                cs = 0
            elif current_pressed_keys[pygame.K_TAB]:
                cs = 2
            else:
                cs = 1
        case "loja":
            if current_pressed_keys[pygame.K_TAB]:
                cs = 1
            elif current_pressed_keys[pygame.K_ESCAPE]:
                cs = 0
            else:
                cs = 2
    
    return gs[cs]
