"""Aufgabe 2: Benutzereingaben"""


def input_summ():
    num = int(input("Zahl eingeben: "))
    if num == 0:
        return num
    else:
        return num + input_summ()


if __name__ == "__main__":
    print("*" * 15, "Aufgabe 2: Benutzereingaben", "*" * 15)
    print(f"Summe aller eingegebenen Zahlen = {input_summ()}")
