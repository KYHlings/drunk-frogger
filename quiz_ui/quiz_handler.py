import pygame
from random import shuffle
import html

import requests

from image.image_handler import get_get_quiz_sprite, get_quiz_box
from game_src.window_handler import screen, text_object

# loads quiz from json-file, in future will load from api.
def get_quiz():
    url = requests.get("https://opentdb.com/api.php?amount=50&category=15&difficulty=easy&type=multiple")
    content = url.json(encoding='utf8')['results']
    shuffle(content)
    return content


# unloads content from get_quiz function.
def quiz():
    while True:
        quiz_content = get_quiz()
        for q in quiz_content:
            if 80 < len(q['question']) < 85:
                return q["question"], "correct", q["incorrect_answers"]


def quiz_window(quiz,drunk_meter):
    # takes quiz function and draws on screen.
    font_list = ["PAPYRUS.TTF", "ConnectionSerif-d20X.otf","LcdSolid-VPzB.ttf","RdjHandPixel-5w3L.otf","VtcBadhangoverone-nnnO.ttf"]
    question, rightanswers, wronganswers = quiz
    question = html.unescape(question)
    rightanswers = html.unescape(rightanswers)
    question_list = [rightanswers]
    for wronganswer in wronganswers:
        question_list.append(html.unescape(wronganswer))
    shuffle(question_list)
    run = True
    keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
            pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
    while run:
        large_text = pygame.font.Font(f"font_src/{font_list[drunk_meter]}", 20)
        large_text1 = pygame.font.Font(f"font_src/{font_list[drunk_meter]}", 35)
        text_surf, text_rect = text_object(question, large_text)
        text_rect.center = (400, 460)
        goat_surf, goat_rect = text_object("The Wise Goat", large_text1)
        goat_rect.center = (230, 415)
        alternatives_text = []
        altnr = 0
        for alternative in question_list:
            alternatives_text.append(text_object(f"{altnr + 1}:{alternative}", large_text))
            altnr += 1
        # checks players answers
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                for i in range(len(question_list)):
                    if event.key == keys[i]:
                        return question_list[i] == rightanswers
        screen.blit(get_get_quiz_sprite(), (100, 150))
        screen.blit(get_quiz_box(), (-10, 330))
        screen.blit(goat_surf, goat_rect)
        screen.blit(text_surf, text_rect)
        alt_pos = 470
        for alternative_text in alternatives_text:
            alternative_text[1].topleft = (100, alt_pos)
            alt_pos += 30
            screen.blit(alternative_text[0], alternative_text[1])
        pygame.display.update()
