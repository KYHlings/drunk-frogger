from game_src.settings import sound_settings
from game_src.window_handler import text_object, draw_text
from image.image_handler import get_pause_window
from game_src.variabels import *


def pause_screen(volume):
    #Creates a pause screen with selectable options
    options = ["[C]ontinue", "[S]ettings", "[Q]uit To Menu"]
    option_ls = []
    pause = "Pause Menu"
    for option in options:
        option_ls.append(text_object(option, large_text))
    while True:
        alt = 250
        screen.blit(get_pause_window(), (465, 125))
        draw_text(pause, large_text, BLACK, screen, 535, 170,'topleft')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYUP:
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
