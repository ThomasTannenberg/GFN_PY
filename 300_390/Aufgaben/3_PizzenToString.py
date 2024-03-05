"""
Pizzen-String-Repräsentation

Erweitere die Klasse `Pizza` um eine Methode `__str__`, die das Verhalten der String-Repräsentation überlädt.
Eine Pizza soll als String dargestellt werden, der sowohl ihren Belag als auch ihre Größe enthält.

Teste die neue Methode mit dem folgenden Code:

class Pizza:
    def __init__(self, belag="Margherita", groesse=28):
        self.belag = belag
        self.groesse = groesse

# Beispiele für die Erstellung von Pizza-Instanzen und Ausgabe ihrer String-Repräsentation
p1 = Pizza()
p2 = Pizza("Salami", 32)
p3 = Pizza("Funghi", 30)

print(p1)  # Sollte ausgeben: Pizza mit Belag Margherita und Größe 28cm
print(p2)  # Sollte ausgeben: Pizza mit Belag Salami und Größe 32cm
print(p3)  # Sollte ausgeben: Pizza mit Belag Funghi und Größe 30cm

Anweisungen:
1. Definiere eine Klasse `Pizza` mit den Attributen `belag` und `groesse` und setze Standardwerte.
2. Implementiere die Methode `__str__`, die eine String-Repräsentation der Pizza zurückgibt, die den Belag und die Größe enthält.
3. Teste die Methode mit dem bereitgestellten Code.
"""