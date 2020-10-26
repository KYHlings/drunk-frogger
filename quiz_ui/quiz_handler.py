import pygame
from random import shuffle
from pathlib import Path
import json

import requests

from image.image_handler import get_get_sprite, get_get_quiz_sprite
from game_src.window_handler import screen,text_object

#loads quiz from json-file, in future will load from api.
def get_quiz():
    url = requests.get("https://opentdb.com/api.php?amount=25&category=15&difficulty=medium&type=multiple")
    content = url.json(encoding='utf8')['results']
    shuffle(content)
    return content

#unloads content from get_quiz function.
def quiz():
    quiz_content=get_quiz()
    for q in quiz_content:
        return q["question"],q["correct_answer"],q["incorrect_answers"]


def quiz_window(quiz):
    #takes quiz function and draws on screen.
    question, rightanswers, wronganswers = quiz
    question_list = [rightanswers]
    for wronganswer in wronganswers:
        question_list.append(wronganswer)
    shuffle(question_list)
    run = True
    keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
            pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
    while run:
        message_window = pygame.Surface([800, 250])
        large_text = pygame.font.Font("font_src/PAPYRUS.TTF", 20)
        text_surf, text_rect = text_object(question, large_text)
        text_rect.center = (400, 500)
        alternatives_text = []
        altnr = 0
        for alternative in question_list:
            alternatives_text.append(text_object(f"{altnr + 1}:{alternative}", large_text))
            altnr += 1
        #checks players answers
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                for i in range(len(question_list)):
                    if event.key == keys[i]:
                        return question_list[i] == rightanswers
        screen.blit(get_get_quiz_sprite(), (100, 250))
        screen.blit(message_window, (0, 450))
        screen.blit(text_surf, text_rect)
        alt_pos = 300
        for alternative_text in alternatives_text:
            alternative_text[1].center = (250, alt_pos)
            alt_pos += 30
            screen.blit(alternative_text[0], alternative_text[1])
        pygame.display.update()
