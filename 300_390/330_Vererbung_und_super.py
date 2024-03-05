# Basisklasse
class Animal:
    def __init__(self, name):
        self.name = name

    def breath(self):
        print(f"{self.name} atmet")

# erbende Klasse
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

animal = Animal("Heinrich")
dog = Dog("Bello")

animal.breath() # Heinrich atmet
dog.breath()  # Bello atmet
