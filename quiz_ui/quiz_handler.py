
from random import shuffle
import html
import requests

from image.image_handler import get_get_quiz_sprite, get_quiz_box
from game_src.window_handler import  text_object, draw_text
from game_src.variabels import *

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
            print(f'{len(q["question"])} :::::::{q["question"]}')
            if len(html.unescape(q['question'])) < 88:
                return q["question"], "correct", q["incorrect_answers"]


def quiz_window(quiz, drunk_meter):
    # takes quiz function and draws on screen.

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
        question_fonts_ls = pygame.font.Font(f"font_src/{font_list[drunk_meter][0]}", font_list[drunk_meter][1])
        goat_name_fonts = pygame.font.Font(f"font_src/{font_list[drunk_meter][0]}", font_list[drunk_meter][1] + 15)

        alternatives_text = []
        altnr = 0
        for alternative in question_list:
            alternatives_text.append(text_object(f"{altnr + 1}:{alternative}", question_fonts_ls))
            altnr += 1
        # checks players answers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                for i in range(len(question_list)):
                    if event.key == keys[i]:
                        return question_list[i] == rightanswers
        screen.blit(get_get_quiz_sprite(), (140, 230))
        screen.blit(get_quiz_box(), (-20, 330))
        draw_text("The Wise Goat", goat_name_fonts, BLACK, screen, 175, 445,'topleft')
        draw_text(question, question_fonts_ls, BLACK, screen, 75, 525,'topleft')
        alt_pos = 575
        for alternative_text in alternatives_text:
            alternative_text[1].topleft = (100, alt_pos)
            alt_pos += 45
            screen.blit(alternative_text[0], alternative_text[1])
        pygame.display.update()
