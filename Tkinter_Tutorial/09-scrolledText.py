import tkinter as tk
from tkinter import scrolledtext

if __name__ == '__main__':

    window = tk.Tk()
    window.title("Welcome to LikeGeeks app")
    window.geometry('350x200')

    txt = tk.scrolledtext.ScrolledText(window, width=40, height=10)
    txt.grid(column=0, row=0)

    window.mainloop()