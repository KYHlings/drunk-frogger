from random import shuffle
import html
import requests

from image.image_handler import get_get_quiz_sprite, get_quiz_box, main_menu_image
from game_src.window_handler import text_object, draw_text
from game_src.variabels import *
from game_src.menu_buttons import movies_category_button, video_games_category_button, geography_category_button, music_category_button, general_knowledge_category_button


# loads quiz from json-file, in future will load from api.
def get_quiz(quiz_category):
    url = requests.get(f"https://opentdb.com/api.php?amount=25&category={quiz_category}&difficulty=easy&type=multiple")
    content = url.json(encoding='utf8')['results']
    shuffle(content)
    return content


# unloads content from get_quiz function.
def quiz(quiz_category):
    while True:
        quiz_content = get_quiz(quiz_category)
        for q in quiz_content:
            if len(html.unescape(q['question'])) < 88:
                return q["question"], q["correct_answer"], q["incorrect_answers"]


def quiz_correct_window(question, rightanswers, drunk_meter):

    while True:
        question_fonts_ls = pygame.font.Font(f"font_src/{font_list[drunk_meter][0]}", font_list[drunk_meter][1])
        goat_name_fonts = pygame.font.Font(f"font_src/{font_list[drunk_meter][0]}", font_list[drunk_meter][1] + 15)

        # checks players answers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

        screen.blit(get_get_quiz_sprite(), (160, 170))
        screen.blit(get_quiz_box(), (-20, 330))
        draw_text("Correct!", goat_name_fonts, BLACK, screen, 175, 445, 'topleft')
        draw_text(f"The question was: {question}", question_fonts_ls, BLACK, screen, 75, 525, 'topleft')
        draw_text(f"'{rightanswers}' was the correct answer! Good job!", question_fonts_ls, BLACK, screen, 75, 605, 'topleft')
        draw_text(f"Press enter to continue", question_fonts_ls, BLACK, screen, 75, 685, 'topleft')

        pygame.display.update()


def quiz_incorrect_window(question, rightanswers, wrong_ans, drunk_meter):
    while True:
        question_fonts_ls = pygame.font.Font(f"font_src/{font_list[drunk_meter][0]}", font_list[drunk_meter][1])
        goat_name_fonts = pygame.font.Font(f"font_src/{font_list[drunk_meter][0]}", font_list[drunk_meter][1] + 15)

        # checks players answers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

        screen.blit(get_get_quiz_sprite(), (160, 170))
        screen.blit(get_quiz_box(), (-20, 330))
        draw_text("Incorrect!", goat_name_fonts, BLACK, screen, 175, 445, 'topleft')
        draw_text(f"The question was: {question}", question_fonts_ls, BLACK, screen, 75, 525, 'topleft')
        draw_text(f"'{rightanswers}' was the correct answer, not '{wrong_ans}'! Better luck next time!", question_fonts_ls, BLACK, screen, 75, 605,
                  'topleft')
        draw_text(f"Press enter to continue", question_fonts_ls, BLACK, screen, 75, 685, 'topleft')
        pygame.display.update()



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
                    # if event.key == keys[i]:
                    #     return question_list[i] == rightanswers
                    if event.key == keys[i]:
                        if question_list[i] == rightanswers:
                            quiz_correct_window(question, rightanswers, drunk_meter)
                            return True
                        else:
                            quiz_incorrect_window(question, rightanswers, question_list[i], drunk_meter)
                            return False
        screen.blit(get_get_quiz_sprite(), (160, 170))
        screen.blit(get_quiz_box(), (-20, 330))
        draw_text("Wise Poppy", goat_name_fonts, BLACK, screen, 175, 445, 'topleft')
        draw_text(question, question_fonts_ls, BLACK, screen, 75, 525, 'topleft')
        alt_pos = 575
        for alternative_text in alternatives_text:
            alternative_text[1].topleft = (100, alt_pos)
            alt_pos += 45
            screen.blit(alternative_text[0], alternative_text[1])
        pygame.display.update()


def quiz_settings(current_quiz):
    categories_ls = {11: "Movies", 15: "Video Games", 9: "General Knowledge", 12: "Music", 22: "Geography"}
    highlighted = 0
    while True:
        screen.blit(main_menu_image(), (0, 0))
        draw_text("Choose quiz category", menu_font, WHITE, screen, 640, 50, "center")
        draw_text(f"Current quiz category: {categories_ls[current_quiz]}", menu_font, WHITE, screen, 50, 100, "topleft")
        movies_category_button(highlighted)
        video_games_category_button(highlighted)
        geography_category_button(highlighted)
        music_category_button(highlighted)
        general_knowledge_category_button(highlighted)
        # draw_text("[1]:Movies", menu_font, BLACK, screen, 100, 200, 'topleft')
        # draw_text("[2]:Video Games", menu_font, BLACK, screen, 100, 270, 'topleft')
        # draw_text("[3]:Books", menu_font, BLACK, screen, 100, 340, 'topleft')
        # draw_text("[4]:Music", menu_font, BLACK, screen, 100, 410, 'topleft')
        # draw_text("[5]:General Knowledge", menu_font, BLACK, screen, 100, 480, 'topleft')
        draw_text("Enter to return", general_font, BLACK, screen, 50, 650, "topleft")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    current_quiz = 11
                if event.key == pygame.K_2:
                    current_quiz = 15
                if event.key == pygame.K_3:
                    current_quiz = 22
                if event.key == pygame.K_4:
                    current_quiz = 12
                if event.key == pygame.K_5:
                    current_quiz = 9
                if event.key == pygame.K_RETURN:
                    if highlighted == 0:
                        current_quiz = 11
                    if highlighted == 1:
                        current_quiz = 15
                    if highlighted == 2:
                        current_quiz = 22
                    if highlighted == 3:
                        current_quiz = 12
                    if highlighted == 4:
                        current_quiz = 9
                    return current_quiz

                if event.key == pygame.K_DOWN:
                    highlighted += 1
                    if highlighted == 5:
                        highlighted = 0
                if event.key == pygame.K_UP:
                    highlighted -= 1
                    if highlighted < 0:
                        highlighted = 4
        pygame.display.update()

