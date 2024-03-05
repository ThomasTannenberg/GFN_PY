# Attribute Anhängen

class Pizza:
    def __init__(self, belagParam, durchmesserParam):
        self.belag = belagParam
        self.durchmesser = durchmesserParam

    def info(self):
        print(f"ich bin eine Pizza. Mein Belag ist {self.belag}, mein Durchmesser ist {self.durchmesser}")


pizza1 = Pizza("Fungi", 48)
pizza2 = Pizza("Hawaii", 20)

print(pizza1.belag)
print(pizza1.durchmesser)
print(pizza1.info())

print("einem Objekt ein Attribut anhängen")
pizza1.temperatur = "heiß"
print(pizza1.temperatur)
# print(pizza2.temperatur) # AttributeError: 'Pizza' object has no attribute 'temperatur'



