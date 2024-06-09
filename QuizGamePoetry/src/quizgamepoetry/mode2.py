import sys
import pygame
from pygame.locals import *
from utils.game_functions import load_images, highlight_correct_answer, load_sounds
from utils.drawing import (
    draw_background,
    draw_timer,
    draw_score_table,
    draw_question,
    draw_lifebuoys,
    draw_options,
)
from questions import load_question, parse_question
from utils.hover_and_event_handling import hover_cond, mark_wrong_option
from lifebuoys import use_friends_help, use_fifty_fifty
from mode1 import endgame




def mode2_play(window, width):
    """
    Main function to play mode 2 of the game.

    Args:
    window (pygame.Surface): The game window.
    width (int): The width of the game window.
    """
    images = load_images()
    sounds = load_sounds()

    sounds["background_music"].play(-1)

    timerfont = pygame.font.SysFont("arial", 130)
    qafont = pygame.font.SysFont("arial", 22)
    full_time = 30
    question_number = 0
    running = True
    load_next_question = True
    used_lifebuoy_50 = False
    used_lifebuoy_friend = False
    used_lifebuoy_time = False
    start_time = pygame.time.get_ticks()
    hidden_answers = []
    suggested_by_friend = -1

    while running:
        mouse_pointer = pygame.mouse.get_pos()
        time_left = full_time - (pygame.time.get_ticks() - start_time) / 1000

        if int(time_left) >= 0 and question_number < 12:
            pygame.display.update()
        else:
            endgame(pygame, window, width, question_number, option_answers)

        draw_background(window, images["bg_img"])
        draw_timer(window, timerfont, time_left, width, images["clock"])
        draw_score_table(window, images["score_table"], question_number)

        if load_next_question:
            hidden_answers = []
            question_data = load_question(10)
            current_question, option_answers, category = parse_question(question_data)
            load_next_question = False

        draw_question(window, current_question, qafont)
        draw_options(
            window,
            option_answers,
            qafont,
            mouse_pointer,
            images["option_hover"],
            hidden_answers,
        )
        draw_lifebuoys(
            window,
            images["lifebuoy_50"],
            images["lifebuoy_time"],
            images["lifebuoy_friend"],
            used_lifebuoy_50,
            used_lifebuoy_time,
            suggested_by_friend,
        )

        if time_left <= 25 or used_lifebuoy_friend:
            dy, dx = 30, 370
            option_frames = [
                pygame.Rect(210, 560, dx, dy),
                pygame.Rect(690, 560, dx, dy),
                pygame.Rect(210, 630, dx, dy),
                pygame.Rect(690, 630, dx, dy),
            ]
            if not used_lifebuoy_friend:
                correct_answer_index = next(
                    i for i, ans in enumerate(option_answers) if ans[1]
                )
            else:
                correct_answer_index = suggested_by_friend

            highlight_correct_answer(
                window,
                option_answers,
                correct_answer_index,
                qafont,
                option_frames[correct_answer_index],
            )

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
                            if not option_answers[j][1]:
                                mark_wrong_option(
                                    window,
                                    option_answers,
                                    qafont,
                                    j,
                                    images["wrong_answer_hover"],
                                )
                                pygame.display.update()
                                sounds["disappointment"].play()
                                sounds["background_music"].stop()
                                pygame.time.wait(2000)

                                endgame(
                                    pygame,
                                    window,
                                    width,
                                    question_number,
                                    option_answers,
                                )
                            else:
                                sounds["applause"].play()
                                pygame.time.wait(2000)
                                start_time = pygame.time.get_ticks()
                                full_time = 30
                                load_next_question = True
                            break

                    if (
                        520 < mouse_pointer[0] < 590
                        and 310 < mouse_pointer[1] < 380
                        and not used_lifebuoy_50
                    ):
                        used_lifebuoy_50 = True
                        hidden_answers = use_fifty_fifty(option_answers)
                    elif (
                        600 < mouse_pointer[0] < 670
                        and 310 < mouse_pointer[1] < 380
                        and not used_lifebuoy_time
                    ):
                        used_lifebuoy_time = True
                        full_time += 30
                    elif (
                        680 < mouse_pointer[0] < 750
                        and 310 < mouse_pointer[1] < 380
                        and suggested_by_friend < 0
                    ):
                        full_time += 5
                        suggested_by_friend = use_friends_help(
                            window, category, option_answers
                        )
                        used_lifebuoy_friend = True
                    elif 1215 < mouse_pointer[0] < 1280 and 0 < mouse_pointer[1] < 62:
                        sys.exit()
