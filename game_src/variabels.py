import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 800))
font = pygame.font.Font("font_src/PAPYRUS.TTF", 120)
font1 = pygame.font.Font("font_src/PAPYRUS.TTF", 60)
large_text = pygame.font.Font("font_src/PAPYRUS.TTF", 40)
score_font = pygame.font.Font("font_src/LcdSolid-VPzB.ttf", 45)
title_font = pygame.font.Font("font_src/ConnectionSerif-d20X.otf", 90)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
full_window_blit_pos = (0,0)
font_list = [("PAPYRUS.TTF", 25), ("ConnectionSerif-d20X.otf", 20), ("LcdSolid-VPzB.ttf", 20),
                 ("RdjHandPixel-5w3L.otf", 23), ("VtcBadhangoverone-nnnO.ttf", 23)]
