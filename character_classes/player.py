import pygame

from image.image_handler import rotate_player_sprite, get_player_sprite


class Player:
    def __init__(self, player_x, player_y, width, height, rotation, img):
        self.lives = 5
        self.x = player_x
        self.y = player_y
        self.width = width
        self.height = height
        self.velocity = 5
        self.rotation = rotation
        self.drunk_meter = 0
        self.img = img
        self.org_img = img
        self.player_mask = pygame.mask.from_surface(self.img)
        self.player_rect = self.img.get_rect(topleft=(self.x, self.y))
        self.floating = False

    def update_img(self):
        # Updates player avatar image
        self.img = get_player_sprite(self.drunk_meter)
        self.img = rotate_player_sprite(self.img, self.rotation)
        self.player_mask = pygame.mask.from_surface(self.img)
        self.player_rect = self.img.get_rect(topleft=(self.x, self.y))
        return self.img, self.player_rect

    def drunken_consequence(self):
        # Changes player movement depending on how high drunk_meter is
        if self.drunk_meter == 1:
            self.velocity = 3.5
        elif self.drunk_meter == 2:
            self.velocity = 10
        elif self.drunk_meter == 3:
            self.velocity = - 5
        elif self.drunk_meter == 4:
            self.velocity = -8

    def mask_outline(self, screen):
        self.img = get_player_sprite(self.drunk_meter)
        self.img = rotate_player_sprite(self.img, self.rotation)
        self.player_mask = pygame.mask.from_surface(self.img)
        mask = self.player_mask
        mask_surf = mask.to_surface()
        mask_surf.set_colorkey((0, 0, 0))
        screen.blit(mask_surf, (self.x - 1, self.y))
        screen.blit(mask_surf, (self.x + 1, self.y))
        screen.blit(mask_surf, (self.x, self.y - 1))
        screen.blit(mask_surf, (self.x, self.y + 1))

    def reset(self):
        # Sets player cord when triggerd.
        self.x = 620
        self.y = 770

    def move(self, keys):
        # Allows player avatar to move with keys on keyboard
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.velocity
            self.rotation = 90
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.velocity
            self.rotation = 270
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.velocity
            self.rotation = 0
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rotation = 180
            self.y += self.velocity

        # Sets border for player to stay on screen.
        if self.y > 770:
            self.y = 770

        if self.y < 0:
            self.y = 0

        if self.x < 0:
            self.x = 0

        if self.x > 1240:
            self.x = 1240
