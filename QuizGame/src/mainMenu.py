import tkinter as tk
from tkinter import ttk, messagebox
from mode1 import mainT1

def main():
    root = tk.Tk()
    root.title("QuizGame")
    root.geometry("600x600")
    def uruchom_tryb1():
        titleLabel.pack_forget()
        przyciskTryb1.pack_forget()
        przyciskTryb2.pack_forget()
        tryb1.pack()
    
    tryb1 = ttk.Frame(root)
    tryb2_frame = ttk.Frame(root)

    titleLabel = ttk.Label(
        root,
        text="QuizGame",
        font=(30),
        anchor="center",
        padding=20
    )
    titleLabel.pack()

    przyciskTryb1 = ttk.Button(
        root,
        text="Tryb 1 (ABCD)",
        command=uruchom_tryb1
    )
    przyciskTryb1.pack(pady=10)

    przyciskTryb2 = ttk.Button(
        root,
        text="Tryb 2 (do zrobienia)",
        state="disabled"
    )
    przyciskTryb2.pack(pady=10)

    mainT1(tryb1)

    root.mainloop()

if __name__ == "__main__":
    main()
