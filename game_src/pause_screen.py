from game_src.settings import sound_settings
from game_src.window_handler import text_object, draw_text
from image.image_handler import get_pause_window
from game_src.variabels import *


def pause_screen(volume):
    #Creates a pause screen with selectable options
    options = ["[C]ontinue", "[S]ound settings", "[Q]uit To Menu"]
    option_ls = []
    pause = "Pause Menu"
    for option in options:
        option_ls.append(text_object(option, pause_font))
    while True:
        alt = 250
        screen.blit(get_pause_window(), (480, 225))
        draw_text(pause, large_text, BLACK, screen, 535, 180,'topleft')
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
            alternative[1].center = (635, alt)
            alt += 50
            screen.blit(alternative[0], alternative[1])
        pygame.display.update()
    return
