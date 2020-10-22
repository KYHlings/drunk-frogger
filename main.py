from game_src.game_loop import game_loop
from game_src.start_menu import start_menu
from music_and_sound.sound_handler import Sound_fx


def main():
    volume = 0.1
    sound_fx = Sound_fx()
    start_menu(sound_fx, volume)
    game_loop(sound_fx, volume)


if __name__ == '__main__':
    while True:
        main()
#This program runs the game