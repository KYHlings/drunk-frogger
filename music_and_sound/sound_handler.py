import pygame
from random import choice


class Sound_fx:
    # This class saves all the sound effects in memory, so you don't have to load the file everytime it called
    def __init__(self):
        self.announcement_sound = get_announcement()
        self.splat_sounds = get_splat()
        self.burp_sounds = get_burp()

    def play_splat(self):
        splat_sound = choice(self.splat_sounds)
        pygame.mixer.Sound.set_volume(splat_sound,0.4)
        return splat_sound.play()

    def play_burp(self):
        burp_sound = choice(self.burp_sounds)
        pygame.mixer.Sound.set_volume(burp_sound,0.2)
        return burp_sound.play()

    def play_announcement(self):
        return self.announcement_sound.play()


def music_volume(volume):
    pygame.mixer.music.set_volume(volume)


# Each function gets a specific soundfile to load
def get_title_music():
    pygame.mixer.music.load("music_and_sound/music_src/df_theme.mp3")
    return pygame.mixer.music.play(-1)


def get_level_music():
    pygame.mixer.music.load("music_and_sound/music_src/df_level.mp3")
    return pygame.mixer.music.play(-1)


def get_goat_music():
    pygame.mixer.music.load("music_and_sound/music_src/df_goat_music.mp3")
    return pygame.mixer.music.play(-1)


def get_win_music():
    pygame.mixer.music.load("music_and_sound/music_src/df_win_music.mp3")
    return pygame.mixer.music.play(1)


def get_lose_music():
    pygame.mixer.music.load("music_and_sound/music_src/df_die_music.mp3")
    return pygame.mixer.music.play(1)


# Loads different track depending on level of drunkness.
def get_drunk_music(drunken_meter):
    drunk_music_ls = ["df_level1_music_drunk1.mp3", "df_level1_music_drunk2.mp3", "df_level1_music_drunk3.mp3",
                      "df_level1_music_drunk4.mp3", "df_level1_music_drunk5.mp3", "df_level1_music_drunk6.mp3"]
    pygame.mixer.music.load(f"music_and_sound/music_src/{drunk_music_ls[drunken_meter]}")
    return pygame.mixer.music.play(-1)


def get_credits():
    pygame.mixer.music.load("music_and_sound/music_src/df_credits.mp3")
    pygame.mixer.music.play(-1)


def get_announcement():
    announcement = pygame.mixer.Sound("music_and_sound/sounds_fx_src/df-theme-announcer.ogg")
    return announcement


def get_splat():
    splat_files = ["df_splat1.ogg", "df_splat2.ogg", "df_splat3.ogg"]
    splat_fx = []
    for s in splat_files:
        splat_fx.append(pygame.mixer.Sound(f"music_and_sound/sounds_fx_src/{s}"))
    return splat_fx


def get_burp():
    burp_files = ["df_burp1.ogg", "df_burp2.wav", "df_burp3.ogg"]
    burp_fx = []
    for b in burp_files:
        burp_fx.append(pygame.mixer.Sound(f"music_and_sound/sounds_fx_src/{b}"))
    return burp_fx
