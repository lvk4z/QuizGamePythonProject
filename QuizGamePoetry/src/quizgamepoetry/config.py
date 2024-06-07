import pygame
from pygame.locals import DOUBLEBUF, HWSURFACE, QUIT, MOUSEBUTTONDOWN


pygame.init()
pygame.event.set_allowed([QUIT, MOUSEBUTTONDOWN])

WIDTH = 1280
HEIGHT = 720

FLAGS = DOUBLEBUF | HWSURFACE
