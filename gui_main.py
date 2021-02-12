# -*- coding: utf-8 -*-
# GUI : tkinter
# 수치연산 : NumPy
# DB : pickle
# 데이터 분석 : pandas

import tkinter as tk




if __name__ == '__main__':
    window = tk.Tk()
    window.title("Welcome to LikeGeeks app")
    window.geometry('350x200')

    lbl = tk.Label(window, text="Hello", font=("Arial Bold", 50))
    lbl.grid(column=0, row=0)

    txt = tk.Entry(window, width=10) # state='disabled'
    txt.grid(column=1, row=0)
    txt.focus()

    def clicked():
        res = "Welcom to " + txt.get()
        lbl.configure(text= res)

    btn = tk.Button(window, text="Click Me", bg="orange", fg="red", command=clicked)
    btn.grid(column=2, row=0)

    window.mainloop()