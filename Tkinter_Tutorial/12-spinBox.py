import tkinter as tk


if __name__ == '__main__':

    window = tk.Tk()
    window.title("Welcome to LikeGeeks app")
    window.geometry('350x200')

    spin = tk.Spinbox(window, from_=0, to=100, width=5)
    spin.grid(column=0, row=0)

    spin1 = tk.Spinbox(window, values=(3, 8, 11), width=5)
    spin1.grid(column=1, row=0)

    var = tk.IntVar()
    var.set(36)
    spin2 = tk.Spinbox(window, from_=0, to=100, width=5, textvariable=var)
    spin2.grid(column=2, row=0)

    window.mainloop()