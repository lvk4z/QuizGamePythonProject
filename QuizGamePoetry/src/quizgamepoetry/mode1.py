import sys
import pygame
from pygame.locals import *
from utils import draw_background, draw_lifebuoys, draw_options, draw_question, draw_score_table,draw_timer, highlight_correct_answer, hover_cond
from questions import load_question, parse_question
from lifebuoys import use_friends
import random

def load_image_by_name(name_):
    path_ = 'C:/QuizGamePythonProject/QuizGamePoetry/src/quizgamepoetry/resources'
    return pygame.image.load(path_ + name_).convert_alpha()

def endgame(pygame, window, width, question_number, ABCD):
    finish_bg = load_image_by_name('/game/finish_bg.jpg')
    font = pygame.font.SysFont('arial', 30)

    correct = [ABCD[i][0] for i in range(4) if ABCD[i][1]][0]

    if ( 2 <= question_number <= 12):
        string = "Niestety to koniec gry. Udało ci się wygrać 1000 zł  !!! Poprawną odpowiedzią było: " + correct
    elif (question_number >= 13):
        string = "Gratulacje mistrzu, wygrywasz 1 000 000 zł!!!! "
    else:
        string = "Niestety to koniec gry. Nic nie wygrałeś :( Poprawną odpowiedzią było:" + correct

    text = font.render(string, True, (184, 193, 209))
    text_rect = text.get_rect (center = (width // 2 , 280))

    run = True
    while run:
        mouse_pointer = pygame.mouse.get_pos()

        window.blit(finish_bg, (0, 0))
        window.blit(text, text_rect)
        if 534 < mouse_pointer[0] < 745 and 481 < mouse_pointer[1] < 512:
            pass
        else: 
            pass
        if 534 < mouse_pointer[0] < 745 and 520 < mouse_pointer[1] < 551:
            pass
        else: 
            pass
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == QUIT:
                    run = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 540 < mouse_pointer[0] < 740:
                            if 365 < mouse_pointer[1] < 420:
                                run = False
                                mode1_play(window, width)
                            elif 476 < mouse_pointer[1] < 535:
                                pygame.quit()
                                sys.exit()

def mode1_play(window, width):

    bg_img = load_image_by_name('/game/bg.jpg')
    option_hover = load_image_by_name('/game/answer_hover.png')
    score_table = [load_image_by_name('/game/score_table1b.jpg')]
    for i in range(2, 13, 1):
        score_table.append(load_image_by_name('/game/score_table' + str(i) + '.jpg'))
    lifebuoy_50 = load_image_by_name('/game/lifebuoy_50.png')
    lifebuoy_friend = load_image_by_name('/game/lifebuoy_friend.png')
    lifebuoy_time = load_image_by_name('/game/lifebuoy_time.png')

    timerfont = pygame.font.SysFont('arial', 130)
    qafont = pygame.font.SysFont('arial', 22)
    full_time = 30
    question_number = 0
    running = True
    load_next_question = True
    used_lifebuoy_50 = False
    used_lifebuoy_friend = False
    used_lifebuoy_time = False
    start_time = pygame.time.get_ticks()
    hidden_answers = []
    questions = {'easy': [], 'medium': [], 'hard': []}
    questions = load_question(questions, question_number)
    suggested_by_friend = -1
    def use_50_50(options):
        incorrect_answers = [i for i, ans in enumerate(options) if not ans[1]]
        return random.sample(incorrect_answers, 2)

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
            hidden_answers = []
            if question_number < 3:
                Q, ABCD, category = parse_question(questions['easy'][question_number])
            elif question_number < 8:
                Q, ABCD, category = parse_question(questions['medium'][question_number-3])
            else:
                Q, ABCD, category = parse_question(questions['hard'][question_number-8])
            load_next_question = False

        draw_question(window, Q, qafont)
        draw_options(window, ABCD, qafont, mouse_pointer, option_hover, hidden_answers)
        draw_lifebuoys(window, lifebuoy_50, lifebuoy_time, lifebuoy_friend, used_lifebuoy_50, used_lifebuoy_time, suggested_by_friend)

        
        if time_left <= 25 or used_lifebuoy_friend:
            dy, dx = 30, 370
            option_frames = [
                    pygame.Rect(210, 560, dx, dy),
                    pygame.Rect(690, 560, dx, dy),
                    pygame.Rect(210, 630, dx, dy),
                    pygame.Rect(690, 630, dx, dy)
                ]
            if not used_lifebuoy_friend:
                correct_answer_index = next(i for i, ans in enumerate(ABCD) if ans[1])
            else:
               correct_answer_index = suggested_by_friend 
               
            highlight_correct_answer(window, ABCD, correct_answer_index, qafont, option_frames[correct_answer_index])

        pygame.display.update()


        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    for j in range(4):
                        if hover_cond(j, mouse_pointer) and j not in hidden_answers:
                            used_lifebuoy_friend = False
                            question_number += 1
                            if not ABCD[j][1]:
                                endgame(pygame, window, width, question_number,ABCD)
                            else:
                                questions = load_question(questions, question_number)
                                start_time = pygame.time.get_ticks()
                                full_time = 30
                                load_next_question = True
                            break

                    if 520 < mouse_pointer[0] < 590 and 310 < mouse_pointer[1] < 380 and not used_lifebuoy_50:
                        used_lifebuoy_50 = True
                        hidden_answers = use_50_50(ABCD)
                    elif 600 < mouse_pointer[0] < 670 and 310 < mouse_pointer[1] < 380 and not used_lifebuoy_time:
                        used_lifebuoy_time = True
                        full_time += 30
                    elif 680 < mouse_pointer[0] < 750 and 310 < mouse_pointer[1] < 380 and suggested_by_friend<0:
                        full_time += 5
                        suggested_by_friend = use_friends(window, category,ABCD)
                        used_lifebuoy_friend = True
                    elif 1215 < mouse_pointer[0] < 1280 and 0 < mouse_pointer[1] < 62:
                        sys.exit()