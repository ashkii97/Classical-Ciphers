

class CipherInterface:

    def __init__(self):
        self.key = ""

    def setKey(self, key):
        self.key = key

    def encrypt(self, text):
        print("")

    def decrypt(self, text):
        print("")

    def cleanResult(self, str):
        return str.strip('\n').strip('\t')
