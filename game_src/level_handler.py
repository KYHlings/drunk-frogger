from random import randint

import pygame

from image.image_handler import get_background_image, get_mob_sprite, get_floating_mob_sprite, \
    get_safe_floating_mob_sprite
from sprites_classes.npc import Mob, Floating_mob

tick = pygame.time.get_ticks()


class Level:
    def __init__(self, lanes, floating_lanes, background_image, spawn_timer, time_spawned,
                 fl_spawn_timer, fl_time_spawned, amount_quiz, quiz_cord, sinking_cord, safe_lanes, possible_spawn,
                 fl_possible_spawn):
        self.lanes = lanes
        self.floating_lanes = floating_lanes
        self.background_image = background_image
        self.spawn_timer = spawn_timer
        self.time_spawned = time_spawned
        self.fl_spawn_timer = fl_spawn_timer
        self.fl_time_spawned = fl_time_spawned
        self.amount_quiz = amount_quiz
        self.quiz_cord = quiz_cord
        self.sinking_cord = sinking_cord
        self.safe_lanes = safe_lanes
        self.possible_spawn = possible_spawn
        self.fl_possible_spawn = fl_possible_spawn

    def spawn_paused(self):
        # Saves the time when the game pauses
        self.time_of_pause = pygame.time.get_ticks()

    def spawn_resumed(self):
        # Adds the time that has been spent while the game been paused to the spawn_timer
        extra_time = pygame.time.get_ticks() - self.time_of_pause
        for i in range(len(self.spawn_timer)):
            self.spawn_timer[i] += extra_time
        for i in range(len(self.fl_spawn_timer)):
            self.fl_spawn_timer[i] += extra_time

    def move_mobs(self):
        # Moves mobs left and right. Removes after leaving window
        for lane in self.lanes + self.floating_lanes:
            for mob in lane.mobs[:]:
                if not mob.is_left:
                    mob.update_rect(1, lane.velocity)
                    if mob.mob_x >= 1280:
                        lane.mobs.remove(mob)
                else:
                    mob.update_rect(-1, lane.velocity)
                    if mob.mob_x <= -60:
                        lane.mobs.remove(mob)

        for lane in self.safe_lanes:
            for floating_mob in lane.floating_mobs[:]:
                if not floating_mob.is_left:
                    floating_mob.update_rect(1, lane.velocity)
                    if floating_mob.mob_x >= 1020 or floating_mob.mob_x <= -10:
                        lane.velocity *= -1

    def spawn_mobs(self):
        # Spawns the mobs
        for i in range(len(self.lanes)):
            if pygame.time.get_ticks() - self.time_spawned[i] >= self.spawn_timer[i]:
                if not self.lanes[i].is_left:
                    self.lanes[i].mobs.append(
                        Mob(-220, self.lanes[i].y, get_mob_sprite(False),
                            self.lanes[i].is_left))  # sätter ett gem :P
                else:
                    self.lanes[i].mobs.append(
                        Mob(1280, self.lanes[i].y, get_mob_sprite(True), self.lanes[i].is_left))
                self.time_spawned[i] = pygame.time.get_ticks()
                self.spawn_timer[i] = randint(self.possible_spawn[i][0], self.possible_spawn[i][1])

        for i in range(len(self.floating_lanes)):
            if pygame.time.get_ticks() - self.fl_time_spawned[i] >= self.fl_spawn_timer[i]:
                if not self.floating_lanes[i].is_left:
                    self.floating_lanes[i].floating_mobs.append(
                        Floating_mob(-60, self.floating_lanes[i].y, get_floating_mob_sprite(False),
                                     self.floating_lanes[i].is_left))
                else:
                    self.floating_lanes[i].floating_mobs.append(
                        Floating_mob(1280, self.floating_lanes[i].y, get_floating_mob_sprite(True),
                                     self.floating_lanes[i].is_left))
                self.fl_time_spawned[i] = pygame.time.get_ticks()
                self.fl_spawn_timer[i] = randint(self.fl_possible_spawn[i][0], self.fl_possible_spawn[i][1])


class Lane:

    def __init__(self, mobs, y, velocity, is_left):
        self.mobs = mobs
        self.y = y
        self.velocity = velocity
        self.is_left = is_left
        self.floating_mobs = mobs


def create_level(level_number):
    # Creates the level objects according to the level number
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

        level = Level(lanes=[Lane(lane_1, 445, 2, False),
                             Lane(lane_2, 510, 10, True),
                             Lane(lane_3, 570, 12, False),
                             Lane(lane_4, 640, 6, True)],
                      floating_lanes=[Lane([], 85, 3, True), Lane([], 130, 5, False),
                                      Lane([], 170, 10, False), Lane([], 215, 6, True), Lane([], 260, 8, False)],
                      background_image=get_background_image(0),
                      amount_quiz=2,
                      quiz_cord=[375, 30],
                      spawn_timer=[1000, 1000, 1000, 1000],
                      time_spawned=[tick, tick, tick, tick],
                      fl_spawn_timer=[1000, 2000, 1000, 2000, 1000, 2000],
                      fl_time_spawned=[tick, tick, tick, tick, tick, tick],
                      sinking_cord=(85, 305),
                      safe_lanes=[],
                      possible_spawn=[(3200, 4200), (800, 1700), (700, 1500), (1000, 2000)],
                      fl_possible_spawn=[(3000, 4000), (1000, 2000), (500, 1700), (1000, 2000), (1000, 2000),
                                         (500, 1200)])

    if level_number == 2:
        lane_9 = [Mob(150, 690, get_mob_sprite(False), False), Mob(300, 690, get_mob_sprite(False), False),
                  Mob(400, 690, get_mob_sprite(False), False),
                  Mob(600, 690, get_mob_sprite(False), False)]
        lane_8 = []
        lane_7 = []

        level = Level(lanes=[Lane([Mob(150, 55, get_mob_sprite(False), False)], 55, 2, False),
                             Lane([Mob(150, 115, get_mob_sprite(True), True)], 115, 5, True),
                             Lane([Mob(150, 185, get_mob_sprite(True), True)], 185, 10, True),

                             Lane([Mob(150, 315, get_mob_sprite(False), False)], 315, 4, False),
                             Lane([Mob(150, 375, get_mob_sprite(True), True)], 375, 14, True),
                             Lane([Mob(150, 430, get_mob_sprite(False), False)], 430, 7, False),

                             Lane([Mob(150, 570, get_mob_sprite(False), False)], 570, 8, False),
                             Lane([Mob(150, 625, get_mob_sprite(True), True)], 625, 8, True),
                             Lane(lane_9, 690, 8, False)],
                      background_image=get_background_image(1),
                      amount_quiz=3,
                      quiz_cord=[525, 270, 20],
                      spawn_timer=[1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000, 1000],
                      time_spawned=[tick, tick, tick, tick, tick, tick, tick, tick, tick],
                      fl_spawn_timer=[],
                      fl_time_spawned=[],
                      floating_lanes=[],
                      sinking_cord=(0, 0),
                      safe_lanes=[],
                      possible_spawn=[(3000, 4000), (1500, 2500), (700, 1600),
                                      (1800, 2700), (500, 1600), (1200, 1800),
                                      (1000, 2000), (2000, 3000), (1000, 2000)],
                      fl_possible_spawn=[]
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
                          Lane([Floating_mob(150, 150, get_floating_mob_sprite(False), False)], 150, 10, False),
                          Lane([Floating_mob(150, 195, get_floating_mob_sprite(False), False)], 195, 5, False),

                          Lane([Floating_mob(150, 290, get_floating_mob_sprite(False), False)], 290, 5, False),
                          Lane([Floating_mob(150, 335, get_floating_mob_sprite(False), False)], 335, 9, False),
                          Lane([Floating_mob(150, 380, get_floating_mob_sprite(True), True)], 380, 5, True),
                          Lane([Floating_mob(150, 425, get_floating_mob_sprite(True), False)], 425, 20, False),
                          Lane([Floating_mob(150, 470, get_floating_mob_sprite(True), False)], 470, 3, False),

                          Lane([Floating_mob(150, 555, get_floating_mob_sprite(True), False)], 555, 5, False),
                          Lane([Floating_mob(150, 600, get_floating_mob_sprite(True), False)], 600, 10, False),
                          Lane([Floating_mob(150, 645, get_floating_mob_sprite(True), True)], 645, 5, True),
                          Lane(lane_9, 690, 5, False)],
                      safe_lanes=[
                          Lane([Floating_mob(150, 245, get_safe_floating_mob_sprite(True), False)], 245, 5, False),
                          Lane([Floating_mob(150, 510, get_safe_floating_mob_sprite(True), False)], 510, 5, False)],
                      background_image=get_background_image(2),
                      amount_quiz=3,
                      quiz_cord=[530, 275, 20],
                      fl_spawn_timer=[1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000, 1000],
                      fl_time_spawned=[tick, tick, tick, tick, tick, tick, tick, tick, tick, tick, tick, tick, tick],
                      spawn_timer=[],
                      time_spawned=[],
                      sinking_cord=(60, 735),
                      fl_possible_spawn=[(1000, 2000), (1000, 2000), (1000, 2000), (1000, 2000),
                                         (1000, 2000), (1000, 2000), (1000, 2000), (250,1000 ), (2000, 3000),
                                         (1000, 2000), (1000, 2000), (1000, 2000), (1000, 2000)],
                      possible_spawn=[]

                      )
    return level
