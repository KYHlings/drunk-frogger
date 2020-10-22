from image.image_handler import get_background_image, get_mob_sprite
from sprites_classes.npc import Mob, Goat


class Level:
    def __init__(self,lanes,background_image,mobs,goat,music, spawn_timer):
        self.lanes = lanes
        self.background_image = background_image
        self.mobs = mobs
        self.goat = goat
        self.music = music
        self.spawn_timer = spawn_timer

def create_level(level_number):
    if level_number == 1:
        level = Level(lanes=[350, 400, 450],
                      background_image=get_background_image(),
                      mobs=[Mob(0, 350, 80, 40, get_mob_sprite(False)), Mob(0, 400, 80, 40, get_mob_sprite(True)),
                            Mob(0, 450, 80, 40, get_mob_sprite(False))],
                      goat=Goat(400, 200, 40, 30),
                      music=0,
                      spawn_timer=[1000, 2000, 1000])
    return level