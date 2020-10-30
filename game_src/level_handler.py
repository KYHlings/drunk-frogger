import pygame

from image.image_handler import get_background_image, get_mob_sprite, get_floating_mob_sprite, \
    get_safe_floating_mob_sprite
from sprites_classes.npc import Mob, Goat, Floating_mob

tick = pygame.time.get_ticks()


class Level:
    def __init__(self, lanes, floating_lanes, background_image, goat, music, spawn_timer, time_spawned,
                 fl_spawn_timer, fl_time_spawned, drown_cord, amount_quiz, quiz_cord, sinking_cord, safe_lanes):
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
        self.amount_quiz = amount_quiz
        self.quiz_cord = quiz_cord
        self.sinking_cord = sinking_cord
        self.safe_lanes = safe_lanes

    def spawn_paused(self):
        self.time_of_pause = pygame.time.get_ticks()

    def spawn_resumed(self):
        extra_time = pygame.time.get_ticks() - self.time_of_pause
        for i in range(len(self.spawn_timer)):
            self.spawn_timer[i] += extra_time
        for i in range(len(self.fl_spawn_timer)):
            self.fl_spawn_timer[i] += extra_time


class Lane:

    def __init__(self, mobs, y, velocity, is_left):
        self.mobs = mobs
        self.y = y
        self.velocity = velocity
        self.is_left = is_left
        self.floating_mobs = mobs


def create_level(level_number):
    if level_number == 1:
        lane_1 = [Mob(30, 345, get_mob_sprite(False), False),
                  Mob(300, 345, get_mob_sprite(False), False), Mob(570, 345, get_mob_sprite(False), False)]

        lane_2 = [Mob(500, 390, get_mob_sprite(True), True), Mob(200, 390, get_mob_sprite(True), True),
                  Mob(700, 390, get_mob_sprite(True), True),
                  Mob(400, 390, get_mob_sprite(True), True)]

        lane_3 = [Mob(0, 435, get_mob_sprite(False), False), Mob(200, 435, get_mob_sprite(False), False),
                  Mob(350, 435, get_mob_sprite(False), False),
                  Mob(500, 435, get_mob_sprite(False), False)]

        lane_4 = [Mob(600, 485, get_mob_sprite(True), True), Mob(400, 485, get_mob_sprite(True), True),
                  Mob(250, 485, get_mob_sprite(True), True),
                  Mob(50, 485, get_mob_sprite(True), True)]

        level = Level(lanes=[Lane(lane_1, 345, 5, False),
                             Lane(lane_2, 390, 5, True),
                             Lane(lane_3, 435, 5, False),
                             Lane(lane_4, 485, 5, True)],
                      floating_lanes=[Lane([], 55, 5, True), Lane([], 90, 5, False), Lane([], 125, 5, True),
                                      Lane([], 160, 5, False), Lane([], 193, 5, True)],
                      background_image=get_background_image(0),
                      goat=Goat(400, 200),
                      amount_quiz=2,
                      quiz_cord=[300, 30],
                      music=0,
                      spawn_timer=[1000, 1000, 1000, 1000],
                      time_spawned=[pygame.time.get_ticks(), pygame.time.get_ticks(), pygame.time.get_ticks(),
                                    pygame.time.get_ticks()],
                      fl_spawn_timer=[1000, 2000, 1000, 2000, 1000],
                      fl_time_spawned=[tick, tick, tick, tick, tick],
                      drown_cord=225,
                      sinking_cord=(60, 225),
                      safe_lanes=[]
                      )

    if level_number == 2:
        lane_9 = [Mob(150, 525, get_mob_sprite(False), False), Mob(300, 525, get_mob_sprite(False), False),
                  Mob(400, 525, get_mob_sprite(False), False),
                  Mob(600, 525, get_mob_sprite(False), False)]
        lane_8 = []
        lane_7 = []

        level = Level(lanes=[Lane([Mob(150, 50, get_mob_sprite(False), False)], 50, 5, False),
                             Lane([Mob(150, 90, get_mob_sprite(True), True)], 90, 5, True),
                             Lane([Mob(150, 135, get_mob_sprite(False), False)], 135, 5, False),

                             Lane([Mob(150, 235, get_mob_sprite(False), False)], 235, 5, False),
                             Lane([Mob(150, 280, get_mob_sprite(True), True)], 280, 5, True),
                             Lane([Mob(150, 330, get_mob_sprite(False), False)], 330, 5, False),

                             Lane([Mob(150, 430, get_mob_sprite(False), False)], 430, 5, False),
                             Lane([Mob(150, 480, get_mob_sprite(True), True)], 480, 5, True),
                             Lane(lane_9, 525, 5, False)],
                      background_image=get_background_image(1),
                      goat=Goat(400, 200),
                      music=0,
                      amount_quiz=3,
                      quiz_cord=[400, 205, 20],
                      spawn_timer=[1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000, 1000],
                      time_spawned=[tick, tick, tick, tick, tick, tick, tick, tick, tick],
                      drown_cord=0,
                      fl_spawn_timer=[],
                      fl_time_spawned=[],
                      floating_lanes=[],
                      sinking_cord=(0, 0),
                      safe_lanes=[]
                      )

    if level_number == 3:
        lane_9 = [Floating_mob(150, 515, get_floating_mob_sprite(False), False),
                  Floating_mob(300, 515, get_floating_mob_sprite(False), False),
                  Floating_mob(400, 515, get_floating_mob_sprite(False), False),
                  Floating_mob(600, 515, get_floating_mob_sprite(False), False)]
        lane_8 = []
        lane_7 = []

        level = Level(lanes=[],
                      floating_lanes=[
                          Lane([Floating_mob(150, 50, get_floating_mob_sprite(False), False)], 50, 5, False),
                          Lane([Floating_mob(150, 90, get_floating_mob_sprite(True), True)], 90, 5, True),
                          Lane([Floating_mob(150, 135, get_floating_mob_sprite(False), False)], 135, 5, False),

                          Lane([Floating_mob(150, 235, get_floating_mob_sprite(False), False)], 235, 5, False),
                          Lane([Floating_mob(150, 280, get_floating_mob_sprite(True), True)], 280, 5, True),
                          Lane([Floating_mob(150, 330, get_floating_mob_sprite(True), False)], 330, 5, False),

                          Lane([Floating_mob(150, 430, get_floating_mob_sprite(True), False)], 430, 5, False),
                          Lane([Floating_mob(150, 480, get_floating_mob_sprite(True), True)], 480, 5, True),
                          Lane(lane_9, 515, 5, False)],
                      safe_lanes=[Lane([Floating_mob(150, 180, get_safe_floating_mob_sprite(True), False)], 180, 5, False),
                                  Lane([Floating_mob(150, 380, get_safe_floating_mob_sprite(True), False)], 380, 5, False)],
                      background_image=get_background_image(2),
                      goat=Goat(400, 200),
                      music=0,
                      amount_quiz=3,
                      quiz_cord=[400, 205, 20],
                      fl_spawn_timer=[1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000, 1000],
                      fl_time_spawned=[tick, tick, tick, tick, tick, tick, tick, tick, tick],
                      drown_cord=0,
                      spawn_timer=[],
                      time_spawned=[],

                      sinking_cord=(60, 560)
                      )
    return level
