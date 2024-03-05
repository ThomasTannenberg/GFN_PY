"""
    Bubblesort

    Schreibe eine Datei in
    der man eine Liste mit beliebig vielen Integern als Werten übergeben kann
    und die diese Liste sortiert und zurückgibt.

    Benutze hierzu den Bubblesort-Algorithmus.
    Bei diesem wird die Liste durchlaufen
    und jede Zahl mit der jeweils nachfolgenden Zahl verglichen.
    Wenn die nachfolgende Zahl kleiner ist,
    werden die Zahlen getauscht.
    Die Liste wird solange durchlaufen,
    bis bei einem Durchlauf keine Zahlen getauscht werden müssen.
"""
meineListe = []
print("Bitte geben Sie beliebige Zahlen ein.")
print("Zum Abbrechen geben Sie bitte 0 ein.")
while True:
    eingabe = input("Zahl: ")
    eingabe = int(eingabe)
    meineListe.append(eingabe)
    if eingabe == 0:
        break

sortierte_liste = sorted(meineListe)
print("Sortierte Liste:", sortierte_liste)