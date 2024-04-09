# main
import tkinter as tk
from tkinter import ttk, messagebox
from customtkinter import *
from mode1 import mainT1


def main():
    global root
    root = CTk()
    
    root.geometry("1000x600")
    root.title("QuizGame")
    set_appearance_mode("black")
    
    def uruchom_tryb1():
        title_label.pack_forget()
        przycisk_tryb1.pack_forget()
        przycisk_tryb2.pack_forget()
        tryb1.pack()
    
    tryb1 = tk.Frame(root, background="black", height=1200)
    tryb2_frame = tk.Frame(root)

    title_label = ttk.Label(
        root,
        text="QuizGame",
        font=('Arial' ,30),
        anchor="center",
        padding=20
    )
    title_label.pack()

    przycisk_tryb1 = tk.Button(
        root,
        text="Tryb 1 (ABCD)",
        command=uruchom_tryb1,
        width=300,
        bg="white"
    )
    przycisk_tryb1.pack(pady=10)

    przycisk_tryb2 = ttk.Button(
        root,
        text="Tryb 2 (do zrobienia)",
        state="disabled"
    )
    przycisk_tryb2.pack(pady=10)

    mainT1(tryb1)

    root.mainloop()

if __name__ == "__main__":
    main()

#mode1
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
        choice_labels[i].config(text=choices[i], bg="#003366", fg="white", cursor="hand2", relief=tk.RAISED, bd=2)

def checkAnswer(choice):
    global score, current_question
    
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
        choice_labels[choice].config(bg="#8B0000", fg="white", relief=tk.SOLID, bd=4)
        for i in range(4):
            choice_labels[i].config(state="disabled")
        messagebox.showinfo("Koniec","Twój wynik: {}".format(score))
        root.destroy()

def nextQuestion():
    global current_question
    current_question += 1
    if current_question < len(quiz_data):
        showQuestion()
    else:
        messagebox.showinfo("Koniec","Twój wynik: {}".format(score))
        root.destroy()

def mainT1(frame):
    global root, question_label, choice_labels, check_label, score_label, next_button
    root = frame
    
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

    showQuestion()

