from pathlib import Path
import json

from game_src.window_handler import write_highscore


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
        sorted_score = sorted(score_ls,key=lambda s:s['score'],reverse=True)
        Path("game_src/highscore.json").write_text(json.dumps(sorted_score),encoding='utf8')

