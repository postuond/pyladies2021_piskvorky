import cv1, cv2, cv3, cv4, cv5, cv6


def tah_hrace(pole, symbol):
    pozice = int(input("\nKam chces hrat?: "))
    while True:
        if pozice >= 0 and pozice < len(pole) and pole[pozice] == "-":
            print(cv3.tah(pole, pozice, symbol))
            return cv3.tah(pole, pozice, symbol)
        else:
            pozice = input("\nKam chces hrat?: ")
