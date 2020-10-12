from random import randint

import pygame
from quiz_handler import get_quiz
from image_handler import get_player_sprite, get_background_image, get_mob_sprite

pygame.init()



class Player(object):
    def __init__(self, player_x, player_y, width, height):
        self.player_x = player_x
        self.player_y = player_y
        self.width = width
        self.height = height
        self.velocity = 2
        self.hitbox = (self.player_x,self.player_y,width,height)


class Mob(object):
    def __init__(self, mob_x, mob_y, width, height):
        self.mob_x = mob_x
        self.mob_y = mob_y
        self.width = width
        self.height = height
        self.velocity = 2
        self.hitbox = (self.mob_x,self.mob_y,width,height)

def main():
    pygame.mixer.music.load("sounds_src/ph_bgm2.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    animals = Player(400, 570, 40, 30)
    cars = [Mob(0, 350, 80, 40), Mob(0, 400, 80, 40), Mob(0, 450, 80, 40)]
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Drunk Frogger")
    running = True

    now = [pygame.time.get_ticks(), pygame.time.get_ticks(), pygame.time.get_ticks()]
    mob_spawn_timer = [1000, 2000, 1000]
    lanes = [350, 400, 450]

    while running:
        screen.blit(get_background_image(), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for car in cars[:]:
            car.mob_x += car.velocity
            if car.mob_x >= 800:
                cars.remove(car)
        for i in range(3):
            if pygame.time.get_ticks() - now[i] >= mob_spawn_timer[i]:
                cars.append(Mob(0, lanes[i], 80, 40))
                now[i] = pygame.time.get_ticks()
                mob_spawn_timer[i] = randint(1000,2000)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a] and animals.player_x > animals.velocity:
            animals.player_x -= animals.velocity
        if keys[pygame.K_RIGHT] or keys[pygame.K_d] and animals.player_x < 800 - 40 - animals.velocity:
            animals.player_x += animals.velocity
        if keys[pygame.K_UP] or keys[pygame.K_w] and animals.player_y > animals.velocity:
            animals.player_y -= animals.velocity
        if keys[pygame.K_DOWN] or keys[pygame.K_s] and animals.player_y < 600 - 30 - animals.velocity:
            animals.player_y += animals.velocity
        if keys[pygame.K_ESCAPE]:
            running = False

        for i in range(len(cars)):
            screen.blit(get_mob_sprite(), (cars[i].mob_x, cars[i].mob_y))
            cars[i].hitbox = (cars[i].mob_x,cars[i].mob_y,cars[i].width,cars[i].height)
           # pygame.draw.rect(screen,(255,0,0),cars[i].hitbox,3)
        screen.blit(get_player_sprite(), (animals.player_x, animals.player_y))
        animals.hitbox = (animals.player_x,animals.player_y,animals.width,animals.height)
        #pygame.draw.rect(screen,(255,0,0),animals.hitbox,2)
        pygame.display.update()


if __name__ == '__main__':
    main()
