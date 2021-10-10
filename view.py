import tkinter as tk
from tkinter import Frame

class View:
    def __init__(self, master):
         self.controller = None
         self.master = master
         boardFrm = Frame(self.master)
         boardFrm.grid(column=1, row=1)

         

         inputFrm = Frame(self.master)
         inputFrm.grid(column=2, row=1)

         buttonFrm = Frame(self.master)
         buttonFrm.grid(columnspan=2, row=2)