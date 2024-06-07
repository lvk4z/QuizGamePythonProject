import pygame
from utils.hover_and_event_handling import hover_cond
from utils.game_functions import draw_text
import time
import math


def draw_background(window, bg_img):
    """
    Draw the background image on the window.

    Args:
    window (pygame.Surface): The game window surface.
    bg_img (pygame.Surface): The background image surface.
    """
    window.blit(bg_img, (0, 0))


def draw_timer(window, timerfont, time_left, width, bg_image):
    """
    Draw the timer on the window with animated background.

    Args:
    window (pygame.Surface): The game window surface.
    timerfont (pygame.font.Font): The font for the timer.
    time_left (float): Time remaining.
    width (int): Width of the window.
    """

    bg_image = pygame.transform.scale(bg_image, (210, 210))

    current_time = time_left
    pulsating_factor = 1 + 0.5 * math.sin(current_time * 2.0)

    scaled_width = int(150 + 80 * pulsating_factor)
    scaled_image = pygame.transform.scale(bg_image, (scaled_width, scaled_width))

    bg_position = (width // 2, 170)
    window.blit(
        scaled_image,
        (bg_position[0] - scaled_width // 2, bg_position[1] - scaled_width // 2),
    )

    text = timerfont.render(str(int(time_left)), True, (255, 255, 255))
    text_rect = text.get_rect(center=bg_position)
    window.blit(text, text_rect)


def draw_question(window, question, qafont):
    """
    Draw the question on the window.

    Args:
    window (pygame.Surface): The game window surface.
    question (str): The question text.
    qafont (pygame.font.Font): The font for the question.
    """
    Q_frame = pygame.Rect(240, 430, 805, 50)
    draw_text(window, question, "white", Q_frame, qafont, True)


def draw_options(window, ABCD, qafont, mouse_pointer, option_hover, hidden_answers):
    """
    Draw the options on the window.

    Args:
    window (pygame.Surface): The game window surface.
    ABCD (list): List of answer options.
    qafont (pygame.font.Font): The font for the options.
    mouse_position (tuple): Current mouse position.
    option_hover (pygame.Surface): Image for indicating hover.
    hidden_answers (list): List of indices of hidden answers.
    """
    option_frames = [
        pygame.Rect(210, 560, 370, 30),
        pygame.Rect(690, 560, 370, 30),
        pygame.Rect(210, 630, 370, 30),
        pygame.Rect(690, 630, 370, 30),
    ]

    for i, frame in enumerate(option_frames):
        if i not in hidden_answers:
            if hover_cond(i, mouse_pointer):
                coord = (
                    (frame.x - 16, frame.y - 12)
                    if i % 2
                    else (frame.x - 2, frame.y - 12)
                )
                window.blit(option_hover, coord)
                draw_text(window, ABCD[i][0], "black", frame, qafont, True)

            else:
                draw_text(window, ABCD[i][0], "white", frame, qafont, True)


def draw_lifebuoys(
    window,
    lifebuoy_50,
    lifebuoy_time,
    lifebuoy_friend,
    used_lifebuoy_50,
    used_lifebuoy_time,
    friends_state,
):
    """
    Draw lifebuoy icons on the window.

    Args:
    window (pygame.Surface): The game window surface.
    lifebuoy_50 (pygame.Surface): Lifebuoy image for 50/50 lifeline.
    lifebuoy_time (pygame.Surface): Lifebuoy image for time lifeline.
    lifebuoy_friend (pygame.Surface): Lifebuoy image for friends lifeline.
    used_lifebuoy_50 (bool): Flag indicating whether 50/50 lifeline is used.
    used_lifebuoy_time (bool): Flag indicating whether time lifeline is used.
    friends_state (int): State of the friends lifeline.
    """
    if not used_lifebuoy_50:
        window.blit(lifebuoy_50, (520, 310))
    if not used_lifebuoy_time:
        window.blit(lifebuoy_time, (600, 310))
    if friends_state < 0:
        window.blit(lifebuoy_friend, (680, 310))


def draw_score_table(window, score_table, question_number):
    """
    Draw the score table on the window.

    Args:
    window (pygame.Surface): The game window surface.
    score_table (list): List of score table images.
    question_number (int): Current question number.
    """
    if question_number <= 12:
        window.blit(score_table[question_number], (5, 5))
