from image.image_handler import main_menu_image
from music_and_sound.sound_handler import music_volume
from game_src.window_handler import draw_text
from game_src.variabels import *


def sound_settings(volume_float):
    #allows player to change sound volume
    running = True
    volume_int = int(volume_float * 10)
    while running:
        volume_float = float(volume_int) / 10
        volume_rect_x = 450
        screen.blit(main_menu_image(), (0, 0))
        draw_text("Settings", font, BLACK, screen, 400, 100,'topleft')
        draw_text("Change volume [-][+]", font1, BLACK, screen, 400, 300,'topleft')
        draw_text("Enter to return",font1,BLACK,screen,50,700,"topleft")
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                # Allows keyboard input to change sound volume
                if event.key == pygame.K_MINUS and volume_int > 0:
                    volume_int -= 1
                if event.key == pygame.K_PLUS and volume_int <= 5:
                    volume_int += 1
                if event.key == pygame.K_RETURN:
                    return volume_float
                if event.key == pygame.K_ESCAPE:
                    return False
            if event.type == pygame.QUIT:
                quit()
        # Changes the volume bars
        for i in range(volume_int):
            volume_rect = pygame.Rect(volume_rect_x, 420, 20, 50)
            volume_rect_x += 50
            pygame.draw.rect(screen, BLACK, volume_rect)
        music_volume(volume_float)
        pygame.display.update()


if __name__ == '__main__':
    sound_settings(0.1)
