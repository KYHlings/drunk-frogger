import pygame

from image.image_handler import get_background_image, get_mob_sprite
from sprites_classes.npc import Mob, Goat


class Level:
    def __init__(self, lanes, floating_lanes, background_image, goat, music, spawn_timer, time_spawned,
                 fl_spawn_timer, fl_time_spawned, drown_cord):
        self.lanes = lanes
        self.floating_lanes = floating_lanes
        self.background_image = background_image
        self.goat = goat
        self.music = music
        self.spawn_timer = spawn_timer
        self.time_spawned = time_spawned
        self.fl_spawn_timer = fl_spawn_timer
        self.fl_time_spawned = fl_time_spawned
        self.drown_cord = drown_cord


class Lane:
    def __init__(self, mobs, y, velocity, is_left):
        self.mobs = mobs
        self.y = y
        self.velocity = velocity
        self.is_left = is_left
        self.floating_mobs = mobs


def create_level(level_number):
    if level_number == 1:
        level = Level(lanes=[Lane([Mob(0, 345, get_mob_sprite(False), False)], 345, 6, False),
                             Lane([Mob(500, 390, get_mob_sprite(True), True)], 390, 5, True),
                             Lane([Mob(0, 435, get_mob_sprite(False), False)], 435, 3, False),
                             Lane([Mob(600, 485, get_mob_sprite(True), True)], 485, 5, True)],
                      floating_lanes=[Lane([], 55, 5, True), Lane([], 85, 5, False), Lane([], 115, 5, True),
                                      Lane([], 145, 5, False), Lane([], 175, 3, True), Lane([], 200, 2, False)],
                      background_image=get_background_image(0),
                      goat=Goat(400, 200, 40, 30),
                      music=0,
                      spawn_timer=[1000, 2000, 1000, 2000],
                      time_spawned=[pygame.time.get_ticks(), pygame.time.get_ticks(), pygame.time.get_ticks(),
                                    pygame.time.get_ticks()],
                      fl_spawn_timer=[1000, 2000, 1000, 2000, 1000, 2000],
                      fl_time_spawned=[pygame.time.get_ticks(), pygame.time.get_ticks(), pygame.time.get_ticks(),
                                       pygame.time.get_ticks(), pygame.time.get_ticks(), pygame.time.get_ticks()],
                      drown_cord=225
                      )

    if level_number == 2:
        level = Level(lanes=[Lane([Mob(0, 350, get_mob_sprite(False), False)], 350, 5, False),
                             Lane([Mob(0, 400, get_mob_sprite(True), True)], 400, 5, True),
                             Lane([Mob(0, 450, get_mob_sprite(False), False)], 450, 5, False)],
                      background_image=get_background_image(1),
                      goat=Goat(400, 200, 40, 30),
                      music=0,
                      spawn_timer=[1000, 2000, 1000],
                      time_spawned=[pygame.time.get_ticks(), pygame.time.get_ticks(), pygame.time.get_ticks()],
                      drown_cord=0,
                      fl_spawn_timer=[],
                      fl_time_spawned=[],
                      floating_lanes=[],
                      )

    if level_number == 3:
        pass
        # To be continued
    return level
