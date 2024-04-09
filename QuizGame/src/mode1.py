import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import json
import random
import time


score = 0
current_question = 0
f = open("C:/Users/48516/Desktop/QuizGamePythonProject/QuizGame/src/data_quiz.json", encoding="utf-8")
quiz_data = json.load(f)["data_quiz"]
random.shuffle(quiz_data)

def showQuestion():
    global current_question
    question = quiz_data[current_question]
    question_label.config(text=question["question"])
    choices = question["choices"]

    for i in range(4):
<<<<<<< HEAD
        choice_labels[i].config(text=choices[i], bg="#003366", fg="white", cursor="hand2", relief=tk.RAISED, bd=2)





def checkAnswer(choice):
    global score, current_question
    
=======
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


    secondEntry.config(text=str(count))
    if(count == 8):
        DisableChoice()
        next_button.pack()
    else:
        root.after(1000, update_time)

def checkAnswer(choice):
    global score, current_question, count, flag
>>>>>>> ad93a6ef389e9817dea70724695086703f5cf7f1
    question = quiz_data[current_question]
    selected = choice_labels[choice].cget("text")
    for i in range(4):
        choice_labels[i].config(cursor="")
    if selected == question["answer"]:
        score += 1
        score_label.config(text="Wynik: {}".format(score))
        choice_labels[choice].config(bg="#6B8E23", fg="#003366", relief=tk.SOLID, bd=4)
        root.after(2000, nextQuestion)
    else:
<<<<<<< HEAD
        choice_labels[choice].config(bg="#8B0000", fg="white", relief=tk.SOLID, bd=4)
        for i in range(4):
            choice_labels[i].config(state="disabled")
        messagebox.showinfo("Koniec","Twój wynik: {}".format(score))
        root.destroy()
=======
        check_label.config(text="Zła odpowiedź", foreground="red")
    next_button.pack()
    DisableChoice()
    flag = 1
>>>>>>> ad93a6ef389e9817dea70724695086703f5cf7f1

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
<<<<<<< HEAD
    global root, question_label, choice_labels, check_label, score_label, next_button
    root = frame
=======
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

>>>>>>> ad93a6ef389e9817dea70724695086703f5cf7f1
    score_label = ttk.Label(
            root,
            text="Wynik: {}".format(score),
            anchor="center",
            padding=10,
            background="#222222",
            foreground="white" 
        )
    score_label.pack(pady=10)
    
    
    question_label = tk.Label(
        root,
        anchor="center",
        wraplength=800,
        width=800,
        height=4,
        background="#b2b234",  
        font=('Arial' ,25),
     
        foreground="white",  
        borderwidth=4, 
        relief=tk.GROOVE 
    )
<<<<<<< HEAD
    question_label.pack(pady=80,padx=10)
    timer_label = tk.Label(root,background="black")
    timer_label.pack(pady=20) 
    choice_labels = []
    for i in range(4):
        label = tk.Label(
            root,
            width=700,
            bg="#003366",  
            fg="white",   
            font=('Arial' ,27),
            padx=20,      
            pady=10,      
               
        )
        label.bind("<Button-1>", lambda event, i=i: checkAnswer(i))
        label.pack(pady=5, padx=50)
        choice_labels.append(label)

=======
    next_button.pack(pady=10)
    root.after(1000, update_time)
    #print(count)
>>>>>>> ad93a6ef389e9817dea70724695086703f5cf7f1
    showQuestion()
    return secondEntry



