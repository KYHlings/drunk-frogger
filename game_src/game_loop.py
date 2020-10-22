from random import randint

import pygame

from game_src.level import create_level
from sprites_classes.dead_frog import Dead_Frog
from image.image_handler import get_player_sprite, get_get_sprite, get_mob_sprite, \
    get_life_sprite, get_dead_sprite, get_beer_sprite

from sprites_classes.npc import Mob, Goat
from sprites_classes.player import Player
from quiz_ui.quiz_handler import quiz_window, quiz
from game_src.settings import Sound_settings
from music_and_sound.sound_handler import get_level_music, get_goat_music, get_drunk_music
from game_src.window_handler import screen, lose_window, win_window


# This function updates the window with sprites_classes each loop
def redraw_window(cars, animals, wise_goat, dead_frog, background_image):
    screen.blit(background_image, (0, 0))
    life_x = 10
    beer_x = 10
    for i in range(animals.drunk_meter):
        screen.blit(get_beer_sprite(), (beer_x, 20))
        beer_x += 25
    for i in range(animals.lives):
        screen.blit(get_life_sprite(), (life_x, 10))
        life_x += 25
    if dead_frog.is_dead:
        screen.blit(dead_frog.img, (dead_frog.dead_x, dead_frog.dead_y))
        screen.blit(animals.update_img()[0], (1000, 1000))

    else:
        screen.blit(animals.update_img()[0], animals.update_img()[1])
    for car in cars:
        screen.blit(car.image, (car.mob_rect))
        car.hitbox = (car.mob_x + 6, car.mob_y + 7, 69, 30)
        # pygame.draw.rect(screen, (255, 0, 0), car.hitbox, 3)
    screen.blit(get_get_sprite(), (animals.player_x - 20, wise_goat.get_y))
    pygame.display.update()


# This function runs the main game
def game_loop(sound_fx, volume):
    clock = pygame.time.Clock()
    get_level_music()
    animals = Player(400, 570, 40, 30, 0, get_player_sprite(0))
    dead_frog = Dead_Frog()
    wise_goat = Goat(animals.player_x, 200, 40, 30)
    pygame.display.set_caption("Drunk Frogger")
    running = True

    q = False

    level_number = 1
    while True:
        level = create_level(level_number)
        running = True
        while running:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            for car in level.mobs[:]:
                if car.mob_y != 400:
                    car.update_rect(1)
                    if car.mob_x >= 800:
                        level.mobs.remove(car)
                else:
                    car.update_rect(-1)
                    if car.mob_x <= -50:
                        level.mobs.remove(car)
            for i in range(3):
                if pygame.time.get_ticks() - level.time_spawned[i] >= level.spawn_timer[i]:
                    if level.lanes[i] != 400:
                        level.mobs.append(Mob(0, level.lanes[i], 80, 40, get_mob_sprite(False)))
                    else:
                        level.mobs.append(Mob(800, level.lanes[i], 80, 40, get_mob_sprite(True)))
                    level.time_spawned[i] = pygame.time.get_ticks()
                    level.spawn_timer[i] = randint(1000, 2000)
            keys = pygame.key.get_pressed()
            if dead_frog.is_dead:
                dead_frog.check_time_of_death()
            else:
                animals.move(keys)
            if keys[pygame.K_p]:
                volume = Sound_settings(volume)
                if not volume:
                    return

            for car in level.mobs:
                if animals.check_collide(car):
                    if animals.lives == 0:
                        lose_window()
                        return
                    else:
                        dead_frog.player_died(animals.player_x, animals.player_y)
                        sound_fx.play_splat()
                        animals.reset()

                    # This if statement checks if the player has reached the safe zone and triggers the quiz function
            if animals.player_y <= 300 and q == False:
                get_goat_music()

                # This if statement checks if the player answers correctly. If the player answers correctly they trigger the win function
                # if they do not answer correctly they get moved to the start position and adds one to the drunk_meter integer
                if not quiz_window(quiz()):
                    if animals.drunk_meter == 3:
                        lose_window()
                        return
                    animals.drunk_meter += 1
                    dead_frog.img = get_dead_sprite(animals.drunk_meter)
                    sound_fx.play_burp()
                    animals.drunken_consequence()
                    get_drunk_music(animals.drunk_meter)
                    animals.reset()
                    q = False
                else:
                    win_window()
                    animals.reset()
                    running = False

            redraw_window(level.mobs, animals, wise_goat, dead_frog, level.background_image)
        level_number += 1
        if level_number == 3:
            level_number = 1
