"""Upravte program z Lekce 2, který postupně načte od uživatele dvě čísla a operaci ('+', '-', '*' nebo '/') a provede na číslech příslušnou operaci.

Program upravte tak, aby:

při špatném vstupu napověděl co očekává a zeptal se znovu a
při dělení nulou vypsal hlášku Nulou nelze dělit.
Použijte na to ošetření příslušné chyby (tj. ne if delitel == 0:).

Příklad použití:

První číslo: třistatřiatřicet
Zadávej jen čísla
První číslo: 333
Druhé číslo: 0
Operace: /
Nulou nelze dělit."""


def calculator():
    while True:
        first_number = input("Enter first number: ")
        second_number = input("Enter second number: ")
        operation = input("Enter operation: ")
        try:
            if operation == "+":
                print(f"{first_number} + {second_number} =", int(first_number) + int(second_number))
                break
            elif operation == "-":
                print(f"{first_number} - {second_number} =", int(first_number) - int(second_number))
                break
            elif operation == "*":
                print(f"{first_number} * {second_number} =", int(first_number) * int(second_number))
                break
            elif operation == "/":
                print(f"{first_number} / {second_number} =", int(first_number) / int(second_number))
                break
            else:
                print("\nPlease type one of these operators: + - * /")

        except ValueError:
            print("\nPlease type numbers only!")

        except ZeroDivisionError:
            print("You can't divide by 0")


calculator()
