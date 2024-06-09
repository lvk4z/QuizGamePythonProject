import random
import requests
import urllib.parse
import time


def fetch_question(difficulty, category):
    """Fetch a single question from the Open Trivia Database API."""
    url = f"https://opentdb.com/api.php?amount=1&category={category}&difficulty={difficulty}&type=multiple&encode=url3986"
    try:
        response = requests.get(url)
    except (requests.ConnectionError, requests.Timeout) as e:
        print(f"XDASCXASXASError fetching question: {e}")
        return None  

    if response.status_code == 200:
        results = response.json()["results"]
        question = results[0]
        question["question"] = urllib.parse.unquote(question["question"])
        question["correct_answer"] = urllib.parse.unquote(question["correct_answer"])
        question["incorrect_answers"] = [
            urllib.parse.unquote(ans) for ans in question["incorrect_answers"]
        ]
        return question
    elif response.status_code == 429:
        print("Too many requests. Waiting before retrying...")
        
        return fetch_question(difficulty, category)
    else:
        print(f"Trying to fetch question again, reason: {response.status_code}")
        return fetch_question(difficulty,category)


def get_difficulty_level(question_number):
    """Map question number to difficulty level."""
    if question_number < 3:
        return "easy"
    elif question_number < 8:
        return "medium"
    else:
        return "hard"


def load_question(question_number):
    """Load question from the API and update the questions dictionary."""
    categories = [9, 22, 10, 27]
    difficulty = get_difficulty_level(question_number)
    category = random.choice(categories)
    return fetch_question(difficulty, category)


def parse_question(question):
    """Parse the question from the API and return shuffled options with the correct answer."""
    q_text = question["question"]
    correct_answer = question["correct_answer"]
    category = question["category"]
    incorrect_answers = question["incorrect_answers"]
    options = [[correct_answer, True]] + [[ans, False] for ans in incorrect_answers]
    random.shuffle(options)
    return q_text, options, category
