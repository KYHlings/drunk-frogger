import pygame


def get_player_sprite():
    player_sprite = pygame.image.load("images_src/frog.png")
    player_sprite = pygame.transform.scale(player_sprite, (40, 30))
    return player_sprite


def get_background_image():
    background_image = pygame.image.load("images_src/back_placehold2.png")
    background_image = pygame.transform.scale(background_image, (800, 600))
    return background_image
