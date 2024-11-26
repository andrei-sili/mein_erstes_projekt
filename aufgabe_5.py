"""Aufgabe 5: Benutzereingabe"""


def begrüßung():
    name = input("Ihre Namen: ")
    beruf = input("Ihre Beruf: ")
    alter = input("Ihre Alter: ")
    print("\n--- Begrüßungsnachricht ---")
    print(f"Hallo {name}!\nDu bist {alter} Jahre alt und arbeitest als {beruf}.\nSchön, dich kennenzulernen!")


if __name__ == "__main__":
    print("*" * 15, "Aufgabe 5: Benutzereingabe", "*" * 15)
    begrüßung()
