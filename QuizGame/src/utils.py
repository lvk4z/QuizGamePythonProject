# drawing_utils.py
import pygame
def draw_background(window, bg_img):
    window.blit(bg_img, (0, 0))

def draw_timer(window, timerfont, time_left, width):
    text = timerfont.render(str(int(time_left)), True, (184, 193, 209))
    text_rect = text.get_rect(center=(width // 2, 200))
    window.blit(text, text_rect)

def draw_question(window, question, qafont):
    Q_frame = pygame.Rect(240, 430, 805, 50)
    draw_text(window, question, "white", Q_frame, qafont, True)

def draw_options(window, ABCD, qafont, mouse_pointer, option_hover, hidden_answers):
    option_frames = [
        pygame.Rect(210, 560, 370, 30),
        pygame.Rect(690, 560, 370, 30),
        pygame.Rect(210, 630, 370, 30),
        pygame.Rect(690, 630, 370, 30)
    ]

    hover_conditions = [
        (206 < mouse_pointer[0] < 610 and 548 < mouse_pointer[1] < 598),
        (675 < mouse_pointer[0] < 1076 and 548 < mouse_pointer[1] < 598),
        (206 < mouse_pointer[0] < 610 and 620 < mouse_pointer[1] < 665),
        (675 < mouse_pointer[0] < 1076 and 620 < mouse_pointer[1] < 665)
    ]

    for i, frame in enumerate(option_frames):
        if i not in hidden_answers:
            if hover_conditions[i]:
                window.blit(option_hover, (frame.x - 2, frame.y - 12))
                draw_text(window, ABCD[i][0], "black", frame, qafont, True)
            else:
                draw_text(window, ABCD[i][0], "white", frame, qafont, True)

def draw_lifebuoys(window, lifebuoy_50, lifebuoy_time, lifebuoy_friend, used_lifebuoy_50, used_lifebuoy_time, used_lifebuoy_friend):
    if not used_lifebuoy_50:
        window.blit(lifebuoy_50, (520, 310))
    if not used_lifebuoy_time:
        window.blit(lifebuoy_time, (600, 310))
    if not used_lifebuoy_friend:
        window.blit(lifebuoy_friend, (680, 310))

def draw_score_table(window, score_table, question_number):
    if question_number <= 12:
        window.blit(score_table[question_number], (5, 5))

def show_friends():
    pass

def draw_text(surface, text, color, rect, font, aa=True, bkg=None):
    line_spacing = -2
    space_width, font_height = font.size(" ")[0], font.size("Tg")[1]

    list_of_words = str(text).split(" ")
    if bkg:
        image_list = [font.render(word, 1, color, bkg) for word in list_of_words]
        for image in image_list: image.set_colorkey(bkg)
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
        line_left += (rect[2] - line_len - space_width * (len(line_images)-1)) // 2
        
        if line_bottom + font_height > rect[1] + rect[3]:
            break
        last_line += 1
        for i, image in enumerate(line_images):
            x, y = line_left + i*space_width, line_bottom
            surface.blit(image, (round(x), y))
            line_left += image.get_width() 
        line_bottom += font_height + line_spacing

    if last_line < len(line_list):
        draw_words = sum([len(line_list[i]) for i in range(last_line)])
        remaining_text = ""
        for text in list_of_words[draw_words:]: remaining_text += text + " "
        return remaining_text
    return ""

