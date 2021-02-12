import tkinter as tk

if __name__ == '__main__':
    window = tk.Tk()

    window.title("Welcome to LikeGeeks app")

    window.geometry('350x200')

    lbl = tk.Label(window, text="Hello")

    lbl.grid(column=0, row=0)

    txt = tk.Entry(window, width=10) # state='disabled'

    txt.grid(column=1, row=0)

    txt.focus() # Set focus to the entry widget

    def clicked():
        res = "Welcome to " + txt.get()
        lbl.configure(text= res)

    btn = tk.Button(window, text="Click Me", command=clicked)

    btn.grid(column=2, row=0)

    window.mainloop()