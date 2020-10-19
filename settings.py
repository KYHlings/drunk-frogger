import sys

import pygame

from image_handler import main_menu_image
from sound_handler import music_volume, get_title_music
from window_handler import draw_text, font, text_colour, screen, font1


def Sound_settings(volume_float):
    running = True
    get_title_music()
    volume_int = int(volume_float * 10)
    while running:
        volume_float = float(volume_int)/10
        volume_rect_x = 200
        screen.blit(main_menu_image(), (0, 0))
        draw_text("Settings", font, text_colour, screen, 220, 100)
        draw_text("Change volume [-][+]", font1, text_colour, screen, 200, 200)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                #Allows keyboard buttons to change sound volume
                if event.key == pygame.K_MINUS and volume_int > 0:
                    volume_int -= 1
                if event.key == pygame.K_PLUS and volume_int <= 5:
                    volume_int += 1
                if event.key == pygame.K_ESCAPE:
                    return volume_float
            if event.type == pygame.QUIT:
                sys.exit()
        #Changes the volume bars
        for i in range(volume_int):
            volume_rect = pygame.Rect(volume_rect_x, 320, 20, 50)
            volume_rect_x += 50
            pygame.draw.rect(screen, text_colour, volume_rect)
        music_volume(volume_float)
        pygame.display.update()

if __name__ == '__main__':
    Sound_settings(0.1)