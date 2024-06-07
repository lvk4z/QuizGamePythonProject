import pygame
from utils.game_functions import draw_text


def hover_cond(i, mouse_position):
    """
    Check if the mouse is hovering over a specific option.

    Args:
    i (int): Index of the option.
    mouse_position (Tuple[int, int]): Current mouse position.

    Returns:
    bool: True if the mouse is hovering over the option, False otherwise.
    """
    hover_conditions = [
        (206 < mouse_position[0] < 610 and 548 < mouse_position[1] < 598),
        (675 < mouse_position[0] < 1076 and 548 < mouse_position[1] < 598),
        (206 < mouse_position[0] < 610 and 620 < mouse_position[1] < 665),
        (675 < mouse_position[0] < 1076 and 620 < mouse_position[1] < 665),
    ]
    return hover_conditions[i]


def mark_wrong_option(
    window, option_asnwers, qafont, chosen_option, wrong_answer_hover
):
    """
    Mark the chosen wrong option with a visual cue.

    Args:
    window (pygame.Surface): The game window.
    option_asnwers (List[Tuple[str, Tuple[int, int, int]]]): List of options.
    qafont (pygame.font.Font): Font for drawing text.
    chosen_option (int): Index of the chosen option.
    wrong_answer_hover (pygame.Surface): Image for indicating a wrong answer.

    Returns:
    None
    """
    option_frames = [
        pygame.Rect(210, 560, 370, 30),
        pygame.Rect(690, 560, 370, 30),
        pygame.Rect(210, 630, 370, 30),
        pygame.Rect(690, 630, 370, 30),
    ]

    for i, frame in enumerate(option_frames):
        if i == chosen_option:
            coord = (
                (frame.x - 16, frame.y - 12)
                if i % 2
                else (frame.x - 2, frame.y - 12)
            )
            window.blit(wrong_answer_hover, coord)
            draw_text(window, option_asnwers[i][0], "black", frame, qafont, True)
