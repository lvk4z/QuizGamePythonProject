import tkinter as tk
from tkinter import ttk, messagebox
from mode1 import mainT1
from customtkinter import *
from ttkbootstrap import *

def main():
    root = CTk()
    style = Style(theme='darkly')  # You can change 'darkly' to other available themes
    root.style = style
    root.geometry("1000x650")
    root.title("QuizGame")
    set_appearance_mode("black")
    def uruchom_tryb1():
        title_label.pack_forget()
        przycisk_tryb1.pack_forget()
        przycisk_tryb2.pack_forget()
        tryb1.pack()
        entry = mainT1(tryb1)
    
    tryb1 = tk.Frame(root, background="black", height=1200)
    tryb2_frame = tk.Frame(root, background="black", height=1200)

    title_label = tk.Label(
        root,
        text="QuizGame",
        font=('Arial' ,30),
        anchor="center",
    )
    title_label.pack(pady=20)

    przycisk_tryb1 = tk.Button(
        root,
        text="Tryb 1 (ABCD)",
        command=uruchom_tryb1,
        font=('Arial', 30),
        width=300
    )
    przycisk_tryb1.pack(pady=10)

    przycisk_tryb2 = tk.Button(
        root,
        text="Tryb 2 (do zrobienia)",
        state="disabled",
        font=('Arial', 30),
        width=300

    )
    przycisk_tryb2.pack(pady=10)

    root.mainloop()
if __name__ == "__main__":
    main()
