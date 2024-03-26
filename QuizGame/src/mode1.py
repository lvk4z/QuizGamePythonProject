import tkinter as tk
from tkinter import ttk, messagebox
from quizData import quiz_data


score = 0
current_question = 0


def showQuestion():
    global current_question
    question = quiz_data[current_question]
    question_label.config(text=question["question"])
    choices = question["choices"]

    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")

    check_label.config(text="")
    next_button.pack_forget()


def checkAnswer(choice):
    global score, current_question
    question = quiz_data[current_question]
    selected = choice_btns[choice].cget("text")
    if selected == question["answer"]:
        score += 1
        score_label.config(text="Wynik: {}".format(score))
        check_label.config(text="Poprawna odpowiedź", foreground="green")
    else:
        check_label.config(text="Zła odpowiedź", foreground="red")
    next_button.pack()


def nextQuestion():
    global current_question
    current_question += 1
    if current_question < len(quiz_data):
        showQuestion()
    else:
        messagebox.showinfo("Koniec","Twój wynik: {}".format(score))
        root.destroy()


def mainT1(frame):
    global root, question_label, choice_btns, check_label, score_label, next_button

    root = frame
    question_label = ttk.Label(
        root,
        anchor="center",
        wraplength=500,
        padding=10
    )
    question_label.pack(pady=10)

    choice_btns = []
    for i in range(4):
        button = ttk.Button(
            root,
            command=lambda i=i: checkAnswer(i)
        )
        button.pack(pady=5)
        choice_btns.append(button)

    check_label = ttk.Label(
        root,
        anchor="center",
        padding=10
    )
    check_label.pack(pady=10)

    score_label = ttk.Label(
        root,
        text="Wynik: {}".format(score),
        anchor="center",
        padding=10
    )
    score_label.pack(pady=10)

    next_button = ttk.Button(
        root,
        text="Next",
        command=nextQuestion
    )
    next_button.pack(pady=10)

    showQuestion()



