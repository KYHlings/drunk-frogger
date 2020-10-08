import pygame


def get_player_sprite():
    player_sprite = pygame.image.load("images_src/frog.png")
    player_sprite = pygame.transform.scale(player_sprite,(40,30))
    return player_sprite