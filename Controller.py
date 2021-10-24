from Model import Model


class Controller:

    def __init__(self):
        self.model = Model()

    
    def determinant_place(self, i, j):
        self.model.arr[j] = i
        self.model.user_selcted[j] = True
    
    def show_results(self):
        ret = []
        self.model.rec_backt(0)
        for sol in self.model.results:
            solarr = []
            for i in range(8):
                solarr.append((i,sol[i]))
            ret.append(solarr)
        return ret
    