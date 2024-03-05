# Konstruktor

class Pizza:
    def __init__(self, belagParam, durchmesserParam):
        self.belag = belagParam
        self.durchmesser = durchmesserParam

    def info(self):
        print(f"ich bin eine Pizza. Mein Belag ist {self.belag}, mein Durchmesser ist {self.durchmesser}")


pizza1 = Pizza("Fungi", 48)
pizza2 = Pizza("Fungi", 48)

print(pizza1.belag)
print(pizza1.durchmesser)
pizza1.info()




