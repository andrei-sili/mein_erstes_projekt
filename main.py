"""Aufgabe 1: Literale in Python"""
# Ganze Zahlen (int)
integer_literal = 42

# Gleitkommazahlen (float)
float_literal = 3.14159

# Zeichenfolgen (str)
string_literal = "Hallo, Welt!"

# Booleans (bool)
boolean_literal_true = True
boolean_literal_false = False

# Listen (list)
list_literal = [1, 2, 3, 4, 5]


# Ausgabe der Literale zur Überprüfung
def literal_print():
    print("Ganze Zahl (int):", integer_literal)
    print("Gleitkommazahl (float):", float_literal)
    print("Zeichenfolge (str):", string_literal)
    print("Boolean True (bool):", boolean_literal_true)
    print("Boolean False (bool):", boolean_literal_false)
    print("Liste (list):", list_literal)


"""Aufgabe 2: Bezeichner und Kommentare.
das verschiedene Variablentypen definiert und ihren Zweck beschreibt"""

# Anzahl der Artikel im Warenkorb (ganze Zahl)
cart_item_count = 5

# Preis eines einzelnen Artikels in Euro (Gleitkommazahl)
item_price = 19.99

# Gesamtpreis der Artikel im Warenkorb (berechnet)
total_price = cart_item_count * item_price

# Nachricht, die dem Benutzer angezeigt wird (Zeichenfolge)
welcome_message = "Willkommen in unserem Online-Shop!"

# Gibt an, ob der Benutzer eingeloggt ist (Boolean)
is_user_logged_in = True

# Liste von Kategorien, die im Shop verfügbar sind
shop_categories = ["Elektronik", "Mode", "Haushalt", "Sport"]


# Ausgabe der Variablen mit ihrer Bedeutung
def var_print():
    print("Anzahl der Artikel im Warenkorb:", cart_item_count)
    print("Preis pro Artikel:", item_price, "€")
    print("Gesamtpreis:", total_price, "€")
    print(welcome_message)
    print("Benutzer eingeloggt:", is_user_logged_in)
    print("Shop-Kategorien:", shop_categories)


"""Namensräume
Aufgabe 3: Lokale und globale Variablen"""

var_name = 7


def lokal_global_var():
    var_name = 3
    print(f"var_name = {var_name} -> ist lokale Variable")


"""Aufgabe 4: Verschachtelte Namensräume"""


def äußere_func():
    var = 0

    def innere_func():
        nonlocal var
        var += 1
        print(f"Innerer Wert von var: {var}")

    print(f"Vor Änderungen in äußere_func(): var = {var}")
    innere_func()
    innere_func()
    print(f"Nach Änderungen in äußere_func(): var = {var}")


"""Aufgabe 5: Wichtige Built-in Funktionen"""


def func():
    my_string = "Hallo Welt"
    my_list = [4, 2, 9, 7, 1]
    my_tuple = (10, 20, 30)

    # 1. len() und type() verwenden
    print("Länge des Strings:", len(my_string))  # Anzahl der Zeichen im String
    print("Typ der Variablen my_string:", type(my_string))  # Datentyp des Strings

    print("Länge der Liste:", len(my_list))  # Anzahl der Elemente in der Liste
    print("Typ der Variablen my_list:", type(my_list))  # Datentyp der Liste

    print("Typ der Variablen my_tuple:", type(my_tuple))  # Datentyp des Tupels

    # 2. sum(), max(), und min() für numerische Listen
    print("Summe der Elemente in der Liste:", sum(my_list))  # Summe aller Elemente
    print("Größtes Element in der Liste:", max(my_list))  # Maximum der Liste
    print("Kleinstes Element in der Liste:", min(my_list))  # Minimum der Liste

    # 3. sorted() zum Sortieren einer Liste
    print("Sortierte Liste (aufsteigend):", sorted(my_list))  # Liste aufsteigend sortiert
    print("Sortierte Liste (absteigend):", sorted(my_list, reverse=True))  # Liste absteigend sortiert


"""Aufgabe 6: Eingaben verarbeiten"""


def aufgabe_6():
    while True:
        # 1. Eingabe vom Benutzer erhalten und in eine ganze Zahl (int) konvertieren
        user_input = input("Bitte geben Sie eine Zahl ein: ")

        try:
            # Versuche, die Eingabe in eine ganze Zahl umzuwandeln
            user_number = int(user_input)
            print(f"Sie haben die Zahl {user_number} eingegeben.")

            # 2. Überprüfung des Typs mit isinstance()
            if isinstance(user_number, int):
                print("Die Eingabe ist vom Typ int.")
            else:
                print("Die Eingabe ist nicht vom Typ int.")  # Dieser Fall sollte hier nicht eintreten
        except ValueError:
            # Fehler, falls die Eingabe keine gültige Zahl ist
            print("Die Eingabe war keine gültige Zahl. Bitte geben Sie eine ganze Zahl ein.")


if __name__ == "__main__":
    print("*" * 15, "Aufgabe 1: Literale in Python", "*" * 15)
    literal_print()
    print("*" * 15, "Aufgabe 2: Bezeichner und Kommentare", "*" * 15)
    var_print()
    print("*" * 15, "Aufgabe 3: Lokale und globale Variablen", "*" * 15)
    lokal_global_var()
    print(f"var_name = {var_name} -> ist globale Variable")
    print("*" * 15, "Aufgabe 4: Verschachtelte Namensräume", "*" * 15)
    äußere_func()
    print("*" * 15, "Aufgabe 5: Wichtige Built-in Funktionen", "*" * 15)
    func()
    print("*" * 15, "Aufgabe 6: Eingaben verarbeiten", "*" * 15)
    aufgabe_6()
