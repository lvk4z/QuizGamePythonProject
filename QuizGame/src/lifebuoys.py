from mode1 import *
import random


def use_50_50(abcd):
        """Funkcja - użycie koła ratunkowego 50/50"""
        incorrect_answers = [i for i, ans in enumerate(abcd) if not ans[1]]
        return random.sample(incorrect_answers, 2)

def use_friends(window, category, ABCD):
    """Funkcja - użycie koła ratunkowego Przyjaciele"""
    friends = pygame.image.load('QuizGame/src/resources/game/friends.jpg').convert_alpha()
    running = True
    chosen_friend = None
    while running:
        mouse_pointer = pygame.mouse.get_pos()
        window.blit(friends, (330,0))
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == QUIT:
                    run = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 350 < mouse_pointer[0] < 500 and 60 < mouse_pointer[1] < 240:
                            chosen_friend = 'Animals'
                            running = False
                        if 550 < mouse_pointer[0] < 710 and 60 < mouse_pointer[1] < 240:
                            chosen_friend = 'Animals'
                            running = False
                        if 760 < mouse_pointer[0] < 910 and 60 < mouse_pointer[1] < 240:
                            chosen_friend = 'Animals'
                            running = False

    if chosen_friend:
        if chosen_friend == category:
            probability = 0.9
        else:
            probability = 0.5
        
        if random.random() < probability:
            correct_answer_index = next(i for i, ans in enumerate(ABCD) if ans[1])
        else:
            incorrect_answers = [i for i, ans in enumerate(ABCD) if not ans[1]]
            correct_answer_index = random.choice(incorrect_answers)
        
        return correct_answer_index
    return None
#

