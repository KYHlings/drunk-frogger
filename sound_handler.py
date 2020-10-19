import pygame


class Sound_fx:
    # This class saves all the sound effects in memory, so you don't have to load the file everytime it called
    def __init__(self):
        self.announcement_sound = get_announcement()
        self.splat_sound = get_splat()
        self.burp_sound = get_burp()

    def play_splat(self):
        return self.splat_sound.play()

    def play_burp(self):
        return self.burp_sound.play()

    def play_announcement(self):
        return self.announcement_sound.play()

def music_volume(volume):
    pygame.mixer.music.set_volume(volume)
# Each function gets a specific soundfile to load
def get_title_music():
    pygame.mixer.music.load("sounds_src/df_theme.mp3")
    return pygame.mixer.music.play(-1)


def get_level_music():
    pygame.mixer.music.load("sounds_src/df_level.mp3")
    return pygame.mixer.music.play(-1)


def get_goat_music():
    pygame.mixer.music.load("sounds_src/df_goat_music.mp3")
    return pygame.mixer.music.play(-1)


def get_win_music():
    pygame.mixer.music.load("sounds_src/df_win_music.mp3")
    return pygame.mixer.music.play(1)


def get_lose_music():
    pygame.mixer.music.load("sounds_src/df_die_music.mp3")
    return pygame.mixer.music.play(1)


def get_announcement():
    announcement = pygame.mixer.Sound("sounds_src/df-theme-announcer.ogg")
    return announcement


def get_splat():
    splat = pygame.mixer.Sound("sounds_src/splat2.ogg")
    return splat


def get_burp():
    burp = pygame.mixer.Sound("sounds_src/df_burp2.wav")
    return burp


# Loads different track depending on level of drunkness.
def get_drunk_music(drunken_meter):
    drunk_music_ls = ["df_level1_music_drunk1.mp3", "df_level1_music_drunk2.mp3", "df_level1_music_drunk3.mp3",
                      "df_level1_music_drunk4.mp3", "df_level1_music_drunk5.mp3", "df_level1_music_drunk6.mp3"]
    pygame.mixer.music.load(f"sounds_src/{drunk_music_ls[drunken_meter]}")
    return pygame.mixer.music.play(-1)


def get_credits():
    pygame.mixer.music.load("sounds_src/df_credits.mp3")
    pygame.mixer.music.play(-1)
