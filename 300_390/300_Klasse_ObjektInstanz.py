# Klasse

class Pizza:
    belag = "Salami" # Statische Attribute
    durchmesser = 20 # Statische Attribute

    def info(self):
        print(f"ich bin eine Pizza. Mein Belag ist {self.belag}, mein Durchmesser ist {self.durchmesser}")
        return None

pizza1 = Pizza()

print(pizza1.belag)
print(pizza1.durchmesser)
pizza1.info()
print(pizza1.info())

pizza1.belag = "Diavolo"
pizza1.durchmesser = 40

print("nach der Veränderung")
print(pizza1.belag)
print(pizza1.durchmesser)
print(pizza1.info())

