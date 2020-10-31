import pygame


class Mob:
    def __init__(self, mob_x, mob_y, image, is_left):
        self.mob_x = mob_x
        self.mob_y = mob_y
        self.image = image
        self.mob_mask = pygame.mask.from_surface(self.image)
        self.mob_rect = self.image.get_rect(topleft=(self.mob_x, self.mob_y))
        self.is_left = is_left

    def update_rect(self, direction, velocity):
        #Updates mobs rectangels
        self.mob_x += velocity * direction
        self.mob_rect = self.image.get_rect(topleft=(self.mob_x, self.mob_y))

    def check_collide(self, player):
        #Checks collision between mobs and player
        (mx, my) = (self.mob_rect[0], self.mob_rect[1])
        px = mx - player.player_rect[0]
        py = my - player.player_rect[1]
        overlap = player.player_mask.overlap(self.mob_mask, (px, py))
        if overlap:
            return True


class Floating_mob(Mob):
    #Does the same as mob class
    def __init__(self, mob_x, mob_y, image, is_left):
        super().__init__(mob_x, mob_y, image, is_left)


class Goat:
    def __init__(self, get_x, get_y):
        self.get_x = get_x
        self.get_y = get_y
        self.velocity = 4
