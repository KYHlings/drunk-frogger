from random import randint

import pygame

from image_handler import get_player_sprite, get_get_sprite, get_mob_sprite, get_background_image, get_life_sprite

from npc import Mob, Get
from player import Player
from quiz_handler import quiz_window, quiz
from sound_handler import get_level_music, get_goat_music, get_drunk_music
from window_handler import screen, lose_window, win_window


# This function updates the window with sprites each loop
def redraw_window(cars, animals, wise_goat):
    life_x = 10
    for i in range(animals.lives):
        screen.blit(get_life_sprite(), (life_x, 10))
        life_x += 25
    for car in cars:
        screen.blit(car.image, (car.mob_rect))
        car.hitbox = (car.mob_x + 6, car.mob_y + 7, 69, 30)
        # pygame.draw.rect(screen, (255, 0, 0), car.hitbox, 3)
    screen.blit(animals.update_img()[0],animals.update_img()[1])
    screen.blit(get_get_sprite(), (animals.player_x - 20, wise_goat.get_y))
    pygame.display.update()

#This function runs the main game
def game_loop(sound_fx):

    clock = pygame.time.Clock()
    get_level_music()
    animals = Player(400, 570, 40, 30, 0,get_player_sprite(0))
    cars = [Mob(0, 350, 80, 40, get_mob_sprite(False)), Mob(0, 400, 80, 40, get_mob_sprite(True)),
            Mob(0, 450, 80, 40, get_mob_sprite(False))]
    wise_goat = Get(animals.player_x, 200, 40, 30)
    pygame.display.set_caption("Drunk Frogger")
    running = True

    now = [pygame.time.get_ticks(), pygame.time.get_ticks(), pygame.time.get_ticks()]
    mob_spawn_timer = [1000, 2000, 1000]
    lanes = [350, 400, 450]
    q = False
    while running:
        clock.tick(30)
        screen.blit(get_background_image(), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for car in cars[:]:
            if car.mob_y != 400:
                car.update_rect(1)
                if car.mob_x >= 800:
                    cars.remove(car)
            else:
                car.update_rect(-1)
                if car.mob_x <= -50:
                    cars.remove(car)
        for i in range(3):
            if pygame.time.get_ticks() - now[i] >= mob_spawn_timer[i]:
                if lanes[i] != 400:
                    cars.append(Mob(0, lanes[i], 80, 40, get_mob_sprite(False)))
                else:
                    cars.append(Mob(800, lanes[i], 80, 40, get_mob_sprite(True)))
                now[i] = pygame.time.get_ticks()
                mob_spawn_timer[i] = randint(1000, 2000)
        keys = pygame.key.get_pressed()
        animals.move(keys)
        if keys[pygame.K_ESCAPE]:
            running = False

        for car in cars:
            if animals.check_collide(car):
                if animals.lives == 0:
                    lose_window()
                sound_fx.play_splat()
                animals.reset()

                #This if statement checks if the player has reached the safe zone and triggers the quiz function
        if animals.player_y <= 300 and q == False:
            get_goat_music()

            #This if statement checks if the player answers correctly. If the player answers correctly they trigger the win function
            #if they do not answer correctly they get moved to the start position and adds one to the drunk_meter integer
            if not quiz_window(quiz()):
                if animals.drunk_meter == 3:
                    lose_window()
                animals.drunk_meter += 1
                sound_fx.play_burp()
                animals.drunken_consequence()
                get_drunk_music(animals.drunk_meter)
                animals.reset()
                q = False
            else:
                win_window()

        redraw_window(cars, animals, wise_goat)
