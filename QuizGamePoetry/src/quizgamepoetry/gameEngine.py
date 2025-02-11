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
global images, sounds


def mode_play(window, width, hardMode = False):
    global images, sounds
    """
    Main function to play mode 1 of the game.

    Args:
    window (pygame.Surface): The game window.
    width (int): The width of the game window.
    """
    images = load_images()
    sounds = load_sounds()
    sounds["background_music"].play(-1)

    timerfont = pygame.font.SysFont("arial", 130)
    qafont = pygame.font.SysFont("arial", 22)
    full_time = 30 if not hardMode else 20
    time_break = full_time - 5
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
            endgame(pygame, window, width, question_number, option_answers, hardMode)

        draw_background(window, images["bg_img"])
        draw_timer(window, timerfont, time_left, width, images["clock"])
        draw_score_table(window, images["score_table"], question_number)

        if load_next_question:
            hidden_answers = []
            question_data = load_question(question_number if not hardMode else 10)
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
        if not hardMode:
            draw_lifebuoys(
                window,
                images["lifebuoy_50"],
                images["lifebuoy_time"],
                images["lifebuoy_friend"],
                used_lifebuoy_50,
                used_lifebuoy_time,
                suggested_by_friend,
            )

        if time_left <= time_break or used_lifebuoy_friend:
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
                if correct_answer_index in hidden_answers:
                    correct_answer_index = next(i for i, ans in enumerate(option_answers) if ans[1])

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
                sounds["background_music"].stop()
                sys.exit()
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
                                    option_answers, hardMode)
                            else:
                                sounds["applause"].play()
                                pygame.time.wait(2000)
                                start_time = pygame.time.get_ticks()
                                full_time = 30 if not hardMode else 20
                                load_next_question = True
                            break
                    if not hardMode:
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


def endgame(pygame_module, window, window_width, question_number, answer_options, hardMode = False):
    global images, sounds
    """
    Ends the game and displays the final message.

    Args:
    pygame_module: The pygame module.
    window (pygame.Surface): The game window.
    window_width (int): The width of the game window.
    question_number (int): The current question number.
    answer_options (list): List of options with their correctness.
    """

    finish_bg = images["finish_bg"]
    font = pygame_module.font.SysFont("arial", 30)

    correct = [answer_options[i][0] for i in range(4) if answer_options[i][1]][0]

    messages = {
        range(
            2, 13
        ): f"Niestety to koniec gry. Udało ci się wygrać 1000 zł  !!! Poprawną odpowiedzią było: {correct}",
        range(13, 100): "Gratulacje mistrzu, wygrywasz 1 000 000 zł!!!!",
        range(
            0, 2
        ): f"Niestety to koniec gry. Nic nie wygrałeś :( Poprawną odpowiedzią było: {correct}",
    }

    for question_range, message in messages.items():
        if question_number in question_range:
            string = message
            break

    text = font.render(string, True, (184, 193, 209))
    text_rect = text.get_rect(center=(window_width // 2, 280))

    run = True
    while run:
        mouse_pointer = pygame_module.mouse.get_pos()

        window.blit(finish_bg, (0, 0))
        window.blit(text, text_rect)

        hover_conditions = {
            (534, 745, 481, 512): lambda: None,
            (534, 745, 520, 551): lambda: None,
        }

        for (x1, x2, y1, y2), action in hover_conditions.items():
            if x1 < mouse_pointer[0] < x2 and y1 < mouse_pointer[1] < y2:
                action()

        pygame_module.display.update()
        for event in pygame_module.event.get():
            if event.type == pygame_module.QUIT:
                run = False
            if event.type == pygame_module.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 540 < mouse_pointer[0] < 740:
                        if 365 < mouse_pointer[1] < 420:
                            run = False
                            mode_play(window, window_width, hardMode)
                        elif 476 < mouse_pointer[1] < 535:
                            pygame_module.quit()
                            sys.exit()