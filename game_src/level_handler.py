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
        lane_1 = [Mob(30, 445, get_mob_sprite(False), False),
                  Mob(300, 445, get_mob_sprite(False), False), Mob(570, 445, get_mob_sprite(False), False)]

        lane_2 = [Mob(500, 510, get_mob_sprite(True), True), Mob(200, 510, get_mob_sprite(True), True),
                  Mob(700, 510, get_mob_sprite(True), True),
                  Mob(400, 510, get_mob_sprite(True), True)]

        lane_3 = [Mob(0, 570, get_mob_sprite(False), False), Mob(200, 570, get_mob_sprite(False), False),
                  Mob(350, 570, get_mob_sprite(False), False),
                  Mob(500, 570, get_mob_sprite(False), False)]

        lane_4 = [Mob(600, 640, get_mob_sprite(True), True), Mob(400, 640, get_mob_sprite(True), True),
                  Mob(250, 640, get_mob_sprite(True), True),
                  Mob(50, 640, get_mob_sprite(True), True)]

        level = Level(lanes=[Lane(lane_1, 445, 8, False),
                             Lane(lane_2, 510, 8, True),
                             Lane(lane_3, 570, 8, False),
                             Lane(lane_4, 640, 8, True)],
                      floating_lanes=[Lane([], 85, 5, False), Lane([], 130, 5, True),
                                      Lane([], 170, 5, False), Lane([], 215, 5, True), Lane([], 260, 5, False)],
                      background_image=get_background_image(0),
                      goat=Goat(400, 200),
                      amount_quiz=2,
                      quiz_cord=[375, 30],
                      music=0,
                      spawn_timer=[1000, 1000, 1000, 1000],
                      time_spawned=[pygame.time.get_ticks(), pygame.time.get_ticks(), pygame.time.get_ticks(),
                                    pygame.time.get_ticks()],
                      fl_spawn_timer=[1000, 2000, 1000, 2000, 1000, 2000],
                      fl_time_spawned=[tick, tick, tick, tick, tick, tick],
                      drown_cord=225,
                      sinking_cord=(85, 305),
                      safe_lanes=[]
                      )

    if level_number == 2:
        lane_9 = [Mob(150, 690, get_mob_sprite(False), False), Mob(300, 690, get_mob_sprite(False), False),
                  Mob(400, 690, get_mob_sprite(False), False),
                  Mob(600, 690, get_mob_sprite(False), False)]
        lane_8 = []
        lane_7 = []

        level = Level(lanes=[Lane([Mob(150, 55, get_mob_sprite(False), False)], 55, 8, False),
                             Lane([Mob(150, 115, get_mob_sprite(True), True)], 115, 8, True),
                             Lane([Mob(150, 185, get_mob_sprite(False), False)], 185, 8, False),

                             Lane([Mob(150, 315, get_mob_sprite(False), False)], 315, 8, False),
                             Lane([Mob(150, 375, get_mob_sprite(True), True)], 375, 8, True),
                             Lane([Mob(150, 430, get_mob_sprite(False), False)], 430, 8, False),

                             Lane([Mob(150, 570, get_mob_sprite(False), False)], 570, 8, False),
                             Lane([Mob(150, 625, get_mob_sprite(True), True)], 625, 8, True),
                             Lane(lane_9, 690, 8, False)],
                      background_image=get_background_image(1),
                      goat=Goat(400, 200),
                      music=0,
                      amount_quiz=3,
                      quiz_cord=[525, 270, 20],
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
        lane_9 = [Floating_mob(150, 690, get_floating_mob_sprite(False), False),
                  Floating_mob(300, 690, get_floating_mob_sprite(False), False),
                  Floating_mob(400, 690, get_floating_mob_sprite(False), False),
                  Floating_mob(600, 690, get_floating_mob_sprite(False), False)]
        lane_8 = []
        lane_7 = []

        level = Level(lanes=[],
                      floating_lanes=[
                          Lane([Floating_mob(150, 60, get_floating_mob_sprite(False), False)], 60, 5, False),
                          Lane([Floating_mob(150, 105, get_floating_mob_sprite(True), True)], 105, 5, True),
                          Lane([Floating_mob(150, 150, get_floating_mob_sprite(False), False)], 150, 5, False),
                          Lane([Floating_mob(150, 195, get_floating_mob_sprite(False), False)], 195, 5, False),

                          Lane([Floating_mob(150, 290, get_floating_mob_sprite(False), False)], 290, 5, False),
                          Lane([Floating_mob(150, 335, get_floating_mob_sprite(False), False)], 335, 5, False),
                          Lane([Floating_mob(150, 380, get_floating_mob_sprite(True), True)], 380, 5, True),
                          Lane([Floating_mob(150, 425, get_floating_mob_sprite(True), False)], 425, 5, False),
                          Lane([Floating_mob(150, 470, get_floating_mob_sprite(True), False)], 470, 5, False),

                          Lane([Floating_mob(150, 555, get_floating_mob_sprite(True), False)], 555, 5, False),
                          Lane([Floating_mob(150, 600, get_floating_mob_sprite(True), False)], 600, 5, False),
                          Lane([Floating_mob(150, 645, get_floating_mob_sprite(True), True)], 645, 5, True),
                          Lane(lane_9, 690, 5, False)],
                      safe_lanes=[
                          Lane([Floating_mob(150, 245, get_safe_floating_mob_sprite(True), False)], 245, 5, True),
                          Lane([Floating_mob(150, 510, get_safe_floating_mob_sprite(True), False)], 510, 5, False)],
                      background_image=get_background_image(2),
                      goat=Goat(400, 200),
                      music=0,
                      amount_quiz=3,
                      quiz_cord=[530, 275, 20],
                      fl_spawn_timer=[1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000, 1000],
                      fl_time_spawned=[tick, tick, tick, tick, tick, tick, tick, tick, tick, tick, tick, tick, tick],
                      drown_cord=0,
                      spawn_timer=[],
                      time_spawned=[],

                      sinking_cord=(60, 735)
                      )
    return level
