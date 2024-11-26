"""Aufgabe 9: Grundlegende Fehlerbehandlung"""


class CustomException(Exception):
    """Benutzerdefinierte Ausnahme-Klasse für spezielle Fehler."""

    def __init__(self, message):
        super().__init__(message)

    @staticmethod
    def handle_input():
        """Fragt den Benutzer nach einer Zahl und gibt sie zurück."""
        try:
            eingabe = float(input("Geben Sie eine Zahl ein: "))
            return eingabe
        except ValueError:
            raise CustomException("Fehler: Die Eingabe ist keine gültige Zahl.")

    @staticmethod
    def check_negative_number(num):
        """Prüft, ob eine Zahl negativ ist, und löst einen Fehler aus, wenn dies der Fall ist."""
        if num < 0:
            raise CustomException("Fehler: Die Zahl ist negativ.")
        return num

    @staticmethod
    def divide_by_two(number):
        """Teilt die Zahl durch 2, behandelt jedoch mögliche Fehler."""
        try:
            re = number / 2
            return re
        except Exception as e:
            raise CustomException(f"Ein unbekannter Fehler ist aufgetreten: {str(e)}")

    @staticmethod
    def division_durch_null(zahlen):
        """Teilt zwei Zahlen und behandelt Division durch Null."""
        try:
            res = zahlen / 0
            return f"Das Ergebnis der Division ist: {res}"
        except ZeroDivisionError:
            return "Fehler: Division durch Null ist nicht erlaubt."


# Hauptprogramm
if __name__ == "__main__":
    try:
        print("*" * 15, "Aufgabe 9: Grundlegende Fehlerbehandlung", "*" * 15)

        # Schritt 1: Zahl eingeben
        zahl = CustomException.handle_input()

        # Schritt 2: Negative Zahl prüfen
        CustomException.check_negative_number(zahl)

        # Schritt 3: Division durch 2
        result = CustomException.divide_by_two(zahl)
        print(f"Das Ergebnis der Division durch 2 ist: {result}")

        # Schritt 3: Division durch 0
        ergebnis = CustomException.division_durch_null(zahl)
        print(ergebnis)

    except CustomException as ce:
        print(ce)
