import sys

import numpy
import pandas
import random

import pygame
from pygame.locals import *


GREEN = (193, 203, 15)
BLACK = (0, 0, 0)


def drawProgressBar(surface, rect, progress):
    filled_rect = pygame.Rect(rect.left, rect.top, rect.width * progress, rect.height)
    pygame.draw.rect(surface, GREEN, filled_rect)

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

def mode1_play(window, width):

    bg_img = pygame.image.load('QuizGame/src/resources/game/bg.jpg').convert_alpha()
    option_hover = pygame.image.load('QuizGame/src/resources/game/answer_hover.png').convert_alpha()

    q_base_easy = pandas.read_excel('QuizGame/src/resources/questionsBase.xlsx', "easy", usecols = "A,B,C,D,E,F").to_dict('index')
    q_base_medium = pandas.read_excel('QuizGame/src/resources/questionsBase.xlsx', "medium", usecols = "A,B,C,D,E,F").to_dict('index')
    q_base_hard = pandas.read_excel('QuizGame/src/resources/questionsBase.xlsx', "hard", usecols = "A,B,C,D,E,F").to_dict('index')

    timerfont = pygame.font.SysFont('arial', 130)
    qafont = pygame.font.SysFont('arial', 20)
    full_time = 30
    time_left = 30
    question_number = 0
    running = True
    load_next_question = True
    start_time = pygame.time.get_ticks()
    while running:
        mouse_pointer = pygame.mouse.get_pos()
        time_left = full_time - (pygame.time.get_ticks()-start_time)/1000
        if int(time_left) >= 0:
            text = timerfont.render(str(int(time_left)), True, (184, 193, 209))
        window.blit(bg_img,(0,0))
        text_rect = text.get_rect(center=(width // 2, 200))
        window.blit(text, text_rect)

        if(time_left > 0.1):
            progress_rect = pygame.Rect(520, 330, 240, 16)  
            drawProgressBar(window, progress_rect, time_left/30)  
        
        if(load_next_question):
            if question_number <= 3:
                Q = q_base_easy[question_number]["PYTANIE"]
                ABCD = [(q_base_easy[question_number]["A"],True),(q_base_easy[question_number]["B"],False),(q_base_easy[question_number]["C"],False),(q_base_easy[question_number]["D"],False)]
                load_next_question = False
            elif  question_number <= 7:
                Q = q_base_medium[question_number-4]["PYTANIE"]
                ABCD = [(q_base_medium[question_number-4]["A"],True),(q_base_medium[question_number-4]["B"],False),(q_base_medium[question_number-4]["C"],False),(q_base_medium[question_number-4]["D"],False)]
                load_next_question = False
            else:
                Q = q_base_hard[question_number-8]["PYTANIE"]
                ABCD = [(q_base_hard[question_number-8]["A"],True),(q_base_hard[question_number-8]["B"],False),(q_base_hard[question_number-8]["C"],False),(q_base_hard[question_number-8]["D"],False)]
                load_next_question = False
        
        
        
        
        Q_frame = pygame.Rect(240, 430, 1045-240, 480-420)
        drawText(window, Q, "white", Q_frame, qafont, textAlignCenter, True)
        
        
        optionA_frame = pygame.Rect(210, 560, 370, 30)
        if 206 <  mouse_pointer[0] < 610 and 548 < mouse_pointer[1] < 598:
            window.blit(option_hover, (208, 548))
            drawText(window, ABCD[0][0], "black", optionA_frame, qafont, textAlignCenter, True)
        else:
            drawText(window, ABCD[0][0], "white", optionA_frame, qafont, textAlignCenter, True)

        optionB_frame = pygame.Rect(690, 560, 370, 30)
        if 675 <  mouse_pointer[0] < 1076 and 548 < mouse_pointer[1] < 598:
            window.blit(option_hover, (670, 548))
            drawText(window, ABCD[1][0], "black", optionB_frame, qafont, textAlignCenter, True)
        else:
            drawText(window, ABCD[1][0], "white", optionB_frame, qafont, textAlignCenter, True)
        
        optionC_frame = pygame.Rect(210, 630, 370, 30)
        if 206 <  mouse_pointer[0] < 610 and 620 < mouse_pointer[1] < 665:
            window.blit(option_hover, (206, 619))
            drawText(window, ABCD[2][0], "black", optionC_frame, qafont, textAlignCenter, True)
        else:
            drawText(window, ABCD[2][0], "white", optionC_frame, qafont, textAlignCenter, True)
        
        optionD_frame = pygame.Rect(690, 630, 370, 30)
        if 675 <  mouse_pointer[0] < 1076 and 620 < mouse_pointer[1] < 665:
            window.blit(option_hover, (674, 620))    
            drawText(window, ABCD[3][0], "black", optionD_frame, qafont, textAlignCenter, True)
        else:
            drawText(window, ABCD[3][0], "white", optionD_frame, qafont, textAlignCenter, True)
        
        
        pygame.display.update()
        
        for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 206 <  mouse_pointer[0] < 610 and 548 < mouse_pointer[1] < 598:
                            question_number += 1
                            start_time = pygame.time.get_ticks()
                            full_time = 30
                            if ABCD[0][1] == 'F':
                                sys.exit()
                            else: load_next_question = True
                        if 675 <  mouse_pointer[0] < 1076 and 548 < mouse_pointer[1] < 598:
                            question_number += 1
                            start_time = pygame.time.get_ticks()
                            full_time = 30
                            if ABCD[2][1] == 'F':
                              
                                sys.exit()
                            else:
                             
                                load_next_question = True
                        if 206 <  mouse_pointer[0] < 610 and 620 < mouse_pointer[1] < 665:
                            start_time = pygame.time.get_ticks()
                            full_time = 30
                            if ABCD[1][1] == 'F':
                                sys.exit()
                            else:
                                load_next_question = True
                        if 675 <  mouse_pointer[0] < 1076 and 620 < mouse_pointer[1] < 665:
                            question_number += 1
                            start_time = pygame.time.get_ticks()
                            full_time = 30
                            if ABCD[1][1] == 'F':
                                sys.exit()
                            else:
                                load_next_question = True

                        

                        if mouse_pointer[0] > 1106 and mouse_pointer[0] < 1106+143 and mouse_pointer[1] > 12 and mouse_pointer[1] < 12 + 24:
                            sys.exit()
