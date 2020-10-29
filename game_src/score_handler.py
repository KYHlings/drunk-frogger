import pathlib
import json

def score_by_player_position(player_y, last_y, score):
    if player_y <= last_y:
        score += last_y - player_y
        last_y = player_y
        return score, last_y
    else:
        return score, last_y


def get_score():



def post_score():
    pass