from tkinter import messagebox

res = messagebox.askquestion('Message title','Message content')

res = messagebox.askyesno('Message title','Message content')

res = messagebox.askyesnocancel('Message title','Message content')

res = messagebox.askokcancel('Message title','Message content')

res = messagebox.askretrycancel('Message title','Message content')


# If you click OK or yes or retry, it will return True value, but if you choose no or cancel, it will return False.

# The only funpyction that returns one of three values is askyesnocancel function, it returns True or False or None.