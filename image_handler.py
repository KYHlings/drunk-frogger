import pygame
from random import choice


def get_player_sprite(rotation):
    player_sprite = pygame.image.load("images_src/frog.png")
    player_sprite = pygame.transform.scale(player_sprite, (40, 30))
    player_sprite = pygame.transform.rotate(player_sprite, rotation)
    return player_sprite

def get_get_sprite():
    get_sprite = pygame.image.load("images_src/visgetens_het.png")
    get_sprite = pygame.transform.scale(get_sprite, (40, 30))
    return get_sprite

def get_background_image():
    background_image = pygame.image.load("images_src/back_placehold2.png")
    background_image = pygame.transform.scale(background_image, (800, 600))
    return background_image


def get_mob_sprite(is_left):
    cars_sprites = ["car_green1.png", "car_red1.png", "taxi1.png", "postnord2.png"]
    mob_sprite = pygame.image.load(f"images_src/{choice(cars_sprites)}")
    mob_sprite = pygame.transform.scale(mob_sprite, (80, 40))
    mob_sprite = pygame.transform.flip(mob_sprite, is_left, False)
    return mob_sprite
