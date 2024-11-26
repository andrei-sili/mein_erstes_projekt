"""Aufgabe 3: Grundlegende Print-Ausgabe"""


def user_data():
    namen = "Andrei Sili"
    ausbildung = "Fachinformatiker"
    zitat = "Auch der weiteste Weg beginnt mit einem ersten Schritt"
    print(f"Meine Name ist {namen}, ich bin {ausbildung} und meine lieblings Zitat ist: '{zitat}'.")
    print("Meine Name ist {}, ich bin {} und meine lieblings Zitat ist: '{}'.".format(namen, ausbildung, zitat))




if __name__ == "__main__":
    print("*" * 15, "Aufgabe 3: Grundlegende Print-Ausgabe", "*" * 15)
    user_data()
