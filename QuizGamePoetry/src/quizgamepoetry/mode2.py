"""Tryb trudny - bez kół ratunkowych, same trudne pytania"""
import sys
import pygame
from pygame.locals import *
from utils import draw_background, draw_options, draw_question, draw_score_table,draw_timer, hover_cond, highlight_correct_answer
from questions import load_question, parse_question

from mode1 import load_image_by_name, endgame


def mode2_play(window, width):
    bg_img = load_image_by_name('/game/bg.jpg')
    option_hover = load_image_by_name('/game/answer_hover.png')
    score_table = [load_image_by_name('/game/score_table1b.jpg')]
    for i in range(2, 13, 1):
        score_table.append(load_image_by_name('/game/score_table' + str(i) + '.jpg'))

    timerfont = pygame.font.SysFont('arial', 130)
    qafont = pygame.font.SysFont('arial', 22)
    full_time = 20
    question_number = 0
    running = True
    load_next_question = True
    start_time = pygame.time.get_ticks()
    hidden_answers = []
    questions = {'easy': [], 'medium': [], 'hard': []}
    questions = load_question(questions, 10)
    print(questions)

    while running:
        mouse_pointer = pygame.mouse.get_pos()
        time_left = full_time - (pygame.time.get_ticks() - start_time) / 1000

        if int(time_left) >= 0 and question_number <= 12:
            pygame.display.update()
        else:
            endgame(pygame, window, width, question_number,ABCD)

        draw_background(window, bg_img)
        draw_timer(window, timerfont, time_left, width)
        draw_score_table(window, score_table, question_number)

        if load_next_question:
            print(question_number)
            Q, ABCD, category = parse_question(questions['hard'][question_number])
            load_next_question = False

        draw_question(window, Q, qafont)
        draw_options(window, ABCD, qafont, mouse_pointer, option_hover, hidden_answers)
        pygame.display.update()
        if(time_left <= 15):
            dy, dx = 30, 370
            option_frames = [
                pygame.Rect(210, 560, dx, dy),
                pygame.Rect(690, 560, dx, dy),
                pygame.Rect(210, 630, dx, dy),
                pygame.Rect(690, 630, dx, dy)]
            correct_answer_index = next(i for i, ans in enumerate(ABCD) if ans[1])
            highlight_correct_answer(window, ABCD, correct_answer_index, qafont, option_frames[correct_answer_index])

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    for j in range(4):
                        if hover_cond(j, mouse_pointer):
                            question_number += 1
                            if not ABCD[j][1]:
                                endgame(pygame, window, width, question_number,ABCD)
                            else:
                                questions = load_question(questions, 10)
                                start_time = pygame.time.get_ticks()
                                full_time = 20
                                load_next_question = True
                            break
                    if 1215 < mouse_pointer[0] < 1280 and 0 < mouse_pointer[1] < 62:
                        sys.exit()
