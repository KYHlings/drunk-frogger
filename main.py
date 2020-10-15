from game_loop import game_loop
from start_menu import main_menu
from sound_handler import Sound_fx


def main():
    sound_fx = Sound_fx()
    main_menu(sound_fx)
    game_loop(sound_fx)


if __name__ == '__main__':
    main()
