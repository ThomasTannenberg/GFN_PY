class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

class Cat(Animal):
    def speak(self):
        return f"{self.name} sagt Miau!"

# Verwendung der abgeleiteten Klassen
dog = Dog("Bello")
cat = Cat("Whiskers")

print(dog.speak())  # Ausgabe: "Bello sagt Wuff!"
print(cat.speak())  # Ausgabe: "Whiskers sagt Miau!"
