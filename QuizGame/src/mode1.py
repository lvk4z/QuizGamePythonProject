import tkinter as tk
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
    global current_question, time_left

    question = quiz_data[current_question]
    question_label.config(text=question["question"])
    choices = question["choices"]
    time_left = 10
    timer_progress['value'] = 100
    for i in range(4):
        choice_labels[i].config(text=choices[i], bg="#003366", fg="white", cursor="hand2", relief=tk.RAISED, bd=2)


def checkAnswer(choice):
    global score, current_question, time_left
    
    question = quiz_data[current_question]
    selected = choice_labels[choice].cget("text")
    for i in range(4):
        choice_labels[i].config(cursor="")
    if selected == question["answer"]:
        score += 1
        score_label.config(text="Wynik: {}".format(score))
        choice_labels[choice].config(bg="#b2b234", fg="#003366", relief=tk.SOLID, bd=4)
        print("helo")
        time_left = 12
        timer_progress['value'] = 100
        root.after(2000, nextQuestion)
        
    else:
        choice_labels[choice].config(bg="#8B0000", fg="white", relief=tk.SOLID, bd=4)
        time_left = 0;
        for label in choice_labels:
            label.unbind("<Button-1>")
        messagebox.showinfo("Koniec","Twój wynik: {}".format(score))

        



def nextQuestion():
    global current_question
    current_question += 1
    if current_question < len(quiz_data):
        showQuestion()
    else:
        messagebox.showinfo("Koniec","Twój wynik: {}".format(score))
        

def update_timer():
        global time_left
        time_left -= 1
        timer_progress['value'] = time_left * 10
        if time_left == 0:
            messagebox.showinfo("Koniec czasu to koniec gry", "Twój wynik to : {}".format(score))
            
        else:
            root.after(1000, update_timer)

def start_timer():
    global time_left
    time_left = 10
    timer_progress['value'] = 100
    update_timer()


def mainT1(frame):
    global root, question_label, choice_labels, check_label, score_label,timer_progress
    root = frame
    
    

    score_label = ttk.Label(
            root,
            text="⭐ x{}".format(score),
            anchor="center",
            padding=10,
            background="#222222",
            font=('Arial' ,25),
            foreground="yellow" 

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
    question_label.pack(pady=80,padx=10)
    timer_frame = tk.Frame(root, background="black")
    timer_frame.pack(pady=10)
    
    timer_label = tk.Label(timer_frame, text="⏰ ", background="black", foreground="white", font=('Arial', 20))
    timer_label.pack(side=tk.LEFT)

    timer_progress = ttk.Progressbar(timer_frame, orient="horizontal", length=200, mode="determinate")
    timer_progress.pack(side=tk.LEFT)
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

    start_timer()
    showQuestion()



