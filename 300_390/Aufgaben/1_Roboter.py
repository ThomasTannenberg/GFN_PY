"""
Wir haben die folgende einfache Roboterklasse in Python:

class Roboter:
    def __init__(self, name):
        self.name = name


Diese Klasse ist plötzlich weltweit sehr beliebt geworden. Wir haben jedoch ein Problem:
Die internationale Robotergewerkschaft hat ein weltweites Verbot durchgesetzt, dass Roboter nicht mehr "Bernd" genannt werden dürfen.
Ändere nun die Klasse so ab, dass Roboter automatisch "Herbert" genannt werden, wenn jemand versucht,
sie "Bernd" zu taufen oder einen Roboter in "Bernd" umzubenennen.
Die Benutzer der Klasse sollten keine Änderungen bemerken, außer dass jetzt zweimal "Herbert" ausgegeben wird, wenn:

roboter_x = Roboter("Herbert")
roboter_y = Roboter("Bernd")
print(roboter_x.name + " und " + roboter_y.name)

Bitte teste auch das Umbenennen. Nach dem Versuch, einen Roboter in „Bernd” umzubenennen,
sollte der Name des Roboters „Herbert” sein:

roboter_z = Roboter("Stefan")
roboter_z.name = "Bernd"
print(roboter_z.name)  # Herbert
"""


class Roboter:
    alle_Roboter = []
    def __init__(self, name):
        if name == "Bernd":
            self.name = "Herbert"
        else:
            self.name = name
        Roboter.alle_Roboter.append(self)

    @classmethod
    def ausgabe_gesamt(cls):
        for robo in cls.alle_Roboter:
            print(robo)

    def __str__(self):
        return (f'{self.name}')


roboter_x = Roboter("Herbert")
roboter_y = Roboter("Bernd")
roboter_z = Roboter("Thorsten")

Roboter.ausgabe_gesamt()







