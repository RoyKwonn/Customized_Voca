import tkinter as tk

if __name__ == '__main__':
    window = tk.Tk()

    window.title("Welcome to LikeGeeks app")

    window.geometry('350x200')

    lbl = tk.Label(window, text="Hello")

    lbl.grid(column=0, row=0)

    def clicked():
        lbl.configure(text="Button was clicked !!")

    btn = tk.Button(window, text="Click Me", command=clicked)

    btn.grid(column=1, row=0)

    window.mainloop()