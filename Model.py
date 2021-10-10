import math


class Model:
    def __init__(self):
        self.arr = [-1 for _ in range(8)]
        self.count = 0

    def threat(self, Q1, Q2):
        if Q1[0] == Q2[0]:
            return True
        if Q1[1] == Q2[1]:
            return True
        if math.abs(Q1[0] - Q2[0]) == math.abs(Q1[1] - Q2[1]):
            return True
        return False

    def isValidPlace(self, col, row):
        for i in range(col):
            if self.threat((row, col), (self.arr[i], i)):
                return False
        return True

    def rec_backt(self, col):
        if col == 9:
            self.count += 1
            return
        for i in range(8):
            if self.isValidPlace(col, i):
                self.arr[col] = i
                self.rec_backt(col)
                self.arr[col] = -1

m = Model()
m.rec_backt(0)
print(m.count)
