import pygame
from image_handler import get_player_sprite

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = get_player_sprite()


def main():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Drunk Frogger")
    running = True
    screen.fill((0, 0, 0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(get_player_sprite(), (400, 300))
        pygame.display.update()
    velocity = 10

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] :
        pass




if __name__ == '__main__':
    main()
