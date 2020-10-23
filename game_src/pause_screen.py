import pygame

from game_src.window_handler import text_object


def pause_screen():
    options = ["[C]ontinue", "[S]ettings", "[Q]uit Game"]
    option_ls = []
    large_text = pygame.font.Font("font_src/PAPYRUS.TTF", 20)
    for option in options:
        option_ls.append(text_object(option, large_text))
    while True:
        screen = pygame.Surface([600, 400])

        alt = 350
        for alternative in option_ls:
            alternative[1].center = (350, alt)
            alt += 90
            screen.blit(alternative[0], alternative[1])
            for event in pygame.event.get():
        pygame.display.update()
    return
