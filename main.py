import pygame
pygame.init()

def main():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Drunk Frogger")
    running = True
    screen.fill((0,0,0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


if __name__ == '__main__':
    main()