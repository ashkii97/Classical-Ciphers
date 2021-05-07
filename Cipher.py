import sys

from CipherInterface import CipherInterface
from Caesar import Caesar
from vigenere import vigenere
from RailFence import RailFence
from Row_Transposition import Rowtransposition
from Playfair import Playfair

try:
    cipherName = (sys.argv[1]).lower()
    key = sys.argv[2]
    encOrDec = (sys.argv[3]).lower()
    inFile = sys.argv[4]
    outFile = sys.argv[5]

    inputFile = open(inFile, "r")
    inFileData = inputFile.read()
    inputFile.close()

    if cipherName == "plf":
        cipher = Playfair()
    elif cipherName == "rts":
        cipher = Rowtransposition()
    elif cipherName == "rfc":
        cipher = RailFence()
    elif cipherName == "vig":
        cipher = vigenere()
    elif cipherName == "ces":
        cipher = Caesar()

    cipher.setKey(key)

    if encOrDec == "enc":
        outFileData = cipher.encrypt(cipher.cleanResult(inFileData))
    else:
        outFileData = cipher.decrypt(cipher.cleanResult(inFileData))

    outputFile = open(outFile, "w")
    outputFile.write(outFileData)
    outputFile.close()

except ValueError:
    print("Need Arguments")
