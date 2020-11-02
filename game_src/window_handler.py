import sys

from game_src.variabels import *
from image.image_handler import win_image, alcohol_poisoning_image, how_to_play_image, roadkill_image, drown_image, \
    space_frog_image
from music_and_sound.sound_handler import get_win_music, get_lose_music

score_surf = pygame.surface.Surface((240, 60))


# Creates surface for draw_text function.
def text_object(text, font):
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()


# Write text at created surface.
def draw_text(text, font, colour, surface, x, y, direction):
    text_obj = font.render(text, 1, colour)
    text_rect = text_obj.get_rect()
    if direction == 'topleft':
        text_rect.topleft = (x, y)
    if direction == 'center':
        text_rect.center = (x, y)
    if direction == 'topright':
        text_rect.topright = (x, y)
    surface.blit(text_obj, text_rect)


# Creates and loads win window.
def win_window():
    get_win_music()
    winning = True
    while winning:
        screen.blit(win_image(), full_window_blit_pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

        pygame.display.update()


# Creates and loads lose window.
def lose_window(cause_of_death):
    get_lose_music()
    losing = True
    while losing:
        if cause_of_death == "roadkill":
            screen.blit(roadkill_image(), full_window_blit_pos)
        elif cause_of_death == "drowned":
            screen.blit(drown_image(), full_window_blit_pos)
        elif cause_of_death == "alcohol_poisoning":
            screen.blit(alcohol_poisoning_image(), full_window_blit_pos)
        elif cause_of_death == "asphyxiation":
            screen.blit(space_frog_image(), full_window_blit_pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

        pygame.display.update()


def instruction_window():
    # Creates how to play window
    while True:
        screen.blit(how_to_play_image(), full_window_blit_pos)
        draw_text("Any key to return", key_font, GREY, screen, 1270, 10, 'topright')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return
            pygame.display.update()


def level_title_window(level_number):
    # Display level names before playing a level
    name_ls = ['Suburban Bourbon', 'Cosmopolitan', 'Pangalactic']
    screen.fill(BLACK)
    draw_text(name_ls[level_number - 1], title_font, WHITE, screen, 650, 350, 'center')
    if level_number == 3:
        draw_text('Gargleblaster', title_font, WHITE, screen, 650, 450, 'center')
    pygame.display.update()
    pygame.time.delay(1000)


