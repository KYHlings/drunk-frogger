from image_handler import get_dead_sprite


class Dead_Frog():
    def __init__(self):
        self.img = get_dead_sprite()
        self.is_dead = False

    def player_died(self,x,y):
        self.dead_x = x
        self.dead_y = y
        self.is_dead = True

