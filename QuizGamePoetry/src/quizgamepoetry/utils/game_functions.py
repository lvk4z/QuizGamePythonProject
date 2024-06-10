import pygame
import time

global base_path_
base_path_ = "C:/QuizGamePythonProject/QuizGamePoetry/src/quizgamepoetry/resources"
def load_sounds():
    global base_path_
    """
    Load all necessary sound files and return them in a dictionary.
    
    Returns:
        dict: A dictionary containing loaded sound files.
    """
    base_ = base_path_ + "/sounds"

    sounds = {
        "background_music": pygame.mixer.Sound(f"{base_}/background_music.mp3"),
        "applause": pygame.mixer.Sound(f"{base_}/applause.mp3"),
        "disappointment": pygame.mixer.Sound(f"{base_}/disappointment.mp3"),
    }

    return sounds
def load_images():
    global base_path_
    """
    Load all necessary images and return them in a dictionary.

    Returns:
    dict: Dictionary containing loaded images.
    """

    images = {
        "bg_img": pygame.image.load(f"{base_path_}/game/bg.jpg").convert_alpha(),
        "option_hover": pygame.image.load(
            f"{base_path_}/game/answer_hover.png"
        ).convert_alpha(),
        "score_table": [
            pygame.image.load(f"{base_path_}/game/score_table1.png").convert_alpha()
        ],
    }

    for i in range(2, 13):
        images["score_table"].append(
            pygame.image.load(f"{base_path_}/game/score_table{i}.png").convert_alpha()
        )
    images["friends"] = pygame.image.load(
        f"{base_path_}/game/friends.jpg").convert_alpha()

    images["menu_bg"] = pygame.image.load(
        f"{base_path_}/menu_bg.jpg" ).convert_alpha()

    images["finish_bg"] = pygame.image.load(
        f"{base_path_}/game/finish_bg.jpg").convert_alpha()

    images["lifebuoy_50"] = pygame.image.load(
        f"{base_path_}/game/lifebuoy_50.png"
    ).convert_alpha()
    images["lifebuoy_friend"] = pygame.image.load(
        f"{base_path_}/game/lifebuoy_friend.png"
    ).convert_alpha()
    images["lifebuoy_time"] = pygame.image.load(
        f"{base_path_}/game/lifebuoy_time.png"
    ).convert_alpha()
    images["wrong_answer_hover"] = pygame.image.load(
        f"{base_path_}/game/wrong_answer_hover.jpg"
    ).convert_alpha()
    images["clock"] = pygame.image.load(
        f"{base_path_}/game/clock_bg.png"
    ).convert_alpha()

    return images


def highlight_correct_answer(window, option_answers, correct_answer_index, font, frame):
    """
    Highlight the correct answer on the screen.

    Args:
    window (pygame.Surface): The game window.
    option_answers (list): List of answer options.
    correct_answer_index (int): Index of the correct answer.
    font (pygame.font.Font): Font for drawing text.
    frame (tuple): Rectangle frame for drawing.

    Returns:
    None
    """
    colors = [(184, 196, 71), (255, 255, 255)]
    current_color_index = int(time.time() * 2) % 2
    color = colors[current_color_index]
    draw_text(window, option_answers[correct_answer_index][0], color, frame, font, True)


def draw_text(surface, text, color, rect, font, aa=True, bkg=None):
    """
    Draw text on a surface with word wrapping.

    Args:
    surface (pygame.Surface): The surface to draw on.
    text (str): The text to be drawn.
    color (tuple): The color of the text.
    rect (tuple): The rectangle to draw within.
    font (pygame.font.Font): The font to use for the text.
    aa (bool): Antialiasing flag.
    bkg (tuple): Background color.

    Returns:
    str: Remaining text if the text doesn't fit within the given rectangle.
    """
    line_spacing = -2
    space_width, font_height = font.size(" ")[0], font.size("Tg")[1]

    list_of_words = str(text).split(" ")
    if bkg:
        image_list = [font.render(word, 1, color, bkg) for word in list_of_words]
        for image in image_list:
            image.set_colorkey(bkg)
    else:
        image_list = [font.render(word, aa, color) for word in list_of_words]

    max_len = rect[2]
    line_len_list = [0]
    line_list = [[]]
    for image in image_list:
        width = image.get_width()
        line_len = line_len_list[-1] + len(line_list[-1]) * space_width + width
        if len(line_list[-1]) == 0 or line_len <= max_len:
            line_len_list[-1] += width
            line_list[-1].append(image)
        else:
            line_len_list.append(width)
            line_list.append([image])

    line_bottom = rect[1]
    last_line = 0
    for line_len, line_images in zip(line_len_list, line_list):
        line_left = rect[0]
        line_left += (rect[2] - line_len - space_width * (len(line_images) - 1)) // 2

        if line_bottom + font_height > rect[1] + rect[3]:
            break
        last_line += 1
        for i, image in enumerate(line_images):
            x, y = line_left + i * space_width, line_bottom
            surface.blit(image, (round(x), y))
            line_left += image.get_width()
        line_bottom += font_height + line_spacing

    if last_line < len(line_list):
        draw_words = sum([len(line_list[i]) for i in range(last_line)])
        remaining_text = ""
        for text in list_of_words[draw_words:]:
            remaining_text += text + " "
        return remaining_text
    return ""
