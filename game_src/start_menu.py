import sys

import pygame

from game_src.score_handler import score_window, write_highscore
from image.image_handler import main_menu_image
from game_src.settings import Sound_settings
from music_and_sound.sound_handler import get_title_music, music_volume
from game_src.window_handler import screen, draw_text, font, text_colour, font1, instruction_window


def start_menu(sound_fx, volume):
    #This loads the sound handler module
    music_volume(volume)
    sound_fx.play_announcement()
    get_title_music()
    running = True
    while running:
        #This program writes out the start menu
        screen.blit(main_menu_image(), (0, 0))
        draw_text("Main Menu", font, text_colour, screen, 370, 20)
        draw_text("[B]egin Game", font1, text_colour, screen, 500, 180)
        draw_text("[S]ettings", font1, text_colour, screen, 500, 260)
        draw_text("[T]utorial", font1, text_colour, screen, 500, 340)
        draw_text("[H]igh Score", font1, text_colour, screen, 500, 420)
        draw_text("[Q]uit Game", font1, text_colour, screen, 500, 500)

        #This section takes input user to control menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return volume
                if event.key == pygame.K_s:
                    volume = Sound_settings(volume)
                if event.key == pygame.K_t:
                    instruction_window()
                if event.key == pygame.K_h:
                    score_window()
                if event.key == pygame.K_q:
                    sys.exit()
        pygame.display.update()