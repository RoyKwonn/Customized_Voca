try:
    import Tkinter as tk
except:
    import tkinter as tk

import time


class Clock():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="", font=('Helvetica', 48), fg='red')
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)


app = Clock()