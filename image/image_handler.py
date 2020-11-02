import pygame
from random import choice

from image.image_variabels import *


###
# each function gets bg_image for respektiv screen.

def main_menu_image():
    main_image = pygame.image.load("image/backgrounds_src/drunk_frog.jpg")
    main_image = pygame.transform.scale(main_image, bg_image_size)
    return main_image


def get_background_image(level_number):
    file_names = ["bg_suburban_bourbon.png", "bg_cosmopolitan.png", "bg_Pangalactic_G2.png"]
    background_image = pygame.image.load(f"image/backgrounds_src/{file_names[level_number]}")
    background_image = pygame.transform.scale(background_image, bg_image_size)
    return background_image


def win_image():
    win_frog_image = pygame.image.load("image/backgrounds_src/win_frog.jpg")
    win_frog_image = pygame.transform.scale(win_frog_image, bg_image_size)
    return win_frog_image


def how_to_play_image():
    how_to_play = pygame.image.load("image/backgrounds_src/how_to_play1.png")
    how_to_play = pygame.transform.scale(how_to_play, bg_image_size)
    return how_to_play


def alcohol_poisoning_image():
    lose_frog_image = pygame.image.load("image/backgrounds_src/you_lose.jpg")
    lose_frog_image = pygame.transform.scale(lose_frog_image, bg_image_size)
    return lose_frog_image


###

# gets image for the quiz box
def get_quiz_box():
    quiz_box = pygame.image.load("image/backgrounds_src/quiz_box1.png")
    quiz_box = pygame.transform.scale(quiz_box, quiz_box_size)
    return quiz_box


# gets image for pause window
def get_pause_window():
    pause_box = pygame.image.load("image/backgrounds_src/Scroll_1.jpg")
    pause_box = pygame.transform.scale(pause_box, pause_window_size)
    return pause_box


# gets roadkill image
def roadkill_image():
    run_over_image = pygame.image.load("image/backgrounds_src/run_over.jpg")
    run_over_image = pygame.transform.scale(run_over_image, bg_image_size)
    return run_over_image


# gets drown image
def drown_image():
    drowned_frog_image = pygame.image.load("image/backgrounds_src/drowned.jpg")
    drowned_frog_image = pygame.transform.scale(drowned_frog_image, bg_image_size)
    return drowned_frog_image


# gets space_frog image
def space_frog_image():
    space_frog_image = pygame.image.load("image/backgrounds_src/dejected-space-frog.jpg")
    space_frog_image = pygame.transform.scale(space_frog_image, bg_image_size)
    return space_frog_image


# gets player sprites depending on drunknes
def get_player_sprite(drunk_meter):
    player_sprites = ['frog.png', 'frog_tipsy.png', 'frog_drunk.png', 'frog_sloshed.png', 'frog_sloshed.png']
    player_sprite = pygame.image.load(f"image/player_sprites/{player_sprites[drunk_meter]}").convert_alpha()
    player_sprite = pygame.transform.scale(player_sprite, player_sprite_size)
    return player_sprite


# rotates player sprite depending on movment
def rotate_player_sprite(player_sprite, rotation):
    player_sprite = pygame.transform.rotate(player_sprite, rotation)
    return player_sprite


# gets the goat sprite
def get_get_sprite():
    get_sprite = pygame.image.load("image/npc_sprites/visgetens_het.png")
    get_sprite = pygame.transform.scale(get_sprite, goat_lane_size)
    return get_sprite


# gets the goat in bigger size for the quiz
def get_get_quiz_sprite():
    get_sprite = pygame.image.load("image/npc_sprites/visgetens_het.png")
    get_sprite = pygame.transform.scale(get_sprite, goat_quiz_size)
    return get_sprite


# Gets the car sprites for the mob class
def get_mob_sprite(is_left):
    cars_sprites = [("car_green1.png", car_green_size), ("car_red1.png", car_red_size), ("taxi1.png", taxi_size),
                    ("postnord2.png", truck_size)]
    car_sprite = choice(cars_sprites)
    mob_sprite = pygame.image.load(f"image/npc_sprites/{car_sprite[0]}").convert_alpha()
    mob_sprite = pygame.transform.scale(mob_sprite, car_sprite[1])
    mob_sprite = pygame.transform.flip(mob_sprite, is_left, False)
    return mob_sprite


# Gets the logs for the floating mobs class
def get_floating_mob_sprite(is_left):
    log_sprites = [("log.png", log_size)]
    log_sprite = choice(log_sprites)
    mob_sprite = pygame.image.load(f"image/npc_sprites/{log_sprite[0]}").convert_alpha()
    mob_sprite = pygame.transform.scale(mob_sprite, log_sprite[1])
    mob_sprite = pygame.transform.flip(mob_sprite, is_left, False)
    return mob_sprite


# Gets sprite for safe lane mobs for lvl3
def get_safe_floating_mob_sprite(is_left):
    log_sprites = [("log.png", safe_lane_mob)]
    log_sprite = choice(log_sprites)
    mob_sprite = pygame.image.load(f"image/npc_sprites/{log_sprite[0]}").convert_alpha()
    mob_sprite = pygame.transform.scale(mob_sprite, log_sprite[1])
    mob_sprite = pygame.transform.flip(mob_sprite, is_left, False)
    return mob_sprite


# Gets sprite for life meter and start of drunken meter
def get_life_sprite():
    life_sprite = pygame.image.load("image/player_sprites/frog_face.png")
    life_sprite = pygame.transform.scale(life_sprite, drunk_meter_size)
    return life_sprite


# Gets sprite for end of drunken meter
def get_sloshed_face():
    sloshed_face = pygame.image.load("image/player_sprites/frog_face_sloshed.png")
    sloshed_face = pygame.transform.scale(sloshed_face, drunk_meter_size)
    return sloshed_face


# Get drunken meter sprite
def get_beer_sprite():
    beer_sprite = pygame.image.load("image/player_sprites/beer1.png")
    beer_sprite = pygame.transform.scale(beer_sprite, drunk_meter_size)
    return beer_sprite


# Get roadkill sprite for when player get run over
def get_roadkill_sprite(drunk_meter):
    dead_frogs = ["dead_frog.png", "frog_dead_tipsy.png", "frog_dead_drunk.png", "frog_dead_sloshed.png",
                  "frog_dead_sloshed.png"]
    dead_frog = pygame.image.load(f"image/player_sprites/{dead_frogs[drunk_meter]}")
    dead_frog = pygame.transform.scale(dead_frog, player_sprite_size)
    return dead_frog


# Get drown sprite for when player falss of logs
def get_drowned_sprite(drunk_meter):
    dead_frogs = ["drowning_frog.png", "drowning_frog_tipsy.png", "drowning_frog_drunk.png",
                  "drowning_frog_sloshed.png", "drowning_frog_sloshed.png"]
    dead_frog = pygame.image.load(f"image/player_sprites/{dead_frogs[drunk_meter]}")
    dead_frog = pygame.transform.scale(dead_frog, player_sprite_size)
    return dead_frog
