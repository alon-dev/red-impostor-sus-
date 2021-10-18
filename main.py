from tkinter import ttk, Tk
from view import View

root = Tk()
root.title("8 Queens")
style = ttk.Style(root)
style.configure("clam")
my_view = View(root)
root.mainloop()