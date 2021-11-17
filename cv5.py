from random import randrange
import cv1, cv2, cv3, cv4, cv5, cv6


def tah_pocitace(pole, symbol):
    pozice = randrange(0, 19)
    if pole[pozice] == "-" and symbol == "x":
        return cv3.tah(pole, pozice, "o")
    else:
        return cv3.tah(pole, pozice, "x")