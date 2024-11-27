"""Aufgabe 10 Methoden für Listen"""
num_list = [1, 2, 3, 4, 5]

if __name__ == "__main__":
    print("*" * 15, "Aufgabe 10 Methoden für Listen", "*" * 15)
    num_list.append(6)
    print(f"Zahl 6 am Ende hinzugefügt: -> {num_list}")
    num_list.insert(0, 0)
    print(f"Zahl 0 an den Anfang der Liste hinzugefügt: -> {num_list}")
    count_3 = num_list.count(3)
    print(f"Zahl 3 vorkommt {count_3} in der Liste")