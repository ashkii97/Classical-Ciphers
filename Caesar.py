from CipherInterface import *

class Caesar(CipherInterface):

    def encrypt(self, text):
        result = ""
        k = int(self.key)

        for i in range(len(text)):
            char = text[i]
            result += chr((ord(char) + k - 97) % 26 + 97)

        return result

    def decrypt(self, text):
        result = ""
        k = int(self.key)
        print(k)
        for i in range(len(text)):
            char = text[i]
            result += chr(((ord(char) - k - 97) + 26) % 26 + 97)
        print(result)
        return result
