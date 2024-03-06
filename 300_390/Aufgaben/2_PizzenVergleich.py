"""
Pizzen-Vergleich

Erweitere die Klasse `Pizza` um eine Methode `__eq__`, die das Gleichheitsverhalten überlädt.
Zwei Pizzen sollen als gleich betrachtet werden, wenn sie die gleiche Größe und den gleichen Belag haben.

Teste die neue Methode mit dem folgenden Code:

class Pizza:
    def __init__(self, belag="Margherita", groesse=28):
        self.belag = belag
        self.groesse = groesse


# Beispiele für die Erstellung von Pizza-Instanzen
p1 = Pizza()
p2 = Pizza("Margherita")
p3 = Pizza(belag=28)
p4 = Pizza("Margherita", 28)

print(p1 == p2)  # True
print(p1 == p3)  # True
print(p1 == p4)  # True

p5 = None
str = "Margherita"
print(p1 == p5)   # False
print(p1 == str)  # False

p7 = Pizza("Salami")
p8 = Pizza(30)
p9 = Pizza("Funghi", 32)

print(p1 == p7)  # False
print(p1 == p8)  # False
print(p1 == p9)  # False

Anweisungen:
1. Definiere eine Klasse `Pizza` mit den Attributen `belag` und `groesse` und setze Standardwerte.
2. Implementiere die Methode `__eq__`, die zwei Pizzen auf Gleichheit überprüft.
3. Teste die Methode mit dem bereitgestellten Code.
"""

class Pizza:
    alle_pizzen = []

    def __init__(self, belag="Margherita", groesse=28):
        self.belag = belag
        self.groesse = groesse

        Pizza.alle_pizzen.append(self)

    def __eq__(self, pizza2):
        if isinstance(pizza2, Pizza):
            return self.belag == pizza2.belag and self.groesse == pizza2.groesse
        return False

    def print_alle_pizzen():
        for pizza in Pizza.alle_pizzen:
            print(f'Pizza: {pizza.belag}, Größe: {pizza.groesse}cm')


# Beispiele für die Erstellung von Pizza-Instanzen

p1 = Pizza()

p2 = Pizza("Margherita")

p3 = Pizza(belag=28)

p4 = Pizza("Margherita", 28)

print(p1 == p2)  # True

print(p1 == p3)  # True

print(p1 == p4)  # True

p5 = None

str = "Margherita"

print(p1 == p5)  # False

print(p1 == str)  # False

p7 = Pizza("Salami")

p8 = Pizza(30)

p9 = Pizza("Funghi", 32)

print(p1 == p7)  # False

print(p1 == p8)  # False

print(p1 == p9)  # False

Pizza.print_alle_pizzen()