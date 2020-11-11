import pygame
from random import choice


class Sound_fx:
    # This class saves all the sound effects in memory, so you don't have to load the file everytime it called
    def __init__(self):
        self.announcement_sound = get_announcement()
        self.splat_sounds = get_splat()
        #self.burp_sounds = get_burp()
        self.burp_sounds = get_beer_cheer() ##
        self.splash_sounds = get_splash()
        self.falling_sounds = get_falling()

    def play_splat(self):
        splat_sound = choice(self.splat_sounds)
        pygame.mixer.Sound.set_volume(splat_sound, 0.4)
        return splat_sound.play()

    def play_splash(self):
        splash_sound = choice(self.splash_sounds)
        pygame.mixer.Sound.set_volume(splash_sound, 0.2)
        return splash_sound.play()


########################
    def play_burp(self):
        burp_sound = choice(self.burp_sounds)
        pygame.mixer.Sound.set_volume(burp_sound, 0.2)
        return burp_sound.play()
######
#    def play_burp(self):
#        burp_sound = choice(self.burp_sounds)
#        pygame.mixer.Sound.set_volume(burp_sound, 0.2)
#        return burp_sound.play()
#########################


    def play_falling(self):
        falling_sound = choice(self.falling_sounds)
        pygame.mixer.Sound.set_volume(falling_sound, 0.03)
        return falling_sound.play()

    def play_announcement(self):
        pygame.mixer.Sound.set_volume(self.announcement_sound, 0.1)
        return self.announcement_sound.play()


def music_volume(volume):
    pygame.mixer.music.set_volume(volume)


###
# Each function gets a specific soundfile to load

def get_title_music():
    pygame.mixer.music.load("music_and_sound/music_src/df_theme_music2.mp3")
    return pygame.mixer.music.play(-1)


#########################
def get_level_music(level_number):
    music_files = ["intro_song_1.mp3", "battle_time_1.mp3", "df_level3_music.mp3"]
    pygame.mixer.music.load(f"music_and_sound/music_src/{music_files[level_number-1]}")
    return pygame.mixer.music.play(-1)
######
#def get_level_music(level_number):
#    music_files = ["df_level1.2_music.mp3", "df_level2_music.mp3", "df_level3_music.mp3"]
#    pygame.mixer.music.load(f"music_and_sound/music_src/{music_files[level_number - 1]}")
#    return pygame.mixer.music.play(-1)
#########################

#########################

######
#def get_goat_music():
#    pygame.mixer.music.load("music_and_sound/music_src/df_goat_music2.mp3")
#    return pygame.mixer.music.play(-1)
#########################
def get_goat_music():
    pygame.mixer.music.load("music_and_sound/music_src/new_music/quizz_music.mp3") #    pygame.mixer.music.load("music_and_sound/music_src/df_goat_music2.mp3")
    return pygame.mixer.music.play(-1)
#########################


#########################
def get_win_music():
    pygame.mixer.music.load("music_and_sound/music_src/new_music/kids_cheering.mp3") #    pygame.mixer.music.load("music_and_sound/music_src/df_win_music.mp3")
    return pygame.mixer.music.play(1)
######
#def get_win_music():
#    pygame.mixer.music.load("music_and_sound/music_src/df_win_music.mp3")
#    return pygame.mixer.music.play(1)
#########################


#########################
def get_lose_music():
    pygame.mixer.music.load("music_and_sound/music_src/new_music/lose_game_melody.mp3")
    return pygame.mixer.music.play(1)
######
#def get_lose_music():
#    pygame.mixer.music.load("music_and_sound/music_src/df_die_music.mp3")
#    return pygame.mixer.music.play(1)
#########################


####
def get_credits_music():
    pygame.mixer.music.load("music_and_sound/music_src/df_credits.mp3")
    return pygame.mixer.music.play(1)


# Loads different track depending on level of drunkness.
#########################
def get_drunk_music(level_number, drunken_meter):
    drunk_music_ls =[["intro_song_drunk_1.mp3", "intro_song_drunk_2.mp3", "intro_song_drunk_3.mp3",
                      "song_level_drunk_4.mp3"],["battle_time_1.mp3", "Battle_time_drunk_2.mp3", "df_level2_music_drunk3.mp3",
                      "df_level2_music_drunk4.mp3"],["df_level3_music_drunk1.mp3","df_level3_music_drunk2.mp3","df_level3_music_drunk3.mp3","df_level3_music_drunk4.mp3"]]
    pygame.mixer.music.load(f"music_and_sound/music_src/{drunk_music_ls[level_number-1][drunken_meter-1]}")
    return pygame.mixer.music.play(-1)
######
#def get_drunk_music(level_number, drunken_meter):
#    drunk_music_ls = [["df_level1.2_music_drunk1.mp3", "df_level1.2_music_drunk2.mp3", "df_level1.2_music_drunk3.mp3",
#                       "df_level1.2_music_drunk4.mp3"],
#                      ["df_level2_music_drunk1.mp3", "df_level2.2_drunk2.mp3", "df_level2_music_drunk3.mp3",
#                       "df_level2_music_drunk4.mp3"],
#                      ["df_level3_music_drunk1.mp3", "df_level3_music_drunk2.mp3", "df_level3_music_drunk3.mp3",
#                       "df_level3_music_drunk4.mp3"]]
#    pygame.mixer.music.load(f"music_and_sound/music_src/{drunk_music_ls[level_number - 1][drunken_meter - 1]}")
#    return pygame.mixer.music.play(-1)
#########################


def get_credits():
    # Adds credits music
    pygame.mixer.music.load("music_and_sound/music_src/df_credits.mp3")
    pygame.mixer.music.play(-1)


#########################
def get_announcement():
    #Adds announcement
    announcement = pygame.mixer.Sound("music_and_sound/sounds_fx_src/drunk_pica_announce.mp3")
    return announcement
######
#def get_announcement():
#    # Adds announcement
#    announcement = pygame.mixer.Sound("music_and_sound/sounds_fx_src/df-theme-announcer.ogg")
#    return announcement
#########################


def get_splat():
    # Adds sound-fx when colliding with car
    splat_files = ["df_splat1.ogg", "df_splat2.ogg", "df_splat3.ogg"]
    splat_fx = []
    for s in splat_files:
        splat_fx.append(pygame.mixer.Sound(f"music_and_sound/sounds_fx_src/{s}"))
    return splat_fx


#########################
def get_beer_cheer():
    #Adds sound-fx when drunk
    burp_files = ["dinosaur_growl.mp3", "mahna_na_2.mp3", "mahna_na_3.mp3"]
    burp_fx = []
    for b in burp_files:
        burp_fx.append(pygame.mixer.Sound(f"music_and_sound/sounds_fx_src/{b}"))
    return burp_fx
######
#def get_burp():
#    # Adds sound-fx when drunk
#    burp_files = ["df_burp1.ogg", "df_burp2.wav", "df_burp3.ogg"]
#    burp_fx = []
#    for b in burp_files:
#        burp_fx.append(pygame.mixer.Sound(f"music_and_sound/sounds_fx_src/{b}"))
#    return burp_fx
#########################


def get_splash():
    # Adds sound-fx when falling into water
    splash_files = ["df_water_splash.ogg"]
    splash_fx = []
    for s in splash_files:
        splash_fx.append(pygame.mixer.Sound(f"music_and_sound/sounds_fx_src/{s}"))
    return splash_fx


def get_falling():
    # Adds sound-fx when falling into space
    falling_files = ["df_falling_short.mp3", "df_falling_pitch_short.mp3"]
    falling_fx = []
    for s in falling_files:
        falling_fx.append(pygame.mixer.Sound(f"music_and_sound/sounds_fx_src/{s}"))
    return falling_fx
