import numpy as np

class Model:
    def __init__(self):
        self.arr = [-1 for _ in range(8)]
        self.user_selcted = [False for _ in range(8)]
        self.count = 0
        self.results = []

    def threat(self, Q1, Q2):
        if Q1[0] == Q2[0]:
            return True
        if Q1[1] == Q2[1]:
            return True
        if abs(Q1[0] - Q2[0]) == abs(Q1[1] - Q2[1]):
            return True
        return False

    def isValidPlace(self, col, row):
        for i in range(col):
            if self.threat((row, col), (self.arr[i], i)):
                return False
        return True

    def rec_backt(self, col):
        if col == 8:
            self.count += 1
            self.results.append(self.arr.copy())
            return
        if self.user_selcted[col] == True:
            self.rec_backt(col + 1)
        else:
            for i in range(8):
                if self.isValidPlace(col, i):
                    self.arr[col] = i
                    self.rec_backt(col + 1)
                    self.arr[col] = -1


    def printb(self):
        board = np.array([[0 for _ in range(8)] for _ in range(8)])
        for i in range(8):
            board[i][self.arr[i]] = 1
        print(board)

