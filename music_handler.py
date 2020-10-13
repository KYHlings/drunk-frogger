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


def get_drunk_music(drunken_meter):
    drunk_music_ls = ["df_level1_music_drunk1.mp3", "df_level1_music_drunk2.mp3", "df_level1_music_drunk3.mp3",
                      "df_level1_music_drunk4.mp3", "df_level1_music_drunk5.mp3", "df_level1_music_drunk6.mp3"]
    pygame.mixer.music.load(drunk_music_ls[drunken_meter])
    pygame.mixer.music.set_volume(0.1)
    return pygame.mixer.music.play(-1)