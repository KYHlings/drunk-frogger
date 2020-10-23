import pygame

from game_src.window_handler import text_object


def pause_screen():
    options = ["[C]ontinue","[S]ettings","[Q]uit Game"]
    while True:
        screen = pygame.Surface([600,400])
        large_text = pygame.font.Font("font_src/PAPYRUS.TTF", 20)
        text_surf, text_rect = text_object(, large_text)
        text_rect.center = (400, 300)
        for alternative in options:
            alternative[1].center = (,alt)
            alt += 90
            screen.blit(alternative[0], alternative[1])
        return