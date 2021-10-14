import tkinter as tk
from tkinter import PhotoImage


class MyButton(tk.Button):
    def __init__(self, master, color):
        self.DEFAULT_IMAGE = PhotoImage()
        super().__init__(master, bg=color, image=self.DEFAULT_IMAGE, width=70, height=70, command= self.on_button_click)
        self.WHITE_IMAGE = PhotoImage(r"img\white_queen.png", width=70, height=70)

    def on_button_click(self):
        self.config(image=self.WHITE_IMAGE)
