import sys

from game_src.variabels import *
from image.image_handler import win_image, lose_image, how_to_play_image, roadkill_image, drown_image
from music_and_sound.sound_handler import get_win_music, get_lose_music

score_surf = pygame.surface.Surface((240, 60))

# Creates surface for draw_text function.
def text_object(text, font):
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()


# Write text at created surface.
def draw_text(text, font, colour, surface, x, y):
    text_obj = font.render(text, 1, colour)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


# Creates and loads win window.
def win_window():
    get_win_music()
    winning = True
    while winning:
        screen.blit(win_image(), full_window_blit_pos)
        # draw_text("You Win!", font, BLACK, screen, 800, 600)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

        pygame.display.update()


# Creates and loads lose window.
def lose_window():
    get_lose_music()
    losing = True
    while losing:
        screen.blit(lose_image(), full_window_blit_pos)
        # draw_text("You Lose!", font, BLACK, screen, 800, 600)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

        pygame.display.update()


def roadkill_window():
    get_lose_music()
    losing = True
    while losing:
        screen.blit(roadkill_image(), full_window_blit_pos)
        # draw_text("You Lose!", font, BLACK, screen, 800, 600)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

        pygame.display.update()


def drown_window():
    get_lose_music()
    losing = True
    while losing:
        screen.blit(drown_image(), full_window_blit_pos)
        # draw_text("You Lose!", font, BLACK, screen, 800, 600)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

        pygame.display.update()


def instruction_window():
    while True:
        screen.blit(how_to_play_image(), full_window_blit_pos)
        # draw_text("How to play!", font, BLACK, screen, 800, 600)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

            pygame.display.update()


def level_title_window(level_number):
    name_ls = ['Suburban Bourbon', 'Cosmopolitan', 'Pangalactic']
    screen.fill(WHITE)
    name_surf, name_rect = text_object(name_ls[level_number - 1], title_font)
    name_rect.center = (650, 350)
    screen.blit(name_surf, name_rect)
    if level_number == 3:
        name2_surf, name2_rect = text_object('Gargleblaster', title_font)
        name2_rect.center = (650, 450)
        screen.blit(name2_surf, name2_rect)
    pygame.display.update()
    pygame.time.delay(1000)
