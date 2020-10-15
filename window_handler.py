import sys
import pygame

from image_handler import win_image, lose_image
from sound_handler import get_win_music, get_lose_music

pygame.init()

screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font("PAPYRUS.TTF", 80)
font1 = pygame.font.Font("PAPYRUS.TTF", 60)
text_colour = (0, 0, 0)

#Creates surface for draw_text function.
def text_object(text, font):
    text_surface = font.render(text, True, (255, 255, 255))
    return text_surface, text_surface.get_rect()

#Write text at created surface.
def draw_text(text, font, colour, surface, x, y):
    text_obj = font.render(text, 1, colour)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

#Creates and loads win window.
def win_window():
    get_win_music()
    winning = True
    while winning:
        screen.blit(win_image(), (0, 0))
        draw_text("You Win!", font, text_colour, screen, 800, 600)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                sys.exit()

        pygame.display.update()

#Creates and loads lose window.
def lose_window():
    get_lose_music()
    losing = True
    while losing:
        screen.blit(lose_image(), (0, 0))
        draw_text("You Lose!", font, text_colour, screen, 800, 600)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                sys.exit()

        pygame.display.update()
