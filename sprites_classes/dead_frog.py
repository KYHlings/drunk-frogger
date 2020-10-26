from pygame.time import get_ticks
from image.image_handler import get_roadkill_sprite, get_drowned_sprite


class Dead_Frog():
    def __init__(self):
        self.roadkill_img = get_roadkill_sprite(0)
        self.drowned_img = get_drowned_sprite(0)
        self.is_dead = False

    def player_died(self, x, y, cause_of_death):
        self.dead_x = x
        self.dead_y = y
        self.is_dead = True
        self.time_of_death = get_ticks()
        self.cause_of_death = cause_of_death

    def check_time_of_death(self):
        if get_ticks() - self.time_of_death >= 1500:
            self.is_dead = False
