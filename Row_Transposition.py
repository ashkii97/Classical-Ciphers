import math
import random
from CipherInterface import *

class Rowtransposition(CipherInterface):

    def encrypt(self, text):
        key = self.key.replace(" ", "")
        rows = math.ceil(len(text) / len(key))
        table = [[''] * len(key) for i in range(rows)]
        idx = 0
        result = []

        for i in range(rows):
            for j in range(len(key)):
                if len(text) != idx:
                    table[i][j] = text[idx]
                    idx += 1
                else:
                    table[i][j] = chr(random.randrange(97, 97 + 26))

        for j in range(len(key)):
            for i in range(rows):
                result.append(table[i][int(key[j]) - 1])

        return("".join(result))

    def decrypt(self, text):
        key = self.key
        rows = math.ceil(len(text) / len(key))
        table = [[''] * len(key) for i in range(rows)]
        idx = 0
        result = []

        for j in range(len(key)):
            for i in range(rows):
                if len(text) != idx:
                    table[i][int(key[j]) - 1] = text[idx]
                    idx += 1

        for i in range(rows):
            for j in range(len(key)):
                result.append(table[i][j])

        return("".join(result))
