import pygame
def get_level_music():
    pygame.mixer.music.load("sounds_src/df_level.mp3")
    pygame.mixer.music.set_volume(0.1)
    return pygame.mixer.music.play(-1)

def get_goat_music():
    pygame.mixer.music.load("sounds_src/df_goat_music.mp3")
    pygame.mixer.music.set_volume(0.1)
    return pygame.mixer.music.play(-1)

def get_splat():
    splat = pygame.mixer.Sound("sounds_src/splat.wav")
    pygame.mixer.music.set_volume(0.1)
    return splat.play(0, 0, 0)
