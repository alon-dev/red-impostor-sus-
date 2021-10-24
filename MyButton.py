import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image, ImageTk


class MyButton(tk.Button):
    def __init__(self, master, color, i, j, command):
        self.command = command
        self.i = i
        self.j = j
        self.DEFAULT_IMAGE = PhotoImage()
        self.WHITE_IMAGE = PhotoImage(file="img/1.png")
        super().__init__(master, bg=color, image=self.DEFAULT_IMAGE, width=70, height=70, highlightthickness = 0, bd = 0, command= self.my_command)
    def my_command(self):
        self.command(self)
    def reset(self):
        self.config(image=self.DEFAULT_IMAGE)
