import tkinter as tk
from tkinter import Menu

if __name__ == '__main__':

    window = tk.Tk()
    window.title("Welcome to LikeGeeks app")
    window.geometry('350x200')

    menu = Menu(window)
    new_item = Menu(menu)
    new_item.add_command(label='New')
    menu.add_cascade(label='File', menu=new_item)

    window.config(menu=menu)
    window.mainloop()