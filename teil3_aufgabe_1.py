"""Aufgabe 1: Zahlen zählen"""


def eins_zehn():
    n = 1
    while n <= 10:
        print(n, end=" ")
        n += 1


if __name__ == "__main__":
    print("*" * 15, "Aufgabe 1: Zahlen zählen", "*" * 15)
    eins_zehn()
