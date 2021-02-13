import tkinter as tk
from tkinter import messagebox

if __name__ == '__main__':

    window = tk.Tk()
    window.title("Welcome to LikeGeeks app")
    window.geometry('350x200')

    def clicked():
        messagebox.showinfo('Message title', 'Message content')

    btn = tk.Button(window, text='Click here', command=clicked)
    btn.grid(column=0, row=0)

    def clicked1():
        messagebox.showwarning('Message title', 'Message content')

    btn1 = tk.Button(window, text='Click here', command=clicked1)
    btn1.grid(column=1, row=0)


    def clicked2():
        messagebox.showerror('Message title', 'Message content')

    btn2 = tk.Button(window, text='Click here', command=clicked2)
    btn2.grid(column=2, row=0)

    window.mainloop()