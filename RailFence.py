import math
from CipherInterface import *

class RailFence(CipherInterface):

    def encrypt(self, text):
        key = int(self.key)
        columns = math.ceil(len(text) / key)
        rail = [[''] * columns for i in range(key)]
        col = 0
        row = 0

        for i in range(len(text)):
            rail[row][col] = text[i]
            if row >= key-1:
                row = 0
                col += 1
            else:
                row += 1

        result = []
        for j in range(key):
            for i in range(columns):
                result.append(rail[j][i])
        return("".join(result))

    def decrypt(self, text):
        key = int(self.key)
        columns = math.ceil(len(text) / key)
        rail = [[''] * columns for i in range(key)]
        col = 0
        row = 0
        letters_per_row = len(text) / key
        remainder = len(text) % key

        for i in range(len(text)):
            rail[row][col] = text[i]
            if remainder > row:
                if letters_per_row - 1 <= col:
                    col = 0
                    row += 1
                else:
                    col += 1
            elif letters_per_row - 2 < col:
                col = 0
                row += 1
            else:
                col += 1

        result = []
        for j in range(columns):
            for i in range(key):
                result.append(rail[i][j])

        return("".join(result))
