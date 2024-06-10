from gameEngine import *
from pygame.locals import *
import pygame
from utils.game_functions import load_images
from utils.drawing import draw_background
from config import WIDTH, HEIGHT, FLAGS, QUIT, MOUSEBUTTONDOWN

window = pygame.display.set_mode((WIDTH, HEIGHT), FLAGS)
images_menu = load_images()
bg_img = images_menu["menu_bg"]

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
                        mode_play(window, WIDTH, False)
                    elif 387 < mouse_pointer[1] < 450:
                        mode_play(window, WIDTH, True)
