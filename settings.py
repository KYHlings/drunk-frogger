import pygame

from image_handler import main_menu_image
from window_handler import draw_text, font, text_colour, screen


def settings():
    running = True
    while running:
        screen.blit(main_menu_image(), (0, 0))
        draw_text("Settings", font, text_colour, screen, 210, 100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False