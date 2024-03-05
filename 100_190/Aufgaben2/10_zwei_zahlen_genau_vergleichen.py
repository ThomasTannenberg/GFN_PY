"""
Zwei Zahlen genau vergleichen

Schreibe ein Programm, das zwei zufällige Zahlen erzeugt.
Dann soll das Programm testen und ausgeben,
welche von zwei Zahlen größer ist oder ob beide Zahlen gleich groß sind.
"""


import random

def vergleiche_zahlen() -> str:
    zahl1 = random.randint(1, 100)
    zahl2 = random.randint(1, 100)

    if zahl1 > zahl2:
        return f"Zahl 1 ({zahl1}) ist größer als Zahl 2 ({zahl2})."
    elif zahl1 < zahl2:
        return f"Zahl 2 ({zahl2}) ist größer als Zahl 1 ({zahl1})."
    else:
        return f"Beide Zahlen sind gleich groß ({zahl1})."

print(vergleiche_zahlen())

