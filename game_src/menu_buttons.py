from game_src.window_handler import draw_text
from game_src.variabels import *

def start_menu_button(highlighted):
    #455 <= mouse[0] <= 455 + 320 and 180 <= mouse[1] <= 180 + 70:
    #mouse = pygame.mouse.get_pos()
    if highlighted == 0:
        pygame.draw.rect(screen, WHITE, (455, 180, 320, 70), 3)
        pygame.draw.rect(screen, LIGHT_PURPLE_SELECTED, (457, 182, 316, 66))
        draw_text("Start Game", menu_font, WHITE, screen, 480, 180, 'topleft')
    else:
        pygame.draw.rect(screen, WHITE, (455, 180, 320, 70), 3)
        pygame.draw.rect(screen, LIGHT_PURPLE_UNSELECTED, (457, 182, 316, 66))
        draw_text("Start Game", menu_font, WHITE, screen, 480, 180, 'topleft')


def settings_menu_button(highlighted):
    #mouse = pygame.mouse.get_pos()
    #if 455 <= mouse[0] <= 440 + 320 and 270 <= mouse[1] <= 270 + 70:
    if highlighted == 1:
        pygame.draw.rect(screen, WHITE, (455, 270, 320, 70), 3)
        pygame.draw.rect(screen, LIGHT_PURPLE_SELECTED, (457, 272, 316, 66))
        draw_text("Settings", menu_font, WHITE, screen, 515, 270, 'topleft')
    else:
        pygame.draw.rect(screen, WHITE, (455, 270, 320, 70), 3)
        pygame.draw.rect(screen, LIGHT_PURPLE_UNSELECTED, (457, 272, 316, 66))
        draw_text("Settings", menu_font, WHITE, screen, 515, 270, 'topleft')


def tutorial_menu_button(highlighted):
    #mouse = pygame.mouse.get_pos()
    #if 455 <= mouse[0] <= 455 + 320 and 360 <= mouse[1] <= 360 + 70:
    if highlighted == 2:
        pygame.draw.rect(screen, WHITE, (455, 360, 320, 70), 3)
        pygame.draw.rect(screen, LIGHT_PURPLE_SELECTED, (457, 362, 316, 66))
        draw_text("Tutorial", menu_font, WHITE, screen, 515, 360, 'topleft')
    else:
        pygame.draw.rect(screen, WHITE, (455, 360, 320, 70), 3)
        pygame.draw.rect(screen, LIGHT_PURPLE_UNSELECTED, (457, 362, 316, 66))
        draw_text("Tutorial", menu_font, WHITE, screen, 515, 360, 'topleft')


def high_score_menu_button(highlighted):
    #mouse = pygame.mouse.get_pos()
    #if 455 <= mouse[0] <= 455 + 320 and 450 <= mouse[1] <= 450 + 70:
    if highlighted == 3:
        pygame.draw.rect(screen, WHITE, (455, 450, 320, 70), 3)
        pygame.draw.rect(screen, LIGHT_PURPLE_SELECTED, (457, 452, 316, 66))
        draw_text("High Score", menu_font, WHITE, screen, 490, 450, 'topleft')
    else:
        pygame.draw.rect(screen, WHITE, (455, 450, 320, 70), 3)
        pygame.draw.rect(screen, LIGHT_PURPLE_UNSELECTED, (457, 452, 316, 66))
        draw_text("High Score", menu_font, WHITE, screen, 490, 450, 'topleft')


def quit_menu_button(highlighted):
    #mouse = pygame.mouse.get_pos()
    #if 455 <= mouse[0] <= 440 + 320 and 540 <= mouse[1] <= 540 + 70:
    if highlighted == 4:
        pygame.draw.rect(screen, WHITE, (455, 540, 320, 70), 3)
        pygame.draw.rect(screen, LIGHT_PURPLE_SELECTED, (457, 542, 316, 66))
        draw_text("Quit Game", menu_font, WHITE, screen, 495, 540, 'topleft')
    else:
        pygame.draw.rect(screen, WHITE, (455, 540, 320, 70), 3)
        pygame.draw.rect(screen, LIGHT_PURPLE_UNSELECTED, (457, 542, 316, 66))
        draw_text("Quit Game", menu_font, WHITE, screen, 495, 540, 'topleft')



def sound_settings_button(highlighted):
    if highlighted == 0:
        pygame.draw.rect(screen, WHITE, (445, 270, 390, 70), 3)
        pygame.draw.rect(screen, LIGHT_PURPLE_SELECTED, (447, 272, 386, 66))
        draw_text("Sound Settings", menu_font, WHITE, screen, 640, 300, 'center')
    else:
        pygame.draw.rect(screen, WHITE, (445, 270, 390, 70), 3)
        pygame.draw.rect(screen, LIGHT_PURPLE_UNSELECTED, (447, 272, 386, 66))
        draw_text("Sound Settings", menu_font, WHITE, screen, 640, 300, 'center')


def quiz_settings_button(highlighted):
    if highlighted == 1:
        pygame.draw.rect(screen, WHITE, (445, 370, 390, 70), 3)
        pygame.draw.rect(screen, LIGHT_PURPLE_SELECTED, (447, 372, 386, 66))
        draw_text("Quiz Settings", menu_font, WHITE, screen, 640, 400, "center")
    else:
        pygame.draw.rect(screen, WHITE, (445, 370, 390, 70), 3)
        pygame.draw.rect(screen, LIGHT_PURPLE_UNSELECTED, (447, 372, 386, 66))
        draw_text("Quiz Settings", menu_font, WHITE, screen, 640, 400, "center")

def credit_button(highlighted):
    if highlighted == 2:
        pygame.draw.rect(screen, WHITE, (445, 470, 390, 70), 3)
        pygame.draw.rect(screen, LIGHT_PURPLE_SELECTED, (447, 472, 386, 66))
        draw_text("Credits", menu_font, WHITE, screen, 640, 500, "center")
    else:
        pygame.draw.rect(screen, WHITE, (445, 470, 390, 70), 3)
        pygame.draw.rect(screen, LIGHT_PURPLE_UNSELECTED, (447, 472, 386, 66))
        draw_text("Credits", menu_font, WHITE, screen, 640, 500, "center")