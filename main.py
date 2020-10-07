import pygame

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (37, 20))


def main():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Drunk Frogger")
    running = True
    screen.fill((0, 0, 0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


if __name__ == '__main__':
    main()
