import pygame

from image_handler import main_menu_image
from window_handler import draw_text, font, text_colour, screen


def settings():
    running = True
    while running:
        screen.blit(main_menu_image(), (0, 0))
        draw_text("Settings", font, text_colour, screen, 210, 100)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    running = False
                if event.key == pygame.K_RIGHT:
                    pass
            if event.type == pygame.QUIT:
                running = False
        button_2 = pygame.Rect(235, 320, 0, 50)
        pygame.draw.rect(screen, text_colour, button_2)
        pygame.display.update()


settings()