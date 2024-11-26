"""Aufgabe 8: Erstellen und Manipulieren von Listen"""
namen_liste = ["Anna", "Max", "Tom", "Lisa"]

if __name__ == "__main__":
    print("*" * 15, "Aufgabe 7: Rückwärts iterieren", "*" * 15)
    namen_liste.append("Marie")
    namen_liste.remove("Tom")
    print(namen_liste)
    print(f"Länge der Liste = {len(namen_liste)} elementen")
