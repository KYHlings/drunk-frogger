import sys

from game_src.score_handler import score_window
from game_src.settings import settings_window
from game_src.variabels import *
from image.image_handler import main_menu_image
from music_and_sound.sound_handler import get_title_music, music_volume
from game_src.window_handler import draw_text, instruction_window
from game_src.menu_buttons import start_menu_button, settings_menu_button, tutorial_menu_button, high_score_menu_button, quit_menu_button


def start_menu(sound_fx, volume, quiz_category):
    # This loads the sound handler module
    music_volume(volume)
    sound_fx.play_announcement()
    get_title_music()
    highlighted = 0
    running = True
    while running:
        # This program writes out the start menu
        screen.blit(main_menu_image(), (0, 0))
        #screen.fill(WHITE)
        draw_text("Main Menu", menu_font_large, WHITE, screen, 330, 20, 'topleft')
        start_menu_button(highlighted)
        settings_menu_button(highlighted)
        tutorial_menu_button(highlighted)
        high_score_menu_button(highlighted)
        quit_menu_button(highlighted)
        # draw_text("[B]egin Game", menu_font, BLACK, screen, 500, 180, 'topleft')
        # draw_text("[S]ettings", menu_font, BLACK, screen, 500, 260, 'topleft')
        # draw_text("[T]utorial", menu_font, BLACK, screen, 500, 340, 'topleft')
        # draw_text("[H]igh Score", menu_font, BLACK, screen, 500, 420, 'topleft')
        # draw_text("[Q]uit Game", menu_font, BLACK, screen, 500, 500, 'topleft')

        # This section takes input user to control menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_b:
                    return volume, quiz_category
                if event.key == pygame.K_s:
                    volume, quiz_category = settings_window(volume, quiz_category)
                if event.key == pygame.K_t:
                    instruction_window()
                if event.key == pygame.K_h:
                    score_window()
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_DOWN:
                    highlighted += 1
                    if highlighted == 5:
                        highlighted = 0
                if event.key == pygame.K_UP:
                    highlighted -= 1
                    if highlighted < 0:
                        highlighted = 4

                if event.key == pygame.K_RETURN:
                    if highlighted == 0:
                        return volume, quiz_category
                    if highlighted == 1:
                        volume, quiz_category = settings_window(volume, quiz_category)
                    if highlighted == 2:
                        instruction_window()
                    if highlighted == 3:
                        score_window()
                    if highlighted == 4:
                        sys.exit()

        pygame.display.update()
