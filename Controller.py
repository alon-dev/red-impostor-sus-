from Model import Model


class Controller:

    def __init__(self):
        self.model = Model()
        self.select = 0
    
    def determinant_place(self, i, j):
        self.model.arr[i] = j
        self.model.user_selcted[i] = True
        self.select += 1
    
    def show_results(self, num_of_queens_input):
        if self.select == num_of_queens_input:
            self.model.rec_backt(0)
            for sol in self.model.results:
                solarr = []
                for i in range(8):
                    solarr.append((i,sol[i]))
                yield solarr
        else:
            raise ValueError("Dropdown must match clicks")
    