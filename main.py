import pygame
from image_handler import get_player_sprite, get_background_image, get_mob_sprite

pygame.init()


class Player(object):
    def __init__(self, player_x, player_y, width, height):
        self.player_x = player_x
        self.player_y = player_y
        self.width = width
        self.height = height
        self.velocity = 2


class Mob(object):
    def __init__(self, mob_x, mob_y, width, height):
        self.mob_x = mob_x
        self.mob_y = mob_y
        self.width = width
        self.height = height
        self.velocity = 2


def main():
    animals = Player(400, 570, 40, 30)
    cars = [Mob(0, 350, 80, 40), Mob(0, 400, 80, 40), Mob(0, 450, 80, 40)]
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Drunk Frogger")
    running = True

    while running:
        screen.blit(get_background_image(), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for i in range(len(cars)):
            cars[i].mob_x += cars[i].velocity
            if cars[i].mob_x == 720:
                cars[i].mob_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and animals.player_x > animals.velocity:
            animals.player_x -= animals.velocity
        if keys[pygame.K_RIGHT] and animals.player_x < 800 - 40 - animals.velocity:
            animals.player_x += animals.velocity
        if keys[pygame.K_DOWN] and animals.player_y < 600 - 30 - animals.velocity:
            animals.player_y += animals.velocity
        if keys[pygame.K_UP] and animals.player_y > animals.velocity:
            animals.player_y -= animals.velocity
        if keys[pygame.K_ESCAPE]:
            running = False

        for i in range(len(cars)):
            screen.blit(get_mob_sprite(), (cars[i].mob_x, cars[i].mob_y))
        screen.blit(get_player_sprite(), (animals.player_x, animals.player_y))
        pygame.display.update()


if __name__ == '__main__':
    main()
