import tkinter as tk
from tkinter import ttk

if __name__ == '__main__':

    window = tk.Tk()
    window.title("Welcome to LikeGeeks app")
    window.geometry('350x200')

    tab_control = ttk.Notebook(window)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)

    tab_control.add(tab1, text='First')
    tab_control.add(tab2, text='Second')

    # lbl1 = tk.Label(tab1, text='label1')
    lbl1 = tk.Label(tab1, text='label1', padx=5, pady=5)
    lbl1.grid(column=0, row=0)

    lbl2 = tk.Label(tab2, text='label2')
    lbl2.grid(column=0, row=0)

    tab_control.pack(expand=1, fill='both')

    window.mainloop()