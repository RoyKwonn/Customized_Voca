# -*- coding: utf-8 -*-
import tkinter as tk

try:
    import tkinter as tk            # python 3
    import tkinter.ttk as ttk       # python 3
except ImportError:
    import Tkinter as tk            # python 2
    import tkFont as tkfont         # python 2

class SampleApp(tk.Tk):
    


if __name__ == '__main__':

    window = tk.Tk()
    window.title("Customized Voca app")
    window.geometry('320x460')

    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background='black')

    bar = ttk.Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
    bar['value'] = 70
    bar.grid(column=0, row=0)

    lbl = tk.Label(window, text="ID : ")
    lbl.grid(column=0, row=1)
    txt = tk.Entry(window, width=10)  # state='disabled'
    txt.grid(column=1, row=1)
    txt.focus()  # Set focus to the entry widget
    def clicked():
        res = "Welcome to " + txt.get()
        lbl.configure(text=res)
    btn = tk.Button(window, text="Click Me", command=clicked)
    btn.grid(column=2, row=1)

    rad1 = ttk.Radiobutton(window, text='First', value=1)
    rad2 = ttk.Radiobutton(window, text='Second', value=2)
    rad3 = ttk.Radiobutton(window, text='Third', value=3)

    rad1.grid(column=0, row=4)
    rad2.grid(column=0, row=5)
    rad3.grid(column=0, row=6)

    window.mainloop()