#Stores variabels for easy change.
import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 800))
menu_font_large = pygame.font.Font("font_src/PAPYRUS.TTF", 120)
menu_font = pygame.font.Font("font_src/PAPYRUS.TTF", 60)
credits_font = pygame.font.Font("font_src/BarcadeBrawlRegular-plYD.ttf",20)
credits_title_font = pygame.font.Font("font_src/BarcadeBrawlRegular-plYD.ttf",25)
credits_font_large = pygame.font.Font("font_src/BarcadeBrawlRegular-plYD.ttf",30)
pause_font = pygame.font.Font("font_src/PAPYRUS.TTF", 30)
general_font = pygame.font.Font("font_src/PAPYRUS.TTF", 40)
score_font = pygame.font.Font("font_src/LcdSolid-VPzB.ttf", 45)
title_font = pygame.font.Font("font_src/ConnectionSerif-d20X.otf", 90)
key_font = pygame.font.Font("font_src/LcdSolid-VPzB.ttf", 30)

BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREY = (100,100,100)
full_window_blit_pos = (0,0)
font_list = [("PAPYRUS.TTF", 25), ("ConnectionSerif-d20X.otf", 20), ("LcdSolid-VPzB.ttf", 20),
                 ("RdjHandPixel-5w3L.otf", 23), ("VtcBadhangoverone-nnnO.ttf", 23)]
