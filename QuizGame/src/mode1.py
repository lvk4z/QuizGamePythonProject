import sys
import pandas
import pygame
from pygame.locals import *
from utils import  show_friends, draw_background, draw_lifebuoys, draw_options, draw_question, draw_score_table,draw_timer
import random

OLIVE_GREEN = (193, 203, 15)
def use_50_50(abcd):
        incorrect_answers = [i for i, ans in enumerate(abcd) if not ans[1]]
        return random.sample(incorrect_answers, 2)

def mode1_play(window, width):
    bg_img = pygame.image.load('QuizGame/src/resources/game/bg.jpg').convert_alpha()
    option_hover = pygame.image.load('QuizGame/src/resources/game/answer_hover.png').convert_alpha()
    score_table = [pygame.image.load('QuizGame/src/resources/game/score_table1.jpg').convert_alpha(),
                    pygame.image.load('QuizGame/src/resources/game/score_table2.jpg').convert_alpha(),
                    pygame.image.load('QuizGame/src/resources/game/score_table3.jpg').convert_alpha(),
                    pygame.image.load('QuizGame/src/resources/game/score_table4.jpg').convert_alpha(),
                    pygame.image.load('QuizGame/src/resources/game/score_table5.jpg').convert_alpha(),
                    pygame.image.load('QuizGame/src/resources/game/score_table6.jpg').convert_alpha(),
                    pygame.image.load('QuizGame/src/resources/game/score_table7.jpg').convert_alpha(),
                    pygame.image.load('QuizGame/src/resources/game/score_table8.jpg').convert_alpha(),
                    pygame.image.load('QuizGame/src/resources/game/score_table9.jpg').convert_alpha(),
                    pygame.image.load('QuizGame/src/resources/game/score_table10.jpg').convert_alpha(),
                    pygame.image.load('QuizGame/src/resources/game/score_table11.jpg').convert_alpha(),
                    pygame.image.load('QuizGame/src/resources/game/score_table12.jpg').convert_alpha()]
    
    lifebuoy_50 =  pygame.image.load('QuizGame/src/resources/game/lifebuoy_50.png').convert_alpha()
    lifebuoy_friend =  pygame.image.load('QuizGame/src/resources/game/lifebuoy_friend.png').convert_alpha()
    lifebuoy_time =  pygame.image.load('QuizGame/src/resources/game/lifebuoy_time.png').convert_alpha()

    q_base_easy = pandas.read_excel('QuizGame/src/resources/questionsBase.xlsx', "easy", usecols = "A,B,C,D,E,F").to_dict('index')
    q_base_medium = pandas.read_excel('QuizGame/src/resources/questionsBase.xlsx', "medium", usecols = "A,B,C,D,E,F").to_dict('index')
    q_base_hard = pandas.read_excel('QuizGame/src/resources/questionsBase.xlsx', "hard", usecols = "A,B,C,D,E,F").to_dict('index')

    timerfont = pygame.font.SysFont('arial', 130)
    qafont = pygame.font.SysFont('arial', 22)
    full_time = 30
    time_left = 30
    question_number = 0
    running = True
    load_next_question = True
    used_lifebuoy_50 = False
    used_lifebuoy_friend = False
    used_lifebuoy_time = False
    start_time = pygame.time.get_ticks()
    hidden_answers = []

    

    while running:
        mouse_pointer = pygame.mouse.get_pos()
        time_left = full_time - (pygame.time.get_ticks() - start_time) / 1000

        if  int(time_left) <= 0 or question_number >= 12:
            sys.exit()
            running = False

        draw_background(window, bg_img)
        draw_timer(window, timerfont, time_left, width)
        draw_score_table(window, score_table, question_number)

        if load_next_question:
            hidden_answers = []
            if question_number <= 3:
                Q = q_base_easy[question_number]["PYTANIE"]
                ABCD = [(q_base_easy[question_number]["A"], True), (q_base_easy[question_number]["B"], False),
                        (q_base_easy[question_number]["C"], False), (q_base_easy[question_number]["D"], False)]
                load_next_question = False
            elif question_number <= 7:
                Q = q_base_medium[question_number - 4]["PYTANIE"]
                ABCD = [(q_base_medium[question_number - 4]["A"], True), (q_base_medium[question_number - 4]["B"], False),
                        (q_base_medium[question_number - 4]["C"], False), (q_base_medium[question_number - 4]["D"], False)]
                load_next_question = False
            else:
                Q = q_base_hard[question_number - 8]["PYTANIE"]
                ABCD = [(q_base_hard[question_number - 8]["A"], True), (q_base_hard[question_number - 8]["B"], False),
                        (q_base_hard[question_number - 8]["C"], False), (q_base_hard[question_number - 8]["D"], False)]
                load_next_question = False

        draw_question(window, Q, qafont)
        draw_options(window, ABCD, qafont, mouse_pointer, option_hover, hidden_answers)
        draw_lifebuoys(window, lifebuoy_50, lifebuoy_time, lifebuoy_friend, used_lifebuoy_50, used_lifebuoy_time, used_lifebuoy_friend)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 206 < mouse_pointer[0] < 610 and 548 < mouse_pointer[1] < 598 and 0 not in hidden_answers:
                        question_number += 1
                        start_time = pygame.time.get_ticks()
                        full_time = 30
                        if not ABCD[0][1]:
                            sys.exit()
                        else:
                            load_next_question = True
                    if 675 < mouse_pointer[0] < 1076 and 548 < mouse_pointer[1] < 598 and 1 not in hidden_answers:
                        question_number += 1
                        start_time = pygame.time.get_ticks()
                        full_time = 30
                        if not ABCD[1][1]:
                            sys.exit()
                        else:
                            load_next_question = True
                    if 206 < mouse_pointer[0] < 610 and 620 < mouse_pointer[1] < 665 and 2 not in hidden_answers:
                        question_number += 1
                        start_time = pygame.time.get_ticks()
                        full_time = 30
                        if not ABCD[2][1]:
                            sys.exit()
                        else:
                            load_next_question = True
                    if 675 < mouse_pointer[0] < 1076 and 620 < mouse_pointer[1] < 665 and 3 not in hidden_answers:
                        question_number += 1
                        start_time = pygame.time.get_ticks()
                        full_time = 30
                        if not ABCD[3][1]:
                            sys.exit()
                        else:
                            load_next_question = True

                    if 520 < mouse_pointer[0] < 590 and 310 < mouse_pointer[1] < 380 and not used_lifebuoy_50:
                        used_lifebuoy_50 = True
                        hidden_answers = use_50_50(ABCD)
                    if 600 < mouse_pointer[0] < 670 and 310 < mouse_pointer[1] < 380 and not used_lifebuoy_time:
                        used_lifebuoy_time = True
                        full_time += 30
                    if 680 < mouse_pointer[0] < 750 and 310 < mouse_pointer[1] < 380 and not used_lifebuoy_friend:
                        used_lifebuoy_friend = True
                        show_friends()

                    if 1215 < mouse_pointer[0] < 1280 and 0 < mouse_pointer[1] < 62:
                        sys.exit()
