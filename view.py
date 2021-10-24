from tkinter import PhotoImage, StringVar
from tkinter import ttk, messagebox
from Controller import Controller
from MyButton import MyButton
from time import sleep

class View:
    def __init__(self, master):
        self.controller = Controller()
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
                        self.buttonsArray[i][j] = MyButton(self.boardFrm, 'white', i, j, self.on_button_click)
                        self.buttonsArray[i][j].grid(row=i,column=j)
                    else:
                        self.buttonsArray[i][j] = MyButton(self.boardFrm, 'black', i, j, self.on_button_click)
                        self.buttonsArray[i][j].grid(row=i,column=j)
            else:
                for j in range(8):
                    if j % 2 == 1:
                        self.buttonsArray[i][j] = MyButton(self.boardFrm, 'white', i, j, self.on_button_click)
                        self.buttonsArray[i][j].grid(row=i,column=j)
                    else:
                        self.buttonsArray[i][j] = MyButton(self.boardFrm, 'black', i, j, self.on_button_click)
                        self.buttonsArray[i][j].grid(row=i,column=j)

        
        self.inputFrm = ttk.Frame(self.main_frame)
        self.inputFrm.grid(column=1, row=0)

        self.msLabel = ttk.Label(self.inputFrm, text="MS:")
        self.number_of_ms_input = ttk.Entry(self.inputFrm)
        self.dropdownLabel = ttk.Label(self.inputFrm, text="Number of Queens:")
        self.strvar = StringVar(self.inputFrm)
        self.strvar.set("One")
        self.dropdown_menu = ttk.OptionMenu(self.inputFrm, self.strvar, *["One", "One", "Two", "Three"])
        
        self.msLabel.pack()
        self.number_of_ms_input.pack()
        self.dropdownLabel.pack()
        self.dropdown_menu.pack()

        #dumb fuck nigger homo
        self.buttonFrm = ttk.Frame(self.main_frame)
        self.buttonFrm.grid(columnspan=2, row=1, column=0)
        self.runButton = ttk.Button(self.buttonFrm, text="Run!", command=self.run)
        self.runButton.pack(side="left")
        self.resetButton = ttk.Button(self.buttonFrm, text="Reset")
        self.resetButton.pack(side="right")
        self.main_frame.pack()
    def on_button_click(self, b):
        b.config(image=b.WHITE_IMAGE)
        self.controller.determinant_place(b.i, b.j)
    def run(self):
        try:
            number_of_ms = int(self.number_of_ms_input.get())
        except Exception as e:
            messagebox.showerror("Error!", "Please enter a valid ms timeout")
            return
        results = self.controller.show_results()
        if not results:
            messagebox.showerror("Error!", "No solutions found.")
            return
        self.show_results(results, number_of_ms)
    def show_results(self, results, number_of_ms):
        for res in results:
            for pair in res:
                print(pair) 
                self.on_button_click(self.buttonsArray[pair[0]][pair[1]])
                sleep(number_of_ms)