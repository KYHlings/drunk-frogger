import pygame

from game_src.window_handler import text_object, screen


def pause_screen():
    options = ["[C]ontinue", "[S]ettings", "[Q]uit Game"]
    option_ls = []
    pause = "Pause Menu"
    large_text = pygame.font.Font("font_src/PAPYRUS.TTF", 20)
    for option in options:
        option_ls.append(text_object(option, large_text))
    while True:
        pause_window = pygame.Surface([350, 350])
        text_surf, text_rect = text_object(pause, large_text)
        text_rect.center = (400, 300)
        alt = 350
        screen.blit(pause_window, (175, 250))
        screen.blit(text_surf, text_rect)
        for alternative in option_ls:
            alternative[1].center = (350, alt)
            alt += 90
            screen.blit(alternative[0], alternative[1])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
        pygame.display.update()
    return
