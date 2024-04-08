import tkinter as tk
from tkinter import ttk, messagebox
from mode1 import mainT1
import time
def main():
    global root
    root = tk.Tk()
    root.title("QuizGame")
    root.geometry("600x600")
    def uruchom_tryb1():
        title_label.pack_forget()
        przycisk_tryb1.pack_forget()
        przycisk_tryb2.pack_forget()
        tryb1.pack()
        entry = mainT1(tryb1)
    
    tryb1 = ttk.Frame(root)
    tryb2_frame = ttk.Frame(root)

    title_label = ttk.Label(
        root,
        text="QuizGame",
        font=(30),
        anchor="center",
        padding=20
    )
    title_label.pack()

    przycisk_tryb1 = ttk.Button(
        root,
        text="Tryb 1 (ABCD)",
        command=uruchom_tryb1
    )
    przycisk_tryb1.pack(pady=10)

    przycisk_tryb2 = ttk.Button(
        root,
        text="Tryb 2 (do zrobienia)",
        state="disabled"
    )
    przycisk_tryb2.pack(pady=10)

    root.mainloop()
if __name__ == "__main__":
    main()
