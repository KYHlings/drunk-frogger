import pygame

from image_handler import rotate_player_sprite, get_player_sprite


class Player:
    def __init__(self, player_x, player_y, width, height, rotation, img):
        self.player_x = player_x
        self.player_y = player_y
        self.width = width
        self.height = height
        self.velocity = 4
        self.hitbox = (self.player_x + 2, self.player_y + 2, 36, 27)
        self.rotation = rotation
        self.drunk_meter = 0
        self.img = img
        self.org_img = img
        self.player_mask = pygame.mask.from_surface(self.img)
        self.player_rect = self.img.get_rect()

    def update_img(self):
        self.img = get_player_sprite(self.rotation,self.drunk_meter)
        self.player_mask = pygame.mask.from_surface(self.img)
        self.player_rect = self.img.get_rect()


    def drunken_consequence(self):
        if self.drunk_meter == 1:
            self.velocity = 3.5
        elif self.drunk_meter == 2:
            self.velocity = 10
        elif self.drunk_meter == 3:
            self.velocity = - 4

    def check_collide_x(self, mob):
        if self.player_x <= mob.mob_x:
            if self.player_x + self.width >= mob.mob_x:
                return True
            return False
        else:
            if mob.mob_x + mob.width >= self.player_x:
                return True
            return False

    def check_collide_y(self, mob):
        if self.player_y <= mob.mob_y:
            if self.player_y + self.height >= mob.mob_y:
                return True
            return False
        else:
            if mob.mob_y + mob.height >= self.player_y:
                return True
            return False

    def check_collide(self, mob):

        return self.check_collide_y(mob) and self.check_collide_x(mob)

    def reset(self):
        self.player_x = 400
        self.player_y = 570

    def move(self, keys):

        if keys[pygame.K_LEFT]  or keys[pygame.K_a]:
            self.player_x -= self.velocity
            self.rotation = 90
            self.img = rotate_player_sprite(self.org_img,self.rotation)
            self.hitbox = (self.player_x + 2, self.player_y + 2, 27, 36)
            # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player_x += self.velocity
            self.rotation = 270
            self.img = rotate_player_sprite(self.org_img,self.rotation)
            self.hitbox = (self.player_x + 2, self.player_y + 2, 27, 36)
            # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.player_y -= self.velocity
            self.rotation = 0
            self.img = rotate_player_sprite(self.org_img,self.rotation)
            self.hitbox = (self.player_x + 2, self.player_y + 2, 36, 27)
            # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rotation = 180
            self.img = rotate_player_sprite(self.org_img,self.rotation)
            self.player_y += self.velocity
            self.hitbox = (self.player_x + 2, self.player_y + 2, 36, 27)
            # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

        if self.player_y > 570:
            self.player_y = 570

        if self.player_y < 0:
            self.player_y = 0

        if self.player_x < 0:
            self.player_x = 0

        if self.player_x > 760:
            self.player_x = 760
