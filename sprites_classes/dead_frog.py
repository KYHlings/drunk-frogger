from pygame.time import get_ticks
from image.image_handler import get_dead_sprite


class Dead_Frog():
    def __init__(self):
        self.img = get_dead_sprite(0)
        self.is_dead = False

    def player_died(self, x, y):
        self.dead_x = x
        self.dead_y = y
        self.is_dead = True
        self.time_of_death = get_ticks()

    def check_time_of_death(self):
        if get_ticks() - self.time_of_death >= 1500:
            self.is_dead = False
