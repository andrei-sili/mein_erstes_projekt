"""
1.	Schreiben Sie ein Programm, das entscheidet, ob eine Zahl gerade oder ungerade ist.
"""


def gerade_ungerade():
    while True:
        zahl = input("Bitte geben Sie eine Zahl ein: ")
        try:
            if zahl == "ende":
                print("Programm beendet.")
                break
            zahl = int(zahl)
            if isinstance(zahl, int):
                if zahl % 2 == 0:
                    print(f"{zahl} ist gerade")
                else:
                    print(f"{zahl} ist ungerade")

        except ValueError:
            print("Die Eingabe war keine gültige Zahl. Bitte geben Sie eine ganze Zahl ein.")


"""
2.	Schreiben Sie ein Programm, das überprüft, ob eine eingegebene Zahl größer, 
kleiner oder gleich 100 ist.
"""


def vergleichen():
    while True:
        zahl = input("Bitte geben Sie eine Zahl ein: ")
        try:
            if zahl == "ende":
                print("Programm beendet.")
                break
            zahl = float(zahl)
            if isinstance(zahl, float):
                if zahl == 100:
                    print(f"{zahl} ist gleich 100 ")
                elif zahl > 100:
                    print(f"{zahl} ist größer als 100")
                elif zahl < 100:
                    print(f"{zahl} ist kleiner als 100")
            else:
                print("Die Eingabe war keine gültige Zahl.")
        except ValueError:
            print("Die Eingabe war keine gültige Zahl.")


"""3.	Schreiben Sie ein Programm, das prüft, ob ein Benutzer ein Passwort korrekt eingibt."""


def passwort_check():
    passwort = "passwort"
    while True:
        eingabe = input("Bitte geben Sie Ihr Passwort ein: ")
        if eingabe == passwort:
            print("Passwort ist korrekt!")
            break
        else:
            print("Falsches Passwort")


"""4.	Schreiben Sie ein Programm, das überprüft, ob eine Zahl zwischen 50 und 100 liegt."""


def ist_zwischen():
    while True:
        zahl = input("Bitte geben Sie eine Zahl ein: ")
        try:
            if zahl == "ende":
                print("Programm beendet.")
                break
            zahl = float(zahl)
            if isinstance(zahl, float):
                if 50 <= zahl <= 100:
                    print(f"Zahl {zahl} liegt zwischen 50 und 100  ")
                elif zahl > 100:
                    print(f"Zahl {zahl} ist größer als 100")
                elif zahl < 50:
                    print(f"Zahl {zahl} ist kleiner als 50")
            else:
                print("Die Eingabe war keine gültige Zahl.")
        except ValueError:
            print("Die Eingabe war keine gültige Zahl.")


"""5.	Schreiben Sie ein Programm, das das Alter eines Benutzers abfragt und prüft, ob er Auto fahren darf"""


def fahren_erlaubnis():
    while True:
        alter = input("Bitte geben Sie Ihr Alter ein: ")
        try:
            if alter == "ende":
                print("Programm beendet.")
                break
            alter = int(alter)
            if isinstance(alter, int):
                if alter >= 18:
                    print("Du darfst Auto fahren.")
                else:
                    if alter >= 16:
                        print("Du darfst einen Führerschein machen.")
                    else:
                        print("Du bist zu jung für den Führerschein.")
        except ValueError:
            print("Die Eingabe war keine gültige Zahl. Bitte geben Sie eine ganze Zahl ein.")


"""6.	Schreiben Sie ein Programm, das zwei Zahlen abfragt und entscheidet
o	Ob die Zahlen gleich sind.
o	Welche der beiden Zahlen größer ist.
o	Ob die Summe der beiden Zahlen gerade oder ungerade ist.
"""


def func():
    zahl_1 = input("Bitte geben Sie erste Zahl_1 ein: ")
    zahl_2 = input("Bitte geben Sie zweite Zahl_2 ein: ")
    try:
        zahl_1, zahl_2 = float(zahl_1), float(zahl_2)
        if isinstance(zahl_1 and zahl_2, float):
            if zahl_1 == zahl_2:
                print("Zahl_1 gleich Zahl_2")
            else:
                if zahl_1 > zahl_2:
                    print("Zahl_1 ist größer als Zahl_2")
                else:
                    print("Zahl_2 ist größer als Zahl_1")
        if (zahl_1 + zahl_2) % 2 == 0:
            print("Die Summe der beiden Zahlen ist gerade")
        else:
            print("Die Summe der beiden Zahlen ist ungerade")
    except ValueError:
        print("Die Eingabe war keine gültige Zahl.")


if __name__ == "__main__":
    print("*" * 15, "Aufgabe 2.1", "*" * 15)
    gerade_ungerade()  # Geben Sie "ende" ein, um das Programm zu beenden
    print("*" * 15, "Aufgabe 2.2", "*" * 15)
    vergleichen()  # Geben Sie "ende" ein, um das Programm zu beenden
    print("*" * 15, "Aufgabe 2.3", "*" * 15)
    passwort_check()  # Geben Sie "ende" ein, um das Programm zu beenden
    print("*" * 15, "Aufgabe 2.4", "*" * 15)
    ist_zwischen()  # Geben Sie "ende" ein, um das Programm zu beenden
    print("*" * 15, "Aufgabe 2.5", "*" * 15)
    fahren_erlaubnis()  # Geben Sie "ende" ein, um das Programm zu beenden
    print("*" * 15, "Aufgabe 2.6", "*" * 15)
    func()
