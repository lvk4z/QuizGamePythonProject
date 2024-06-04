import random
import requests
import urllib.parse

def fetch_questions(difficulty, category):
    """Funkcja pobierająca pytanie z API"""
    url = f'https://opentdb.com/api.php?amount=1&category={category}&difficulty={difficulty}&type=multiple&encode=url3986'
    try:
        response = requests.get(url)
    except (ConnectionError, TimeoutError):
        print("Response crashed")

    if response.status_code == 200:
        results = response.json()['results']
        for question in results:
            question['question'] = urllib.parse.unquote(question['question'])
            question['correct_answer'] = urllib.parse.unquote(question['correct_answer'])
            question['incorrect_answers'] = [urllib.parse.unquote(ans) for ans in question['incorrect_answers']]
        return results
    else:
        return fetch_questions(difficulty,category)

def load_question(questions, number):
    """Funkcja dopasowująca poziom trudności pytania i jego kategorię"""
    categories = [9, 22, 23, 27]
    if number < 3:
        difficulty = 'easy'
    elif number < 8:
        difficulty = 'medium'
    else:
        difficulty = 'hard'
    n = random.randint(0,3)
    questions[difficulty].extend(fetch_questions(difficulty, categories[n]))
    
    return questions


def parse_question(question):
    """Funkcja parsująca pytanie z API, zwraca zestaw pomieszanych odpowiedzi ABCD"""
    q_text = question['question']
    correct_answer = question['correct_answer']
    category = question['category']
    incorrect_answers = question['incorrect_answers']
    options = [[correct_answer, True] if (i == 0) else [incorrect_answers[i-1], False] for i in range(4)]
    #options = [(correct_answer, True)] + [(ans, False) for ans in incorrect_answers]
    random.shuffle(options)
    return q_text, options, category
