import tkinter as tk
from tkinter import ttk, messagebox
from quizData import quizData


score = 0
currentQuestion = 0


def showQuestion():
    global currentQuestion
    question = quizData[currentQuestion]
    questionLabel.config(text=question["question"])
    choices = question["choices"]

    for i in range(4):
        choiceBtns[i].config(text=choices[i], state="normal")

    checkLabel.config(text="")
    nextButton.pack_forget()


def checkAnswer(choice):
    global score, currentQuestion
    question = quizData[currentQuestion]
    selected = choiceBtns[choice].cget("text")
    if selected == question["answer"]:
        score += 1
        scoreLabel.config(text="Wynik: {}".format(score))
        checkLabel.config(text="Poprawna odpowiedź", foreground="green")
    else:
        checkLabel.config(text="Zła odpowiedź", foreground="red")
    nextButton.pack()


def nextQuestion():
    global currentQuestion
    currentQuestion += 1
    if currentQuestion < len(quizData):
        showQuestion()
    else:
        messagebox.showinfo("Koniec","Twój wynik: {}".format(score))
        root.destroy()


def mainT1(frame):
    global root, questionLabel, choiceBtns, checkLabel, scoreLabel, nextButton

    root = frame
    questionLabel = ttk.Label(
        root,
        anchor="center",
        wraplength=500,
        padding=10
    )
    questionLabel.pack(pady=10)

    choiceBtns = []
    for i in range(4):
        button = ttk.Button(
            root,
            command=lambda i=i: checkAnswer(i)
        )
        button.pack(pady=5)
        choiceBtns.append(button)

    checkLabel = ttk.Label(
        root,
        anchor="center",
        padding=10
    )
    checkLabel.pack(pady=10)

    scoreLabel = ttk.Label(
        root,
        text="Wynik: {}".format(score),
        anchor="center",
        padding=10
    )
    scoreLabel.pack(pady=10)

    nextButton = ttk.Button(
        root,
        text="Next",
        command=nextQuestion
    )
    nextButton.pack(pady=10)

    showQuestion()



