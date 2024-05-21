from mode1 import *
from mode2 import *
from pygame.locals import *
import pygame
from utils import draw_background

pygame.init()
pygame.event.set_allowed([QUIT, MOUSEBUTTONDOWN])
width = 1280
height = 720
flags = FULLSCREEN | DOUBLEBUF | HWSURFACE
window = pygame.display.set_mode((width,height), flags, 16)
clock = pygame.time.Clock()
bg_img = pygame.image.load('QuizGame/src/resources/menu_bg.jpg').convert_alpha()
running = True
while True:
    mouse_pointer = pygame.mouse.get_pos()
    draw_background(window, bg_img)
    pygame.display.update()
    for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 540 < mouse_pointer[0] < 740 and 276 < mouse_pointer[1] < 334:
                        mode1_play(window, width)
                    if 540 < mouse_pointer[0] < 740 and 387 < mouse_pointer[1] < 450:
                        mode2_play(window, width)
