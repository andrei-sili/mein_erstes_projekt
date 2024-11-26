"""Aufgabe 8: Typkonvertierung"""
var_int = 32
if __name__ == "__main__":
    print("*" * 15, "Aufgabe 8: Typkonvertierung", "*" * 15)
    print(f"var_int = {var_int} type {type(var_int)}\n"
          f"var_int = {float(var_int)} type {type(float(var_int))}\n"
          f"var_int = {str(float(var_int))} type {type(str(float(var_int)))}")
