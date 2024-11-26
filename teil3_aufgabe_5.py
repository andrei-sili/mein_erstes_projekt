"""Aufgabe 5: Gerade Zahlen"""

if __name__ == "__main__":
    print("*" * 15, "Aufgabe 4: Zahlenbereiche", "*" * 15)
    print(*[i if i % 2 == 0 else "" for i in range(1, 21)], "-> geraden Zahlen von 1 bis 20")  # list generator
    print(*[i for i in range(1, 21, 5)], "-> jede 5. Zahl der Liste")  # list generator
