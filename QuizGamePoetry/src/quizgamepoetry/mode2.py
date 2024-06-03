"""Tryb trudny - bez kół ratunkowych, same trudne pytania"""
import sys
import pygame
from pygame.locals import *
from utils import draw_background, draw_lifebuoys, draw_options, draw_question, draw_score_table,draw_timer, highlight_correct_answer
from questions import load_question, parse_question



def endgame(pygame, window, width, question_number, ABCD):
    """Ekran końca gry"""
    finish_bg = pygame.image.load('C:/QuizGamePythonProject/QuizGamePoetry/src/quizgamepoetry/resources/gamefinish_bg.jpg').convert_alpha()
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
                            mode2_play(window, width)
                        if 540 < mouse_pointer[0] < 740 and 476 < mouse_pointer[1] < 503:
                            pygame.quit()
                            sys.exit()

def mode2_play(window, width):
    """Mechanika gry trybu trudnego"""
    bg_img = pygame.image.load('C:/QuizGamePythonProject/QuizGame/src/resources/game/bg.jpg').convert_alpha()
    option_hover = pygame.image.load('C:/QuizGamePythonProject/QuizGamePoetry/src/quizgamepoetry/resources/game/answer_hover.png').convert_alpha()
    score_table = [pygame.image.load('C:/QuizGamePythonProject/QuizGamePoetry/src/quizgamepoetry/resources/game/score_table1b.jpg').convert_alpha(),
                    pygame.image.load('C:/QuizGamePythonProject/QuizGamePoetry/src/quizgamepoetry/resources/game/score_table2.jpg').convert_alpha(),
                    pygame.image.load('C:/QuizGamePythonProject/QuizGamePoetry/src/quizgamepoetry/resources/game/score_table3.jpg').convert_alpha(),
                    pygame.image.load('C:/QuizGamePythonProject/QuizGamePoetry/src/quizgamepoetry/resources/game/score_table4.jpg').convert_alpha(),
                    pygame.image.load('C:/QuizGamePythonProject/QuizGamePoetry/src/quizgamepoetry/resources/game/score_table5.jpg').convert_alpha(),
                    pygame.image.load('C:/QuizGamePythonProject/QuizGamePoetry/src/quizgamepoetry/resources/game/score_table6.jpg').convert_alpha(),
                    pygame.image.load('C:/QuizGamePythonProject/QuizGamePoetry/src/quizgamepoetry/resources/game/score_table7.jpg').convert_alpha(),
                    pygame.image.load('C:/QuizGamePythonProject/QuizGamePoetry/src/quizgamepoetry/resources/game/score_table8.jpg').convert_alpha(),
                    pygame.image.load('C:/QuizGamePythonProject/QuizGamePoetry/src/quizgamepoetry/resources/game/score_table9.jpg').convert_alpha(),
                    pygame.image.load('C:/QuizGamePythonProject/QuizGamePoetry/src/quizgamepoetry/resources/game/score_table10.jpg').convert_alpha(),
                    pygame.image.load('C:/QuizGamePythonProject/QuizGamePoetry/src/quizgamepoetry/resources/game/score_table11.jpg').convert_alpha(),
                    pygame.image.load('C:/QuizGamePythonProject/QuizGamePoetry/src/quizgamepoetry/resources/game/score_table12.jpg').convert_alpha()]
    


    

    timerfont = pygame.font.SysFont('arial', 130)
    qafont = pygame.font.SysFont('arial', 22)
    full_time = 20
    time_left = 20
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
            load_question = False
            

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
