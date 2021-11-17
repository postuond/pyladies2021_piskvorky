import cv1, cv2, cv3, cv4, cv5, cv6


def tah(pole, pozice, symbol):
    try:
        return pole[:pozice] + symbol +pole[pozice + 1]

    except ValueError:
        if pozice not in pole:
            print("Pozice neni v poli!")
        elif pozice in pole == "x" or "o":
            print("Policko je obsazene")
        elif symbol != "x" or "o":
            print("Hrajes jinym symbolem!")
        elif pozice != int:
            print("Toto neni cislo!")
        elif pozice < 0:
            print("Cislo nesmi byt zaporne!")