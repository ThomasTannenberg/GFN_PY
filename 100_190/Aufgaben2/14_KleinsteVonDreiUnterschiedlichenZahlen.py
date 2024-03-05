"""
Kleinste von drei UNTERSCHIEDLICHEN Zahlen

Schreibe ein Programm,
das drei Variablen mit zufälligen,
UNTERSCHIEDLICHEN Zahlen (aus dem gleichen Zahlenraum) befüllt.
Dann soll das Programm testen,
welche der Zahlen die Kleinste ist und diese ausgeben.
"""
import random

def vergleiche_zahlen() -> str:
    zahl1 = random.randint(1, 100)
    zahl2 = random.randint(1, 100)
    zahl3 = random.randint(1, 100)

    kleinste_zahl = min(zahl1, zahl2, zahl3)
    return (f'die zahlen sind: {zahl1}, {zahl2}, {zahl3} und die kleinste Zahl ist {kleinste_zahl}')

print(vergleiche_zahlen())