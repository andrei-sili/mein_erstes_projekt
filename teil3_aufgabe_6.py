"""Aufgabe 6: Verschachtelte Schleifen"""


def stern_quadrat(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                print("*", end="  ")
            else:
                print("  ", end=" ")
        print(end="\n")


def quadrat(m):
    for i in range(m):
        print("*  " * 5)


if __name__ == "__main__":
    print("*" * 15, "Aufgabe 6: Verschachtelte Schleifen", "*" * 15)
    print("v1.0")
    größe = 5
    stern_quadrat(größe)
    print("v2.0")
    quadrat(größe)
