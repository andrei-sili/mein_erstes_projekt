"""Aufgabe 9: Sortieren und Umkehren"""
num_list = [5, 3, 8, 1, 2]

if __name__ == "__main__":
    print("*" * 15, "Aufgabe 9: Sortieren und Umkehren", "*" * 15)
    asc_sorted_num_list = sorted(num_list)
    print(f"Liste in aufsteigender Reihenfolge: -> {asc_sorted_num_list}")
    dow_sorted_num_list = sorted(num_list, reverse=True)
    print(f"Liste in absteigender Reihenfolge: -> {dow_sorted_num_list}")
    umg_num_list = num_list[::-1]  # umgekehrte Kopie der Liste, ohne die Original-Liste zu verändern.
    print(f"Umgekehrte Kopie der Liste, ohne die Original-Liste zu verändern-> {umg_num_list}")
    num_list.reverse()  # verändert die Original-Liste.
    print(f"Umgekehrte Reihenfolge der Elemente in der Liste, verändert die Original-Liste: -> {num_list}")
