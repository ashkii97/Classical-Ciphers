from CipherInterface import *

class vigenere(CipherInterface):

    def newKey(self, text, key):
        if (len(text) > len(key)):
            j = 0
            new_key = key
            for i in range(len(text) - len(key)):
                new_key += key[j]
                if new_key[j] == key[-1]:
                    j = 0
                else:
                    j += 1
        return new_key

    def encrypt(self, text):
        key = self.newKey(text, self.key)
        cipher_text = []
        for i, j in zip(text, key):
            shift = ord(j) - ord('a')
            pos = ord('a') + (ord(i) - ord('a') + shift) % 26
            cipher_text.append(chr(pos))
        return("" . join([i for i in cipher_text]))

    def decrypt(self, text):
        key = self.newKey(text, self.key)
        orginal_text = []
        for i in range(len(text)):
            decipheredLetter = (ord(text[i]) - ord(key[i]) + 26) % 26
            decipheredLetter += ord('a')
            orginal_text.append(chr(decipheredLetter))
        return("" . join(orginal_text))
