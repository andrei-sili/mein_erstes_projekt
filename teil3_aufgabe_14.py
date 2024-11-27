"""Aufgabe 14: Filtern von Elementen"""


def filtern():
    num_list = [2, 34, 10, 12, 45, 5, 7, -456, 9.99, 10.00001]
    for num in num_list:
        if num > 10:
            print(f"{num} < 10")
    

if __name__ == "__main__":
    print("*" * 15, "Aufgabe 14: Filtern von Elementen", "*" * 15)
    filtern()
