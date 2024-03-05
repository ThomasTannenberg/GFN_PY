"""
    Doppelte

    Schreibe eine Datei, die überprüft,
    ob in einer Liste doppelte Elemente sind.
    Dem Programm wird die Liste übergeben
    und sie soll den Boolean True zurückgeben,
    wenn es doppelte Elemente in der Liste gibt.
    Andernfalls soll die Funktion den Boolean False zurückgeben.
"""



def pruefung_liste(zahlen:list) -> bool:
    if len(zahlen) == len(set(zahlen)):
        return False
    else:
        return True



zahlen1 = [1, 3, 7, 9, 7, 11, 17]
zahlen2 = [1, 3, 7, 9, 11, 17]

print(f"checke doppelte bei {zahlen1}: ", pruefung_liste(zahlen1))  # True
print(f"checke doppelte bei {zahlen2}: ", pruefung_liste(zahlen2))  # False