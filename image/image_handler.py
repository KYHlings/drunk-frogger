import pygame
from random import choice


def main_menu_image():
    main_menu_image = pygame.image.load("image/backgrounds_src/drunk_frog.jpg")
    main_menu_image = pygame.transform.scale(main_menu_image, (800, 600))
    return main_menu_image


def win_image():
    win_frog_image = pygame.image.load("image/backgrounds_src/win_frog.jpg")
    win_frog_image = pygame.transform.scale(win_frog_image, (800, 600))
    return win_frog_image


def lose_image():
    lose_frog_image = pygame.image.load("image/backgrounds_src/you_lose.jpg")
    lose_frog_image = pygame.transform.scale(lose_frog_image, (800, 600))
    return lose_frog_image


def get_player_sprite(drunk_meter):
    player_sprites = ['frog.png', 'frog_tipsy.png', 'frog_drunk.png', 'frog_sloshed.png']
    player_sprite = pygame.image.load(f"image/player_sprites/{player_sprites[drunk_meter]}").convert_alpha()
    player_sprite = pygame.transform.scale(player_sprite, (40, 30))
    return player_sprite


def rotate_player_sprite(player_sprite, rotation):
    player_sprite = pygame.transform.rotate(player_sprite, rotation)
    return player_sprite


def get_get_sprite():
    get_sprite = pygame.image.load("image/npc_sprites/visgetens_het.png")
    get_sprite = pygame.transform.scale(get_sprite, (100, 85))
    return get_sprite


def get_background_image(level_number):
    file_names = ["bg_suburban_bourbon.png", "back_placehold2.png"]
    background_image = pygame.image.load(f"image/backgrounds_src/{file_names[level_number]}")
    background_image = pygame.transform.scale(background_image, (800, 600))
    return background_image


def get_mob_sprite(is_left):
    cars_sprites = ["car_green1.png", "car_red1.png", "taxi1.png", "postnord2.png"]
    mob_sprite = pygame.image.load(f"image/npc_sprites/{choice(cars_sprites)}").convert_alpha()
    mob_sprite = pygame.transform.scale(mob_sprite, (80, 40))
    mob_sprite = pygame.transform.flip(mob_sprite, is_left, False)
    return mob_sprite


def get_life_sprite():
    life_sprite = pygame.image.load("image/player_sprites/frog_face.png")
    life_sprite = pygame.transform.scale(life_sprite, (40, 30))
    return life_sprite

def get_beer_sprite():
    beer_sprite = pygame.image.load("image/player_sprites/beer_mug.png")
    beer_sprite = pygame.transform.scale(beer_sprite, (40, 30))
    return beer_sprite



def get_dead_sprite(drunk_meter):
    dead_frogs = ["dead_frog.png", "frog_dead_tipsy.png", "frog_dead_drunk.png", "frog_dead_sloshed.png"]
    dead_frog = pygame.image.load(f"image/player_sprites/{dead_frogs[drunk_meter]}")
    dead_frog = pygame.transform.scale(dead_frog, (40, 30))
    return dead_frog
