from mode1 import *
from mode2 import *
from pygame.locals import *
import pygame   
from utils.drawing import draw_background
from config import WIDTH, HEIGHT, FLAGS, QUIT, MOUSEBUTTONDOWN

window = pygame.display.set_mode((WIDTH, HEIGHT), FLAGS)
bg_img = pygame.image.load('QuizGamePoetry/src/quizgamepoetry/resources/menu_bg.jpg').convert_alpha()

running = True
while True:
    mouse_pointer = pygame.mouse.get_pos()
    draw_background(window, bg_img)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if 540 < mouse_pointer[0] < 740:
                    if 276 < mouse_pointer[1] < 334:
                        mode1_play(window, WIDTH)
                    elif 387 < mouse_pointer[1] < 450:
                        mode2_play(window, WIDTH)
                        pass