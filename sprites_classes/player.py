import pygame

from image.image_handler import rotate_player_sprite, get_player_sprite


class Player:
    def __init__(self, player_x, player_y, width, height, rotation, img):
        self.lives = 5
        self.player_x = player_x
        self.player_y = player_y
        self.width = width
        self.height = height
        self.velocity = 4
        self.rotation = rotation
        self.drunk_meter = 0
        self.img = img
        self.org_img = img
        self.player_mask = pygame.mask.from_surface(self.img)
        self.player_rect = self.img.get_rect(topleft=(self.player_x, self.player_y))
        self.floating = False

    def update_img(self):
        self.img = get_player_sprite(self.drunk_meter)
        self.img = rotate_player_sprite(self.img, self.rotation)
        self.player_mask = pygame.mask.from_surface(self.img)
        self.player_rect = self.img.get_rect(topleft=(self.player_x, self.player_y))
        return self.img, self.player_rect

    def drunken_consequence(self):
        if self.drunk_meter == 1:
            self.velocity = 3.5
        elif self.drunk_meter == 2:
            self.velocity = 10
        elif self.drunk_meter == 3:
            self.velocity = - 4

    def check_collide(self, mob):
        (px, py) = (self.player_rect[0], self.player_rect[1])
        mx = px - mob.mob_rect[0]
        my = py - mob.mob_rect[1]
        overlap = mob.mob_mask.overlap(self.player_mask, (mx, my))
        if overlap:
            return True

    def reset(self):
        self.player_x = 400
        self.player_y = 570

    def move(self, keys):

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player_x -= self.velocity
            self.rotation = 90
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player_x += self.velocity
            self.rotation = 270
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.player_y -= self.velocity
            self.rotation = 0
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rotation = 180
            self.player_y += self.velocity

        if self.player_y > 570:
            self.player_y = 570

        if self.player_y < 0:
            self.player_y = 0

        if self.player_x < 0:
            self.player_x = 0

        if self.player_x > 760:
            self.player_x = 760
