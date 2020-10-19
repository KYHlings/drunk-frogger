import sys

import pygame

from image_handler import main_menu_image
from settings import Sound_settings
from sound_handler import get_title_music, music_volume
from window_handler import screen, draw_text, font, text_colour, font1


def start_menu(sound_fx, volume):
    #This loads the sound handler module
    music_volume(volume)
    sound_fx.play_announcement()
    get_title_music()
    running = True
    while running:
        #This program writes out the start menu
        screen.blit(main_menu_image(), (0, 0))
        draw_text("Main Menu", font, text_colour, screen, 210, 100)
        button_1 = pygame.Rect(235, 220, 0, 50)
        button_2 = pygame.Rect(235, 320, 0, 50)
        button_3 = pygame.Rect(235, 420, 0, 50)
        pygame.draw.rect(screen, text_colour, button_1)
        draw_text("Start Game [1]", font1, text_colour, screen, 245, 200)
        pygame.draw.rect(screen, text_colour, button_2)
        draw_text("Settings [2]", font1, text_colour, screen, 245, 300)
        pygame.draw.rect(screen, text_colour, button_3)
        draw_text("End Game [3]", font1, text_colour, screen, 245, 400)
        #This section takes input user to control menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return volume
                if event.key == pygame.K_2:
                    volume = Sound_settings(volume)
                if event.key == pygame.K_3:
                    sys.exit()
        pygame.display.update()