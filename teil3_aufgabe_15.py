"""Aufgabe 15: Indizes verwenden"""


def index_print():
    num_list = [4, 5, 0, 6, 2, 9, 1, 4]
    länge = len(num_list)
    for index in range(länge):
        print(f"Element [{num_list[index]}] : hat index -> [{index}]")
    print("=" * 50)
    for index in range(länge):
        print(f"  {index}", end="")
    print("\n", num_list)


if __name__ == "__main__":
    print("*" * 15, "Aufgabe 15: Indizes verwenden", "*" * 15)
    index_print()
