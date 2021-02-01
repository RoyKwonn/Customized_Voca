from tkinter import *
import pickle
from tkcalendar import Calendar, DateEntry

root = Tk()
root.geometry("400x400")
my_text1 = StringVar()
my_text2 = StringVar()
my_date = StringVar()
entry1 = Entry(root, textvariable=my_text1)
entry1.pack()
entry2 = Entry(root, textvariable=my_text2)
entry2.pack()
entry3 = DateEntry(root, textvariable=my_date)
entry3.pack()


def save():
    text = my_text1.get()
    with open("saved_settings.dat", "wb") as pickle_file:
        pickle.dump(text, pickle_file, pickle.HIGHEST_PROTOCOL)


def clear():
    my_text1.set('')


def load():
    with open("saved_settings.dat", "rb") as pickle_file:
        text = pickle.load(pickle_file)
    my_text1.set(text)


Button(root, text="Save Settings", command=save).pack()
Button(root, text="Clear", command=clear).pack()
Button(root, text="Load Settings", command=load).pack()
root.mainloop()
