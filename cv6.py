import cv1, cv2, cv3, cv4, cv5


def piskvorky1d():
    pole = "-" * 20
    symbol = input("Vyber si symbol!\nx nebo o: ")
    while True:
        pole = cv4.tah_hrace(pole, symbol)
        print(pole)
        pole = cv5.tah_pocitace(pole, symbol)
        print(pole)

        if cv1.vyhodnot(pole) != "-":
            break


piskvorky1d()


