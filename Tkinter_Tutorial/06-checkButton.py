import tkinter as tk
import tkinter.ttk as ttk

if __name__ == '__main__':

    window = tk.Tk()

    window.title("Welcome to LikeGeeks app")

    window.geometry('350x200')

    chk_state = tk.BooleanVar()
    chk_state.set(True) # set check state

    # Also, you can use it
    #chk_state = IntVar()
    #chk_state.set(0)  # uncheck
    #chk_state.set(1)  # check


    chk = ttk.Checkbutton(window, text='Choose', var=chk_state)
    chk.grid(column=0, row=0)

    window.mainloop()