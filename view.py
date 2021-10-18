from tkinter import StringVar
from tkinter import ttk
from MyButton import MyButton

class View:
    def __init__(self, master):
        self.controller = None
        self.master = master
        self.main_frame = ttk.Frame(self.master)
        self.boardFrm = ttk.Frame(self.main_frame)
        self.boardFrm.grid(column=0, row=0)
        self.buttonsArray = [[],[],[],[],[],[],[],[]]
        for i in range(8):
            for j in range(8):
                self.buttonsArray[i].append(None)
        for i in range(8):
            if i%2 == 0:
                for j in range(8):
                    if j % 2 == 0:
                        self.buttonsArray[i][j] = MyButton(self.boardFrm, 'white', i, j)
                        self.buttonsArray[i][j].grid(row=i,column=j)
                    else:
                        self.buttonsArray[i][j] = MyButton(self.boardFrm, 'black', i, j)
                        self.buttonsArray[i][j].grid(row=i,column=j)
                    self.buttonsArray[i][j].configure(command= lambda: self.on_button_click())
            else:
                for j in range(8):
                    if j % 2 == 1:
                        self.buttonsArray[i][j] = MyButton(self.boardFrm, 'white', i, j)
                        self.buttonsArray[i][j].grid(row=i,column=j)
                    else:
                        self.buttonsArray[i][j] = MyButton(self.boardFrm, 'black', i, j)
                        self.buttonsArray[i][j].grid(row=i,column=j)
                    b= self.buttonsArray[i][j]
                    self.buttonsArray[i][j].configure(command= lambda: self.on_button_click(b))

        
        self.inputFrm = ttk.Frame(self.main_frame)
        self.inputFrm.grid(column=1, row=0)

        self.msLabel = ttk.Label(self.inputFrm, text="MS:")
        self.number_of_ms_input = ttk.Entry(self.inputFrm)
        self.dropdownLabel = ttk.Label(self.inputFrm, text="Number of Queens:")
        self.strvar = StringVar(self.inputFrm)
        self.strvar.set("One")
        self.dropdown_menu = ttk.OptionMenu(self.inputFrm, self.strvar, "One", "Two", "Three")
        
        self.msLabel.pack()
        self.number_of_ms_input.pack()
        self.dropdownLabel.pack()
        self.dropdown_menu.pack()

        self.buttonFrm = ttk.Frame(self.main_frame)
        self.buttonFrm.grid(columnspan=2, row=1, column=0)
        self.runButton = ttk.Button(self.buttonFrm, text="Run!")
        self.runButton.pack(side="left")
        self.resetButton = ttk.Button(self.buttonFrm, text="Reset")
        self.resetButton.pack(side="right")
        self.main_frame.pack()
    def on_button_click(self, b):
        print("clicked!")
        b.config(image=b.WHITE_IMAGE)