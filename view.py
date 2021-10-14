import tkinter as tk
from tkinter import Button, Frame
import numpy as np

from MyButton import MyButton

class View:
    def __init__(self, master):
        self.controller = None
        self.master = master
        self.boardFrm = Frame(self.master)
        self.boardFrm.grid(column=0, row=0)
        self.buttonsArray = [[],[],[],[],[],[],[],[]]
        for i in range(8):
            for j in range(8):
                self.buttonsArray[i].append(None)
        print(self.buttonsArray)
        for i in range(8):
            if i%2 == 0:
                for j in range(8):
                    if j % 2 == 0:
                        self.buttonsArray[i][j] = MyButton(self.boardFrm, 'white')
                        self.buttonsArray[i][j].grid(row=i,column=j)
                    else:
                        self.buttonsArray[i][j] = MyButton(self.boardFrm, 'black')
                        self.buttonsArray[i][j].grid(row=i,column=j)
            else:
                for j in range(8):
                    if j % 2 == 1:
                        self.buttonsArray[i][j] = MyButton(self.boardFrm, 'white')
                        self.buttonsArray[i][j].grid(row=i,column=j)
                    else:
                        self.buttonsArray[i][j] = MyButton(self.boardFrm, 'black')
                        self.buttonsArray[i][j].grid(row=i,column=j)
        self.inputFrm = Frame(self.master)
        self.inputFrm.grid(column=1, row=0)

        self.buttonFrm = Frame(self.master)
        self.buttonFrm.grid(columnspan=2, row=1, column=0)
        self.runButton = Button(self.buttonFrm, text="Run!", height=10, width=10)
        self.runButton.pack()