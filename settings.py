import sys

import pygame

from image_handler import main_menu_image
from window_handler import draw_text, font, text_colour, screen


def settings():
    running = True
    volume_int = 2
    while running:
        volume_float = float(volume_int)/10
        volume_rect_x = 200
        screen.blit(main_menu_image(), (0, 0))
        draw_text("Settings", font, text_colour, screen, 210, 100)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    volume_int -= 1
                if event.key == pygame.K_RIGHT:
                    volume_int += 1
                if event.key == pygame.K_ESCAPE:
                    return volume_float
            if event.type == pygame.QUIT:
                sys.exit()

        for i in range(volume_int):
            volume_rect = pygame.Rect(volume_rect_x, 320, 20, 50)
            volume_rect_x += 50
            pygame.draw.rect(screen, (255, 0, 0), volume_rect)

        pygame.display.update()

if __name__ == '__main__':
    settings()