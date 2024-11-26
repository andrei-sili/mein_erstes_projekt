"""Aufgabe 7: Variablen mit verschiedenen Datentypen"""
var_type_dictionary = {"var_1": 13,
                       "var_2": 3.14,
                       "var_3": "text",
                       "var_4": False,
                       "var_5": [1, 2, "drei", 4.4, True],
                       "var_6": {1: "value_1", 2: "value_2"},
                       "var_7": (2, -3, "python"),
                       "var_8": 3 + 5j,
                       "var_9": {1, 2, 3, 4, 5, "text"},
                       "var_10": None,
                       "var_11": b"binary"
                       }
if __name__ == "__main__":
    print("*" * 15, "Aufgabe 7: Variablen mit verschiedenen Datentypen", "*" * 15)
    for key, value in var_type_dictionary.items():
        print(f"{key} = {value} : ist type >>>>>>>>>> {type(value)}")
