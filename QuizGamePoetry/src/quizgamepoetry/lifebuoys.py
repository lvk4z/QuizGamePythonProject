from mode1 import *
import random


def use_fifty_fifty(answers):
    """
    Function - Use the 50/50 lifeline.

    Args:
    answers (list): List of options with their correctness.

    Returns:
    list: Two indices representing the incorrect options to be removed.
    """
    incorrect_answers = [i for i, ans in enumerate(answers) if not ans[1]]
    return random.sample(incorrect_answers, 2)


def use_friends_help(window, question_category, answers):
    """
    Function - Use the Friends lifeline.

    Args:
    window (pygame.Surface): The game window.
    question_category (str): The category of the question.
    answers (list): List of options with their correctness.

    Returns:
    int: Index of the correct answer suggested by the friend.
    """
    friends = pygame.image.load(
        "QuizGamePoetry/src/quizgamepoetry/resources/game/friends.jpg"
    ).convert_alpha()
    running = True
    chosen_friend = None
    while running:
        mouse_pointer = pygame.mouse.get_pos()
        window.blit(friends, (330, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 350 < mouse_pointer[0] < 500 and 60 < mouse_pointer[1] < 240:
                        chosen_friend = "Animals"
                        running = False
                    if 550 < mouse_pointer[0] < 710 and 60 < mouse_pointer[1] < 240:
                        chosen_friend = "History"
                        running = False
                    if 760 < mouse_pointer[0] < 910 and 60 < mouse_pointer[1] < 240:
                        chosen_friend = "Geography"
                        running = False

    if chosen_friend:
        if chosen_friend == question_category:
            probability = random.uniform(0.75, 0.85)
        else:
            probability = random.uniform(0.35, 0.55)

        if random.random() < probability:
            correct_answer_index = next(i for i, ans in enumerate(answers) if ans[1])
        else:
            incorrect_answers = [i for i, ans in enumerate(answers) if not ans[1]]
            correct_answer_index = random.choice(incorrect_answers)

        return correct_answer_index
    return None
