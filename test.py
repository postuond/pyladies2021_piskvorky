from random import randrange


def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"


def tah(pole, pozice, symbol):
    try:
        n_pole = pole[:pozice] + symbol + pole[pozice + 1:]
        pole = n_pole
        return pole

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


def tah_hrace(herni_pole, symbol):
    while True:
        pozice = int(input("\nKam chces hrat?: "))
        if pozice >= 0 and pozice < len(herni_pole) and herni_pole[pozice] == "-":
            return tah(herni_pole, pozice, symbol)


def tah_pocitace(herni_pole, symbol):
    pozice = randrange(len(herni_pole))
    if herni_pole[pozice] == "-" and symbol == "x":
        return tah(herni_pole, pozice, symbol="o")
    elif herni_pole[pozice] == "-" and symbol == "o":
        return tah(herni_pole, pozice, symbol="x")


def piskvorky1d():
    pole = "-" * 20
    symbol = input("Vyber si symbol!\nx nebo o: ")
    while True:
        print(pole)
        pole = tah_hrace(pole, symbol)
        print(pole)

        if tah_hrace(pole, symbol="x"):
            pole = tah_pocitace(pole, symbol="o")
            print(pole)
        else:
            pole = tah_pocitace(pole, symbol="x")
            print(pole)

        if vyhodnot(pole) != '-':
            break

    if vyhodnot(pole) == '!':
        print('Remíza!')
    elif vyhodnot(pole) == 'x':
        print('Vyhrála jsi!')
    elif vyhodnot(pole) == 'o':
        print('Vyhrál počítač!')


piskvorky1d()