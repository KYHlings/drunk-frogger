import pygame

from image.image_handler import get_background_image, get_mob_sprite
from sprites_classes.npc import Mob, Goat


class Level:
    def __init__(self, lanes, floating_lanes, background_image, mobs, goat, music, spawn_timer, time_spawned):
        self.lanes = lanes
        self.floating_lanes = floating_lanes
        self.background_image = background_image
        self.mobs = mobs
        self.goat = goat
        self.music = music
        self.spawn_timer = spawn_timer
        self.time_spawned = time_spawned


class Lane:
    def __init__(self, y, velocity, is_left):
        self.y = y
        self.velocity = velocity
        self.is_left = is_left


def create_level(level_number):
    if level_number == 1:
        level = Level(lanes=[Lane(345, 5, False), Lane(390, 5, True), Lane(435, 5, False), Lane(485, 5, True)],
                      floating_lanes=[Lane(130, 5, False), Lane(100, 5, True), Lane(80, 5, False), Lane(60, 5, True)],
                      background_image=get_background_image(0),
                      mobs=[Mob(0, 345, 80, 40, get_mob_sprite(False), False),
                            Mob(500, 390, 80, 40, get_mob_sprite(True), True),
                            Mob(0, 435, 80, 40, get_mob_sprite(False), False),
                            Mob(600, 485, 80, 40, get_mob_sprite(True), True)],
                      goat=Goat(400, 200, 40, 30),
                      music=0,
                      spawn_timer=[1000, 2000, 1000, 2000],
                      time_spawned=[pygame.time.get_ticks(), pygame.time.get_ticks(), pygame.time.get_ticks(),
                                    pygame.time.get_ticks()])
    if level_number == 2:
        level = Level(lanes=[Lane(350, 5, False), Lane(400, 5, True), Lane(450, 5, False)],
                      background_image=get_background_image(1),
                      mobs=[Mob(0, 350, 80, 40, get_mob_sprite(False), False),
                            Mob(0, 400, 80, 40, get_mob_sprite(True), True),
                            Mob(0, 450, 80, 40, get_mob_sprite(False), False)],
                      goat=Goat(400, 200, 40, 30),
                      music=0,
                      spawn_timer=[1000, 2000, 1000],
                      time_spawned=[pygame.time.get_ticks(), pygame.time.get_ticks(), pygame.time.get_ticks()])

    if level_number == 3:
        pass
        # To be continued
    return level
