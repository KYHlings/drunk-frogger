import sys
from pathlib import Path
import json

from game_src.window_handler import draw_text
from game_src.variabels import *


def score_by_player_position(player_y, last_y, score):
    # takes player postition and returns score.
    if player_y <= last_y:
        score += last_y - player_y
        last_y = player_y
        return score, last_y
    else:
        return score, last_y


def get_score():
    #gets score file.
    score_ls = json.loads(Path("game_src/highscore.json").read_text(encoding='utf8'))
    return score_ls


def high_score_list(score):
    # Checks if player has enough score to be on high score list. Shows the list afterwards
    score_ls = get_score()
    if score_ls[9]["score"] < score:
        score_ls[9]["score"] = score
        name = write_highscore()
        score_ls[9]["name"] = name
        sorted_score = sorted(score_ls, key=lambda s: s['score'], reverse=True)
        Path("game_src/highscore.json").write_text(json.dumps(sorted_score), encoding='utf8')
    score_window()


def write_highscore():
    # Player can add their name to the highscore
    user_name = ""
    while True:
        screen.fill(BLACK)
        draw_text("Enter your name", score_font, WHITE, screen, 630, 60,'center')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]
                elif event.key == pygame.K_RETURN:
                    return user_name
                else:
                    user_name += event.unicode

        draw_text(user_name, score_font, WHITE, screen, 640, 130,'center')
        pygame.display.update()


def score_window():
    # Shows the highscore
    score_ls = get_score()
    screen.fill(WHITE)
    while True:
        score_y = 100
        draw_text("High score", score_font, BLACK, screen, 600, 40,'center')
        draw_text("Any key to return",key_font,BLACK,screen,1270,10,"topright")
        for nr, score in enumerate(score_ls, 1):
            draw_text(f"{nr:2}. {score['name']:12} : {score['score']:5}", score_font, BLACK, screen, 285, score_y,'topleft')
            score_y += 70
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

            pygame.display.update()
