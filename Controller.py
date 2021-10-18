from .Model import Model
from .view import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View()

    
    def determinant_place(self, i, j):
        self.model.arr[j] = i
        self.model.user_selcted[j] = True