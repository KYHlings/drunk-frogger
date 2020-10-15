import sys

import pygame

from image_handler import main_menu_image
from sound_handler import get_announcement, get_title_music
from window_handler import screen, draw_text, font, text_colour, font1


def main_menu():
    get_announcement()
    get_title_music()
    running = True
    while running:
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    running = False
                if event.key == pygame.K_2:
                    pass
                if event.key == pygame.K_3:
                    sys.exit()
        pygame.display.update()