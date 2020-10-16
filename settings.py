import pygame

from image_handler import main_menu_image
from window_handler import draw_text, font, text_colour, screen


def settings():
    running = True
    volume_int = 10
    while running:
        volume_rect_x = 200
        screen.blit(main_menu_image(), (0, 0))
        draw_text("Settings", font, text_colour, screen, 210, 100)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    volume_int -= 5
                if event.key == pygame.K_RIGHT:
                    volume_int += 5
            if event.type == pygame.QUIT:
                running = False
        for i in range(volume_int):
            volume_rect = pygame.Rect(volume_rect_x, 320, 0, 50)
            volume_rect_x += 50
            pygame.draw.rect(screen, text_colour, volume_rect)
        pygame.display.update()
