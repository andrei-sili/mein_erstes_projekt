import sqlite3
class DB:
    def __init__(self, datenbank):
        """
        Initialisiert eine SQLite-Datenbank.
        :param datenbank: Name der SQLite-Datenbankdatei.
        """
        self.datenbank = datenbank
        self.connection = sqlite3.connect(self.datenbank)
        self.cursor = self.connection.cursor()

    def tabelle_erstellen(self, _tabelle_name, spalten_daten):
        """
        Erstellt eine Tabelle mit dynamischen Spalten.
        :param _tabelle_name: Name der Tabelle.
        :param spalten_daten: Liste der Spalten und ihrer Typen.
                              Beispiel: [("id", "INTEGER"), ("name", "TEXT")].
        """
        sql_spalten = ", ".join([f"{_spalten_name} {spalten_type}" for _spalten_name, spalten_type in spalten_daten])
        sql_anweisung = f"CREATE TABLE IF NOT EXISTS {_tabelle_name} ({sql_spalten})"
        self.cursor.execute(sql_anweisung)

    def daten_hinzufügen(self, _tabelle_name, _spalten, werte):
        """
        Fügt Daten in die Tabelle ein.
        :param _tabelle_name: Name der Tabelle.
        :param _spalten: Spaltennamen, in die Werte eingefügt werden sollen.
                         Beispiel: ["name", "email"].
        :param werte: Liste der Werte, die eingefügt werden sollen.
                      Beispiel: [("Alice", "alice@example.com"), ...].
        """
        platzhalter = ", ".join(["?"] * len(werte[0]))
        sql_spalten = ", ".join(_spalten)
        sql_anweisung = f'INSERT INTO {_tabelle_name} ({sql_spalten}) VALUES ({platzhalter})'
        self.cursor.executemany(sql_anweisung, werte)
        self.connection.commit()

    def daten_lesen(self, spalte_name, _tabelle_name):
        """
        Liest Daten aus einer Tabelle.
        :param spalte_name: Namen der Spalten, die gelesen werden sollen.
        :param _tabelle_name: Name der Tabelle.
        """
        sql_anweisung = f'SELECT {spalte_name} FROM {_tabelle_name}'
        self.cursor.execute(sql_anweisung)
        for reihe in self.cursor.fetchall():
            print(reihe)

    def daten_aktualisieren(self, _tabelle_name, aktualisierungen):
        """
        Aktualisiert Daten in einer Tabelle.
        :param _tabelle_name: Name der Tabelle.
        :param aktualisierungen: Liste von Aktualisierungen, mit SET und WHERE-Klauseln.
        """
        for spalten_set, werte_set, spalten_where, werte_where in aktualisierungen:
            set_klausel = ", ".join([f"{spalte} = ?" for spalte in spalten_set])
            where_klausel = " AND ".join([f"{spalte} = ?" for spalte in spalten_where])
            sql_abfrage = f"UPDATE {_tabelle_name} SET {set_klausel} WHERE {where_klausel}"
            werte = list(werte_set) + list(werte_where)
            self.cursor.execute(sql_abfrage, werte)
        self.connection.commit()
        print(f"Insgesamt wurden {self.cursor.rowcount} Zeilen aktualisiert.")

    def daten_filter(self, tabelle_name, bedingungen=None, order_by=None, limit=None):
        """
        Filtert Daten aus einer Tabelle basierend auf Bedingungen.
        :param tabelle_name: Name der Tabelle.
        :param bedingungen: Bedingungen als Wörterbuch.
        :param order_by: Sortierung der Ergebnisse.
        :param limit: Maximale Anzahl der Ergebnisse.
        """
        if bedingungen:
            where_klausel = " AND ".join([f"{spalte} {bedingung[0]} ?" for spalte, bedingung in bedingungen.items()])
            sql_abfrage = f"SELECT * FROM {tabelle_name} WHERE {where_klausel}"
            werte = [bedingung[1] for bedingung in bedingungen.values()]
        else:
            sql_abfrage = f"SELECT * FROM {tabelle_name}"
            werte = []
        if order_by:
            sql_abfrage += f" ORDER BY {order_by}"
        if limit:
            sql_abfrage += f" LIMIT {limit}"
        self.cursor.execute(sql_abfrage, tuple(werte))
        ergebnisse = self.cursor.fetchall()
        for reihe in ergebnisse:
            print(reihe)
        return ergebnisse

    def daten_suchen(self, tabelle_name, bedingungen=None):
        """
        Sucht Daten in einer Tabelle.
        :param tabelle_name: Name der Tabelle.
        :param bedingungen: Suchbedingungen als Wörterbuch.
        """
        if bedingungen:
            where_klausel = " OR ".join([f"{spalte} = ?" for spalte in bedingungen.keys()])
            sql_anweisung = f"SELECT * FROM {tabelle_name} WHERE {where_klausel}"
            werte = list(bedingungen.values())
        else:
            sql_anweisung = f"SELECT * FROM {tabelle_name}"
            werte = []
        self.cursor.execute(sql_anweisung, tuple(werte))
        ergebnisse = self.cursor.fetchall()
        for reihe in ergebnisse:
            print(reihe)
        return ergebnisse

    def daten_löschen(self, tabelle_name, bedingungen=None):
        """
        Löscht Daten aus einer Tabelle basierend auf Bedingungen.
        :param tabelle_name: Name der Tabelle.
        :param bedingungen: Löschbedingungen als Wörterbuch.
        """
        if not bedingungen:
            raise ValueError("Bedingungen sind erforderlich, um Daten sicher zu löschen.")
        where_klausel = " AND ".join([f"{spalte} = ?" for spalte in bedingungen.keys()])
        sql_anweisung = f"DELETE FROM {tabelle_name} WHERE {where_klausel}"
        werte = list(bedingungen.values())
        self.cursor.execute(sql_anweisung, tuple(werte))
        self.connection.commit()
        print(f"Daten wurden gelöscht mit Bedingungen: {bedingungen}")

    def close(self):
        """
        Schließt die Verbindung zur Datenbank.
        """
        self.connection.close()



def aufgabe1(benutzer_db, tabelle_name, spalten_name):
    """Aufgabe 1: Erstellen Sie eine Tabelle"""
    print("*" * 15, "Aufgabe 1.2: Erstellen Sie eine Tabelle", "*" * 15)
    benutzer_db.tabelle_erstellen(tabelle_name, spalten_name)

def aufgabe2(benutzer_db, tabelle_name):
    """Aufgabe 2: Lesen Sie Daten aus der Tabelle"""
    print("*" * 15, "Aufgabe 2: Daten aus der Tabelle lesen", "*" * 15)
    benutzer_db.daten_lesen("*", tabelle_name)

def aufgabe3(benutzer_db, tabelle_name, spalten, daten):
    """Aufgabe 3: Fügen Sie neue Benutzer hinzu"""
    print("*" * 15, "Aufgabe 3: Benutzer hinzufügen", "*" * 15)
    benutzer_db.daten_hinzufügen(tabelle_name, spalten, daten)

def aufgabe4(benutzer_db, tabelle_name, aktualisierungen):
    """Aufgabe 4: Aktualisieren Sie die Daten eines Benutzers"""
    print("*" * 15, "Aufgabe 4: Benutzer aktualisieren", "*" * 15)
    benutzer_db.daten_aktualisieren(tabelle_name, aktualisierungen)

def aufgabe5(benutzer_db, tabelle_name, alter_grenze):
    """Aufgabe 5: Filtern Sie Benutzer basierend auf dem Alter"""
    print("*" * 15, "Aufgabe 5: Benutzer nach Alter filtern", "*" * 15)
    bedingungen = {'age': ('>', alter_grenze)}
    benutzer_db.daten_filter(tabelle_name, bedingungen)

def aufgabe6(benutzer_db, tabelle_name, suchkriterien):
    """Aufgabe 6: Benutzer suchen"""
    print("*" * 15, "Aufgabe 6: Benutzer suchen", "*" * 15)
    benutzer_db.daten_suchen(tabelle_name, suchkriterien)

def aufgabe7(benutzer_db):
    """Aufgabe 7: To-Do-Liste erstellen und manipulieren"""
    print("*" * 15, "Aufgabe 7.1: To-Do-Liste erstellen", "*" * 15)
    tabelle_name_todo = "aufgaben"
    spalten_todo = [("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
                    ("titel", "TEXT"),
                    ("status", "TEXT")]
    benutzer_db.tabelle_erstellen(tabelle_name_todo, spalten_todo)

    print("*" * 15, "Aufgabe 7.2: Aufgaben hinzufügen", "*" * 15)
    spalten_todo = ("titel", "status")
    aufgaben_daten = [("Kaufen Milch", "offen"),
                      ("Schreiben einen Bericht", "offen"),
                      ("Buch lesen", "offen"),
                      ("Fitnessstudio besuchen", "offen"),
                      ("Freunde treffen", "offen")]
    benutzer_db.daten_hinzufügen(tabelle_name_todo, spalten_todo, aufgaben_daten)

    print("*" * 15, "Aufgabe 7.3: Alle Aufgaben anzeigen", "*" * 15)
    benutzer_db.daten_lesen("*", tabelle_name_todo)

    print("*" * 15, "Aufgabe 7.4: Aufgabe als erledigt markieren", "*" * 15)
    aufgabe_id = int(input("Geben Sie die ID der zu markierenden Aufgabe ein: "))
    aktualisierungen = [(("status",), ("erledigt",), ("id",), (aufgabe_id,))]
    benutzer_db.daten_aktualisieren(tabelle_name_todo, aktualisierungen)

    print("*" * 15, "Aufgabe 7.5: Aufgabe löschen", "*" * 15)
    aufgabe_id = int(input("Geben Sie die ID der zu löschenden Aufgabe ein: "))
    benutzer_db.daten_löschen(tabelle_name_todo, {'id': aufgabe_id})

def aufgabe8(benutzer_db, tabelle_name):
    """Aufgabe 8: Benutzerregistrierung und -login"""
    print("*" * 15, "Aufgabe 8.1: Benutzer registrieren", "*" * 15)
    name = input("Name eingeben: ")
    email = input("Email eingeben: ")
    passwort = input("Passwort eingeben: ")
    alter = input("Alter eingeben: ")
    benutzer_db.daten_hinzufügen(tabelle_name, ("name", "email", "age", "passwort"), [(name, email, alter, passwort)])

    print("*" * 15, "Aufgabe 8.2: Benutzer-Login", "*" * 15)
    email = input("Email eingeben: ")
    passwort = input("Passwort eingeben: ")
    suchkriterien = {'email': email, 'passwort': passwort}
    if benutzer_db.daten_suchen(tabelle_name, suchkriterien):
        print("Login erfolgreich!")
    else:
        print("Login fehlgeschlagen.")

    print("*" * 15, "Aufgabe 8.3: Alle registrierten Benutzer anzeigen", "*" * 15)
    benutzer_db.daten_lesen("*", tabelle_name)


if __name__ == "__main__":
    # Initialisiere Datenbank
    benutzer_db = DB("user_data.db")

    # Aufgabe 1: Tabelle erstellen
    tabelle_name = "benutzer"
    spalten_name = [("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
                    ("name", "TEXT"),
                    ("email", "TEXT"),
                    ("age", "TEXT"),
                    ("passwort", "TEXT")]
    aufgabe1(benutzer_db, tabelle_name, spalten_name)

    # Aufgabe 2: Daten aus der Tabelle lesen
    aufgabe2(benutzer_db, tabelle_name)

    # Aufgabe 3: Neue Benutzer hinzufügen
    benutzer_daten = [("Andrei", "andrei.sili1985@gmail.com", 39, "pass123"),
                      ("Aslam", "aslam.nabizada@yahoo.com", 23, "pass456"),
                      ("Guzelia", "guzelia.asambekova@mail.de", 30, "pass789")]
    aufgabe3(benutzer_db, tabelle_name, ("name", "email", "age", "passwort"), benutzer_daten)

    # Aufgabe 4: Benutzer aktualisieren
    aktualisierungen = [(("email",), ("neue.email@example.com",), ("id",), (1,))]
    aufgabe4(benutzer_db, tabelle_name, aktualisierungen)

    # Aufgabe 5: Benutzer nach Alter filtern
    aufgabe5(benutzer_db, tabelle_name, 25)

    # Aufgabe 6: Benutzer suchen
    suchkriterien = {'name': 'Andrei'}
    aufgabe6(benutzer_db, tabelle_name, suchkriterien)

    # Aufgabe 7: To-Do-Liste verwalten
    aufgabe7(benutzer_db)

    # Aufgabe 8: Benutzerregistrierung und -login
    aufgabe8(benutzer_db, tabelle_name)

    # Schließen der Datenbankverbindung
    benutzer_db.close()