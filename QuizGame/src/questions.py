import random
import requests
import urllib.parse

def fetch_questions(difficulty, category):
    url = f'https://opentdb.com/api.php?amount=1&difficulty={difficulty}&category={category}&type=multiple&encode=url3986'
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()['results']
        for question in results:
            question['question'] = urllib.parse.unquote(question['question'])
            question['correct_answer'] = urllib.parse.unquote(question['correct_answer'])
            question['incorrect_answers'] = [urllib.parse.unquote(ans) for ans in question['incorrect_answers']]
        return results
    else:
        return []

def load_question(questions, number):
    categories = [9, 22, 23, 27]
    if number <= 3:
        difficulty = 'easy'
    elif number <= 8:
        difficulty = 'medium'
    else:
        difficulty = 'hard'

    questions[difficulty].extend(fetch_questions(difficulty, categories[random.randint(0, 3)]))
    
    return questions


def parse_question(question):
    q_text = question['question']
    correct_answer = question['correct_answer']
    incorrect_answers = question['incorrect_answers']
    options = [(correct_answer, True)] + [(ans, False) for ans in incorrect_answers]
    random.shuffle(options)
    return q_text, options
