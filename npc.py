import pygame
class Mob:
    def __init__(self, mob_x, mob_y, width, height, image):
        self.mob_x = mob_x
        self.mob_y = mob_y
        self.image = image
        self.width = width
        self.height = height
        self.velocity = 5
        self.hitbox = (self.mob_x + 6, self.mob_y + 7, 69, 30)
        self.mob_mask = pygame.mask.from_surface(self.image)
        self.mob_rect = self.image.get_rect()


class Get:
    def __init__(self, get_x, get_y, width, height):
        self.get_x = get_x
        self.get_y = get_y
        self.width = width
        self.height = height
        self.velocity = 4
        self.hitbox = (self.get_x + 6, self.get_y + 7, 69, 30)