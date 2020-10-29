import sys
from pathlib import Path
import json

import pygame

from game_src.window_handler import screen, text_object, score_font


def score_by_player_position(player_y, last_y, score):
    if player_y <= last_y:
        score += last_y - player_y
        last_y = player_y
        return score, last_y
    else:
        return score, last_y


def get_score():
    score_ls = json.loads(Path("game_src/highscore.json").read_text(encoding='utf8'))
    return score_ls


def high_score_list(score):
    score_ls = get_score()
    if score_ls[9]["score"] < score:
        write_highscore()
        score_ls[9]["score"] = score
        name = input("enter name: ")
        score_ls[9]["name"] = name
        sorted_score = sorted(score_ls, key=lambda s: s['score'], reverse=True)
        Path("game_src/highscore.json").write_text(json.dumps(sorted_score), encoding='utf8')


def write_highscore():
    user_name = ""
    while True:
        screen.fill((250, 250, 250))
        inst_surf, inst_rect = text_object("Congratulations. Enter your name", score_font)
        inst_rect.center = (400, 60)
        screen.blit(inst_surf, inst_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]
                elif event.key == pygame.K_RETURN:
                    return
                else:
                    user_name += event.unicode


        name_surf, name_rect = text_object(user_name, score_font)
        name_rect.center = (400, 100)
        print(user_name)
        screen.blit(name_surf, name_rect)

        pygame.display.update()


def score_window():
    score_ls = get_score()
    screen.fill((250, 250, 250))
    while True:
        nr = 1
        score_y = 100
        hs_surf, hs_rect = text_object("High score", score_font)
        hs_rect.center = (400, 60)
        screen.blit(hs_surf, hs_rect)
        for score in score_ls:
            score_surfing, score_rect = text_object(f"{nr}:{score['name']} : {score['score']}", score_font)
            nr += 1
            score_rect.center = 400, score_y
            score_y += 40
            screen.blit(score_surfing, score_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

            pygame.display.update()
