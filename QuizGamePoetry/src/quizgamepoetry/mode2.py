"""Tryb trudny - bez kół ratunkowych, same trudne pytania"""
import sys
import pygame
from pygame.locals import *
from utils import draw_background, draw_options, draw_question, draw_score_table,draw_timer, highlight_correct_answer
from questions import load_question, parse_question



def load_image_by_name(name_):
    path_ = 'C:/QuizGamePythonProject/QuizGamePoetry/src/quizgamepoetry/resources'
    return pygame.image.load(path_ + name_).convert_alpha()
def endgame(pygame, window, width, question_number, ABCD):
    finish_bg = load_image_by_name('/game/finish_bg.jpg')
    font = pygame.font.SysFont('arial', 30)

    for i in range(0, 4):
            if ABCD[i][1]:
                correct  = ABCD[i][0]
                

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
                            mode2_play(window, width)
                        if 540 < mouse_pointer[0] < 740 and 476 < mouse_pointer[1] < 503:
                            pygame.quit()
                            sys.exit()

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
            Q, ABCD, category = parse_question(questions['hard'][question_number])
            load_next_question = False
            

        draw_question(window, Q, qafont)
        draw_options(window, ABCD, qafont, mouse_pointer, option_hover, hidden_answers)

      
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 206 < mouse_pointer[0] < 610 and 548 < mouse_pointer[1] < 598:
                        question_number += 1
                        if not ABCD[0][1]:
                            endgame(pygame, window, width, question_number,ABCD)
                        else:
                            questions = load_question(questions, 10)
                            start_time = pygame.time.get_ticks()
                            full_time = 20
                            load_next_question = True
                    if 675 < mouse_pointer[0] < 1076 and 548 < mouse_pointer[1] < 598:
                        question_number += 1
                        if not ABCD[1][1]:
                            endgame(pygame, window, width, question_number,ABCD)
                        else:
                            questions = load_question(questions, 10)
                            start_time = pygame.time.get_ticks()
                            full_time = 20
                            load_next_question = True
                    if 206 < mouse_pointer[0] < 610 and 620 < mouse_pointer[1] < 665:
                        question_number += 1
                        if not ABCD[2][1]:
                            endgame(pygame, window, width, question_number,ABCD)
                        else:
                            questions = load_question(questions, 10)
                            start_time = pygame.time.get_ticks()
                            full_time = 20
                            load_next_question = True
                    if 675 < mouse_pointer[0] < 1076 and 620 < mouse_pointer[1] < 665:
                        question_number += 1
                        if not ABCD[3][1]:
                            
                            endgame(pygame, window, width, question_number,ABCD)
                        else:
                            questions = load_question(questions, 10)
                            start_time = pygame.time.get_ticks()
                            full_time = 20
                            load_next_question = True

                    if 1215 < mouse_pointer[0] < 1280 and 0 < mouse_pointer[1] < 62:
                        sys.exit()
