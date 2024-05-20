import sys
import pygame
from pygame.locals import *
from utils import show_friends, draw_background, draw_lifebuoys, draw_options, draw_question, draw_score_table,draw_timer
from questions import load_question, parse_question
import random

def use_50_50(abcd):
        incorrect_answers = [i for i, ans in enumerate(abcd) if not ans[1]]
        return random.sample(incorrect_answers, 2)
def friends(window, Q):
    friends = pygame.image.load('QuizGame/src/resources/game/friends.jpg').convert_alpha()
    window.blit(friends, (330,0))

def endgame(pygame, window, width, question_number, ABCD):

    finish_bg = pygame.image.load('QuizGame/src/resources/game/finish_bg.jpg').convert_alpha()
    font = pygame.font.SysFont('arial', 30)

    for i in range(0, 4):
            if ABCD[i][1]:
                correct  = ABCD[i][0]
                

    if ( 2 <= question_number <= 7):
        string = "Niestety to koniec gry. Udało ci się wygrać 1000 zł  !!! Poprawną odpowiedzią było: " + correct
    elif (8 <= question_number <= 12):
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
        if mouse_pointer[0] > 534 and mouse_pointer[0] < 745 and mouse_pointer[1] > 481 and mouse_pointer[1] < 512:
            pass
        else: 
            pass
        if mouse_pointer[0] > 534 and mouse_pointer[0] < 745 and mouse_pointer[1] > 520 and mouse_pointer[1] < 551:
            pass
        else: 
            pass
        pygame.display.update()

        for event in pygame.event.get():
                if event.type == QUIT:
                    run = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 540 < mouse_pointer[0] < 740 and 365 < mouse_pointer[1] < 420:
                            run = False
                            mode1_play(window, width)
                        if 540 < mouse_pointer[0] < 740 and 476 < mouse_pointer[1] < 503:
                            pygame.quit()
                            sys.exit()

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
    questions = {'easy': [], 'medium': [], 'hard': []}
    questions = load_question(questions, question_number)
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
            if question_number <= 3:
                Q, ABCD = parse_question(questions['easy'][question_number])
                load_next_question = False
            elif question_number <= 7:
                Q, ABCD = parse_question(questions['medium'][question_number - 4])
                load_next_question = False
            else:
                Q, ABCD = parse_question(questions['hard'][question_number - 8])
                load_next_question = False

        draw_question(window, Q, qafont)
        draw_options(window, ABCD, qafont, mouse_pointer, option_hover, hidden_answers)
        draw_lifebuoys(window, lifebuoy_50, lifebuoy_time, lifebuoy_friend, used_lifebuoy_50, used_lifebuoy_time, used_lifebuoy_friend)

        if used_lifebuoy_friend:
            friends(window,Q)

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
                            endgame(pygame, window, width, question_number,ABCD)
                        else:
                            questions = load_question(questions, question_number)
                            load_next_question = True
                    if 675 < mouse_pointer[0] < 1076 and 548 < mouse_pointer[1] < 598 and 1 not in hidden_answers:
                        question_number += 1
                        start_time = pygame.time.get_ticks()
                        full_time = 30
                        if not ABCD[1][1]:
                            endgame(pygame, window, width, question_number,ABCD)
                        else:
                            questions = load_question(questions, question_number)
                            load_next_question = True
                    if 206 < mouse_pointer[0] < 610 and 620 < mouse_pointer[1] < 665 and 2 not in hidden_answers:
                        question_number += 1
                        start_time = pygame.time.get_ticks()
                        full_time = 30
                        if not ABCD[2][1]:
                            endgame(pygame, window, width, question_number,ABCD)
                        else:
                            questions = load_question(questions, question_number)
                            load_next_question = True
                    if 675 < mouse_pointer[0] < 1076 and 620 < mouse_pointer[1] < 665 and 3 not in hidden_answers:
                        question_number += 1
                        start_time = pygame.time.get_ticks()
                        full_time = 30
                        if not ABCD[3][1]:
                            
                            endgame(pygame, window, width, question_number,ABCD)
                        else:
                            questions = load_question(questions, question_number)
                            load_next_question = True

                    if 520 < mouse_pointer[0] < 590 and 310 < mouse_pointer[1] < 380 and not used_lifebuoy_50:
                        used_lifebuoy_50 = True
                        hidden_answers = use_50_50(ABCD)
                    if 600 < mouse_pointer[0] < 670 and 310 < mouse_pointer[1] < 380 and not used_lifebuoy_time:
                        used_lifebuoy_time = True
                        full_time += 30
                    if 680 < mouse_pointer[0] < 750 and 310 < mouse_pointer[1] < 380 and not used_lifebuoy_friend:
                        used_lifebuoy_friend = True
                        full_time += 5
                        

                    if 1215 < mouse_pointer[0] < 1280 and 0 < mouse_pointer[1] < 62:
                        sys.exit()