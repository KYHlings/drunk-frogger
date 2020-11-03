from game_src.game_loop import game_loop
from game_src.start_menu import start_menu
from music_and_sound.sound_handler import Sound_fx


def main():
    # This program runs the game
    volume = 0.1
    quiz_category = 9
    sound_fx = Sound_fx()
    volume,quiz_category = start_menu(sound_fx, volume,quiz_category)
    game_loop(sound_fx, volume,quiz_category)


if __name__ == '__main__':
    while True:
        main()

