"""Aufgabe 6: Eingaben validieren"""


def zahl_validieren():
    while True:
        zahl = input("Bitte geben Sie ein Zahl ein: ")
        if zahl == "ende":
            print("Programm beendet")
            break
        if zahl.isdigit():
            print(f"'{zahl}' ist ein gültige Zahl")
        else:
            print(f"'{zahl}' keine gültige Zahl.")


if __name__ == "__main__":
    print("*" * 15, "Aufgabe 6: Eingaben validieren", "*" * 15)
    zahl_validieren()
