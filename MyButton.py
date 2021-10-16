import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk


class MyButton(tk.Button):
    def __init__(self, master, color):
        self.DEFAULT_IMAGE = PhotoImage()
        self.WHITE_IMAGE = PhotoImage(file="img/1.png")
        super().__init__(master, bg=color, image=self.DEFAULT_IMAGE, width=70, height=70, command= self.on_button_click)

    def on_button_click(self):
        print("clicked!")
        self.config(image=self.WHITE_IMAGE)

