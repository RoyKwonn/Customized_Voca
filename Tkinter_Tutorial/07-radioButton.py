import tkinter as tk
import tkinter.ttk as ttk

if __name__ == '__main__':

    window = tk.Tk()

    window.title("Welcome to LikeGeeks app")

    window.geometry('350x200')

    rad1 = ttk.Radiobutton(window, text='First', value=1)
    rad2 = ttk.Radiobutton(window, text='Second', value=2)
    rad3 = ttk.Radiobutton(window, text='Third', value=3)


    rad1.grid(column=0, row=0)
    rad2.grid(column=1, row=0)
    rad3.grid(column=2, row=0)

    window.mainloop()