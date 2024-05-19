from mode1 import *


pygame.init()
pygame.event.set_allowed([QUIT, MOUSEBUTTONDOWN])
width = 1280
height = 720
flags = FULLSCREEN | DOUBLEBUF | HWSURFACE
window = pygame.display.set_mode((width,height), flags, 16)
clock = pygame.time.Clock()

mode1_play(window, width)