import string
from CipherInterface import *

class Playfair(CipherInterface):

    def encrypt(self, text):
        key = self.key
        alphabet = "abcdefghiklmnopqrstuvwxyz"
        myList = []
        table = [[''] * 5 for i in range(5)]
        idx = 0

        for char in key:
            if char not in myList and char in alphabet:
                myList.append(char)

        for char in alphabet:
            if char not in myList:
                myList.append(char)

        for i in range(5):
            for j in range(5):
                table[i][j] = myList[idx]
                idx += 1

        for i in range(0,len(text) - 1,2):
            if text[i] == text[i+1]:
                text = text[:i+1] + "x" + text[i+1:]

        if len(text) % 2 == 1:
            text += "x"

        cipherText = ""
        for i in range(0, len(text), 2):
            firstLetterIdx = [(index, row.index(text[i])) for index, row in enumerate(table) if text[i] in row]
            secondLetterIdx = [(index, row.index(text[i+1])) for index, row in enumerate(table) if text[i+1] in row]

            if firstLetterIdx[0][0] == secondLetterIdx[0][0]:
                if int(firstLetterIdx[0][1]) != 4:
                    cipherText += table[int(firstLetterIdx[0][0])][int(firstLetterIdx[0][1]) + 1]
                if int(firstLetterIdx[0][1]) == 4:
                    cipherText += table[int(firstLetterIdx[0][0])][0]
                if int(secondLetterIdx[0][1]) == 4:
                    cipherText += table[int(secondLetterIdx[0][0])][0]
                else:
                    cipherText += table[int(secondLetterIdx[0][0])][int(secondLetterIdx[0][1]) + 1]
            elif firstLetterIdx[0][1] == secondLetterIdx[0][1]:
                if int(firstLetterIdx[0][0]) != 4:
                    cipherText += table[int(firstLetterIdx[0][0]) + 1][int(firstLetterIdx[0][1])]
                if int(firstLetterIdx[0][0]) == 4:
                    cipherText += table[0][int(firstLetterIdx[0][1])]
                if int(secondLetterIdx[0][0]) == 4:
                    cipherText += table[0][int(secondLetterIdx[0][1])]
                else:
                    cipherText += table[int(secondLetterIdx[0][0]) + 1][int(secondLetterIdx[0][1])]
            else:
                cipherText += table[int(firstLetterIdx[0][0])][int(secondLetterIdx[0][1])]
                cipherText += table[int(secondLetterIdx[0][0])][int(firstLetterIdx[0][1])]
        return cipherText

    def decrypt(self, text):
        key = self.key
        alphabet = "abcdefghiklmnopqrstuvwxyz"
        myList = []
        table = [[''] * 5 for i in range(5)]
        idx = 0

        for char in key:
            if char not in myList and char in alphabet:
                myList.append(char)

        for char in alphabet:
            if char not in myList:
                myList.append(char)

        for i in range(5):
            for j in range(5):
                table[i][j] = myList[idx]
                idx += 1

        plaintext = ""
        for i in range(0, len(text), 2):
            firstLetterIdx = [(index, row.index(text[i])) for index, row in enumerate(table) if text[i] in row]
            secondLetterIdx = [(index, row.index(text[i+1])) for index, row in enumerate(table) if text[i+1] in row]

            if firstLetterIdx[0][0] == secondLetterIdx[0][0]:
                if int(firstLetterIdx[0][1]) != 0:
                    plaintext += table[int(firstLetterIdx[0][0])][int(firstLetterIdx[0][1]) - 1]
                if int(firstLetterIdx[0][1]) == 0:
                    plaintext += table[int(firstLetterIdx[0][0])][4]
                if int(secondLetterIdx[0][1]) == 0:
                    plaintext += table[int(secondLetterIdx[0][0])][4]
                else:
                    plaintext += table[int(secondLetterIdx[0][0])][int(secondLetterIdx[0][1]) - 1]
            elif firstLetterIdx[0][1] == secondLetterIdx[0][1]:
                if int(firstLetterIdx[0][0]) != 0:
                    plaintext += table[int(firstLetterIdx[0][0]) - 1][int(firstLetterIdx[0][1])]
                if int(firstLetterIdx[0][0]) == 0:
                    plaintext += table[4][int(firstLetterIdx[0][1])]
                if int(secondLetterIdx[0][0]) == 0:
                    plaintext += table[4][int(secondLetterIdx[0][1])]
                else:
                    plaintext += table[int(secondLetterIdx[0][0]) - 1][int(secondLetterIdx[0][1])]
            else:
                plaintext += table[int(firstLetterIdx[0][0])][int(secondLetterIdx[0][1])]
                plaintext += table[int(secondLetterIdx[0][0])][int(firstLetterIdx[0][1])]

        temp = plaintext.replace('x', '')

        return temp
