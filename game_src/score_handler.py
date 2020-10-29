from pathlib import Path
import json

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

def post_score():
    pass


