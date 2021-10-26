import os
from tkinter import PhotoImage, StringVar
from tkinter import ttk, messagebox
from Controller import Controller
from MyButton import MyButton
from time import sleep
import sys


class View:
    def __init__(self, master):
        self.controller = Controller()
        self.master = master
        self.main_frame = ttk.Frame(self.master)
        self.boardFrm = ttk.Frame(self.main_frame)
        self.boardFrm.grid(column=0, row=0)
        self.buttonsArray = [[], [], [], [], [], [], [], []]
        for i in range(8):
            for j in range(8):
                self.buttonsArray[i].append(None)
        for i in range(8):
            if i % 2 == 0:
                for j in range(8):
                    if j % 2 == 0:
                        self.buttonsArray[i][j] = MyButton(
                            self.boardFrm, 'white', i, j, self.on_button_click)
                        self.buttonsArray[i][j].grid(row=i, column=j)
                    else:
                        self.buttonsArray[i][j] = MyButton(
                            self.boardFrm, 'black', i, j, self.on_button_click)
                        self.buttonsArray[i][j].grid(row=i, column=j)
            else:
                for j in range(8):
                    if j % 2 == 1:
                        self.buttonsArray[i][j] = MyButton(
                            self.boardFrm, 'white', i, j, self.on_button_click)
                        self.buttonsArray[i][j].grid(row=i, column=j)
                    else:
                        self.buttonsArray[i][j] = MyButton(
                            self.boardFrm, 'black', i, j, self.on_button_click)
                        self.buttonsArray[i][j].grid(row=i, column=j)

        self.inputFrm = ttk.Frame(self.main_frame)
        self.inputFrm.grid(column=1, row=0)

        self.msLabel = ttk.Label(self.inputFrm, text="MS:")
        self.number_of_ms_input = ttk.Entry(self.inputFrm)
        self.dropdownLabel = ttk.Label(self.inputFrm, text="Number of Queens:")
        self.strvar = StringVar(self.inputFrm)
        self.strvar.set("1")
        self.dropdown_menu = ttk.OptionMenu(
            self.inputFrm, self.strvar, *["1", "1", "2", "3"])

        self.msLabel.pack()
        self.number_of_ms_input.pack()
        self.dropdownLabel.pack()
        self.dropdown_menu.pack()

        # dumb fuck nigger homo
        self.buttonFrm = ttk.Frame(self.main_frame)
        self.buttonFrm.grid(columnspan=2, row=1, column=0)
        self.runButton = ttk.Button(self.buttonFrm, text="Run!", command=self.run)
        self.runButton.pack(side="left")
        self.resetButton = ttk.Button(self.buttonFrm, text="Reset", command=self.reset)
        self.resetButton.pack(side="right")
        self.main_frame.pack()

    def on_button_click(self, b):
        b.config(image=b.WHITE_IMAGE)
        self.controller.determinant_place(b.i, b.j)

    def run(self):
        num = int(self.strvar.get())
        try:
            number_of_ms = int(self.number_of_ms_input.get() / 1000)
        except Exception as e:
            messagebox.showerror("Error!", "Please enter a valid ms timeout")
            return
        self.show_results(number_of_ms, num)

    def show_results(self, number_of_ms, num):
        count = 0
        try:
            for res in self.controller.show_results(num):
                count+=1
                for button_list in self.buttonsArray:
                    for button in button_list:
                        button.config(image=PhotoImage())
                for pair in res:
                    print(pair)
                    b = self.buttonsArray[pair[0]][pair[1]]
                    b.config(image=b.WHITE_IMAGE)
                self.master.update()
                sleep(number_of_ms)
            if count==0:
                messagebox.showinfo(message="No Solutions.")
        except ValueError:
            messagebox.showerror("Error!", "Error! Dropdown Menu and Clicks mismatch!")
    def reset(self):
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
