from random import randint

import pygame
from quiz_handler import get_quiz
from image_handler import get_player_sprite, get_background_image, get_mob_sprite

pygame.init()

clock = pygame.time.Clock()




class Player():
    def __init__(self, player_x, player_y, width, height):
        self.player_x = player_x
        self.player_y = player_y
        self.width = width
        self.height = height
        self.velocity = 3
        self.hitbox = (self.player_x, self.player_y, width, height)

    def check_collide_x(self,mob):
        if self.player_x <= mob.mob_x:
            if self.player_x + self.width >= mob.mob_x:
                return True
            return False
        else:
            if mob.mob_x + mob.width >= self.player_x:
                return True
            return False

    def check_collide_y(self,mob):
        if self.player_y <= mob.mob_y:
            if self.player_y + self.height >= mob.mob_y:
                return True
            return False
        else:
            if mob.mob_y + mob.height <= self.player_y:
                return True
            return False
    def check_collide(self,mob):

        return self.check_collide_y(mob) and self.check_collide_x(mob)

    def reset(self):
        self.player_x = 400
        self.player_y = 570

class Mob():
    def __init__(self, mob_x, mob_y, width, height, image):
        self.mob_x = mob_x
        self.mob_y = mob_y
        self.image = image
        self.width = width
        self.height = height
        self.velocity = 4
        self.hitbox = (self.mob_x, self.mob_y, width, height)



def main():
    pygame.mixer.music.load("sounds_src/df_level.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    animals = Player(400, 570, 40, 30)
    cars = [Mob(0, 350, 80, 40, get_mob_sprite()), Mob(0, 400, 80, 40, get_mob_sprite()), Mob(0, 450, 80, 40, get_mob_sprite())]
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Drunk Frogger")
    running = True

    now = [pygame.time.get_ticks(), pygame.time.get_ticks(), pygame.time.get_ticks()]
    mob_spawn_timer = [1000, 2000, 1000]
    lanes = [350, 400, 450]

    while running:
        clock.tick(30)
        screen.blit(get_background_image(), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for car in cars[:]:
            if car.mob_y!= 400:
                car.mob_x += car.velocity
                if car.mob_x >= 800:
                    cars.remove(car)
            else:
                car.mob_x -= car.velocity
                if car.mob_x <= -50:
                    cars.remove(car)
        for i in range(3):
            if pygame.time.get_ticks() - now[i] >= mob_spawn_timer[i]:
                if lanes[i]!= 400:
                    cars.append(Mob(0, lanes[i], 80, 40, get_mob_sprite()))
                else:
                    cars.append(Mob(800, lanes[i], 80, 40, get_mob_sprite()))
                now[i] = pygame.time.get_ticks()
                mob_spawn_timer[i] = randint(1000, 2000)
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

        for car in cars:
            screen.blit(car.image, (car.mob_x, car.mob_y))
            car.hitbox = (car.mob_x, car.mob_y, car.width, car.height)
        pygame.draw.rect(screen,(255,0,0),car.hitbox,3)
        screen.blit(get_player_sprite(), (animals.player_x, animals.player_y))
        animals.hitbox = (animals.player_x, animals.player_y, animals.width, animals.height)
        pygame.draw.rect(screen,(255,0,0),animals.hitbox,2)
        for car in cars:
            if animals.check_collide(car):
                animals.reset()

        pygame.display.update()


if __name__ == '__main__':
    main()
