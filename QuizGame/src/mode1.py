import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import json
import random
import time


score = 0
current_question = 0
f = open("data_quiz.json", encoding="utf-8")
quiz_data = json.load(f)["data_quiz"]
random.shuffle(quiz_data)

def showQuestion():
    global current_question
    question = quiz_data[current_question]
    question_label.config(text=question["question"])
    choices = question["choices"]

    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")
    check_label.config(text="")
    next_button.pack_forget()


def DisableChoice():
    for i in range(4):
        choice_btns[i]["state"] = "disabled"


def EnableChoice():
    for i in range(4):
        choice_btns[i]["state"] = "enabled"

def update_time():
    global count
    global flag
    if(flag):
        return
    count += 1

    #print(count)

    secondEntry.config(text=str(count))
    if(count == 8):
        DisableChoice()
        next_button.pack()
    else:
        root.after(1000, update_time)

def checkAnswer(choice):
    global score, current_question, count, flag
    question = quiz_data[current_question]
    selected = choice_btns[choice].cget("text")
    if selected == question["answer"]:
        score += 1
        score_label.config(text="Wynik: {}".format(score))
        check_label.config(text="Poprawna odpowiedź", foreground="green")
    else:
        check_label.config(text="Zła odpowiedź", foreground="red")
    next_button.pack()
    DisableChoice()
    flag = 1

def timer(t1):
    for i in range(30, -1, -1):
        time.sleep(1.0)
        secondEntry.config(text = str(i))


def nextQuestion():
    global current_question, root, count, flag, secondEntry
    current_question += 1
    if current_question < len(quiz_data):
        showQuestion()
        count, flag = 0, 0
        secondEntry.config(text = "0")
        root.after(1000, update_time)
    else:
        messagebox.showinfo("Koniec","Twój wynik: {}".format(score))
        root.destroy()


def mainT1(frame):
    global root, question_label, choice_btns, check_label, score_label, next_button, secondEntry, count, flag
    count = 1
    flag = 0
    root = frame
    question_label = ttk.Label(
        root,
        anchor="center",
        wraplength=500,
        padding=10
    )


    secondEntry = ttk.Label(root, wraplength = 500, padding=10, font=("Calibri", 20), text = "1" )

    #secondEntry.place(x= 200, y=220)

    secondEntry.pack(pady = 10)
    question_label.pack(pady=10)

    choice_btns = []
    for i in range(4):
        button = ttk.Button(
            root,
            command=lambda k=i: checkAnswer(k)
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
    root.after(1000, update_time)
    #print(count)
    showQuestion()
    return secondEntry



