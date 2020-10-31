from game_src.settings import sound_settings
from game_src.window_handler import text_object
from image.image_handler import get_pause_window
from game_src.variabels import *


def pause_screen(volume):
    options = ["[C]ontinue", "[S]ettings", "[Q]uit To Menu"]
    option_ls = []
    pause = "Pause Menu"
    for option in options:
        option_ls.append(text_object(option, large_text))
    while True:
        text_surf, text_rect = text_object(pause, large_text)
        text_rect.center = (650, 180)
        alt = 250
        screen.blit(get_pause_window(), (465, 125))
        screen.blit(text_surf, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return volume
                if event.key == pygame.K_s:
                    volume = sound_settings(volume)
                    return volume
                if event.key == pygame.K_q:
                    return False

        for alternative in option_ls:
            alternative[1].center = (625, alt)
            alt += 75
            screen.blit(alternative[0], alternative[1])
        pygame.display.update()
    return
