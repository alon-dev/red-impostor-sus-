import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image, ImageTk


class MyButton(tk.Button):
    def __init__(self, master, color, i, j):
        self.DEFAULT_IMAGE = PhotoImage()
        self.WHITE_IMAGE = PhotoImage(file="img/1.png")
        super().__init__(master, bg=color, image=self.DEFAULT_IMAGE, width=70, height=70, highlightthickness = 0, bd = 0)

