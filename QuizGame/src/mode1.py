import sys

# basic func imports
import numpy
import pandas
import random

import pygame
from pygame.locals import *
import cv2

GREEN = (102, 163, 72)
BLACK = (0, 0, 0)
def draw_pulsating_circle(window, center, radius, min_radius, max_radius, thickness, color, pulse_speed):
 
    pulse_color = GREEN 
    pulse_progress = pygame.time.get_ticks() % pulse_speed / pulse_speed  
    gradient_color = [int(pulse_color[channel] * (1 - pulse_progress)) for channel in range(3)]

    pygame.draw.circle(window, color, center, radius, thickness)
    pygame.draw.circle(window, gradient_color, center, radius, 0) 

    pulse_radius = min_radius + ((max_radius - min_radius) / 2) * (1 + pulse_progress - 0.5) / 0.5
    pygame.draw.circle(window, color, center, int(pulse_radius), thickness)

def drawProgressBar(surface, color, rect, progress):
    filled_rect = pygame.Rect(rect.left, rect.top, rect.width * progress, rect.height)
    pygame.draw.rect(surface, color, filled_rect)

    pygame.draw.rect(surface, (0, 0, 0), rect, 2)

textAlignLeft = 0
textAlignRight = 1
textAlignCenter = 2
textAlignBlock = 3
def drawText(surface, text, color, rect, font, align=textAlignLeft, aa=True, bkg=None):

    lineSpacing = -2
    spaceWidth, fontHeight = font.size(" ")[0], font.size("Tg")[1]

    listOfWords = str(text).split(" ")
    if bkg:
        imageList = [font.render(word, 1, color, bkg) for word in listOfWords]
        for image in imageList: image.set_colorkey(bkg)
    else:
        imageList = [font.render(word, aa, color) for word in listOfWords]

    maxLen = rect[2]
    lineLenList = [0]
    lineList = [[]]
    for image in imageList:
        width = image.get_width()
        lineLen = lineLenList[-1] + len(lineList[-1]) * spaceWidth + width
        if len(lineList[-1]) == 0 or lineLen <= maxLen:
            lineLenList[-1] += width
            lineList[-1].append(image)
        else:
            lineLenList.append(width)
            lineList.append([image])

    lineBottom = rect[1]
    lastLine = 0
    for lineLen, lineImages in zip(lineLenList, lineList):
        lineLeft = rect[0]
        if align == textAlignRight:
            lineLeft += + rect[2] - lineLen - spaceWidth * (len(lineImages)-1)
        elif align == textAlignCenter:
            lineLeft += (rect[2] - lineLen - spaceWidth * (len(lineImages)-1)) // 2
        elif align == textAlignBlock and len(lineImages) > 1:
            spaceWidth = (rect[2] - lineLen) // (len(lineImages)-1)
        if lineBottom + fontHeight > rect[1] + rect[3]:
            break
        lastLine += 1
        for i, image in enumerate(lineImages):
            x, y = lineLeft + i*spaceWidth, lineBottom
            surface.blit(image, (round(x), y))
            lineLeft += image.get_width() 
        lineBottom += fontHeight + lineSpacing

    if lastLine < len(lineList):
        drawWords = sum([len(lineList[i]) for i in range(lastLine)])
        remainingText = ""
        for text in listOfWords[drawWords:]: remainingText += text + " "
        return remainingText
    return ""

def game(window, width, height, clock):
    # ładowanie obrazków
    

    bg_img = pygame.image.load('QuizGame/src/resources/game/background1.jpg').convert_alpha()

    time_left = 30
    running = True
    start_time = pygame.time.get_ticks()
    while running:
        time_left = 30 - (pygame.time.get_ticks()-start_time)/1000
        if int(time_left) >= 0:
            window.blit(bg_img,(0,0))
        
        window.blit(bg_img,(0,0))