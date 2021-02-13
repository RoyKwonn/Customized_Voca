import tkinter as tk
import tkinter.ttk as ttk

if __name__ == '__main__':

    window = tk.Tk()

    window.title("Welcome to LikeGeeks app")

    window.geometry('350x200')

    selected = tk.IntVar()

    rad1 = ttk.Radiobutton(window, text='First', value=1, variable=selected)
    rad2 = ttk.Radiobutton(window, text='Second', value=2, variable=selected)
    rad3 = ttk.Radiobutton(window, text='Third', value=3, variable=selected)

    def clicked():
        print(selected.get())

    btn = ttk.Button(window, text="Click Me", command=clicked)

    rad1.grid(column=0, row=0)
    rad2.grid(column=1, row=0)
    rad3.grid(column=2, row=0)
    btn.grid(column=3, row=0)

    window.mainloop()