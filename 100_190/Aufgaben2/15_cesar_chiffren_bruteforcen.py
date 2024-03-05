"""
    Cäsar-Chiffre bruteforcen

    Schreibe ein Programm, das alle möglichen Lösungen
    eines Cäsar-chiffrierten Strings ausgibt.

    Was bedeutet "vxumxgssokxkt sginz yvgyy"?

    Wer Cäsar-Chiffre nicht kennt: https://de.wikipedia.org/wiki/Caesar-Verschlüsselung
"""

def brute_force_chiffre() -> list:
    cesar = "vxumxgssokxkt sginz yvgyy"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    erg_liste = []

    for verschiebung in range(0, 26):
        zwischen_erg = ''

        #print(f"DEBUG_Verschiebung: Verschiebung {verschiebung + 1}")

        for buchstabe in cesar:
            if buchstabe in alphabet:

                #https://de.wikipedia.org/wiki/Caesar-Verschl%C3%BCsselung#Algorithmus

                #index = (verschiebung - alphabet.find(buchstabe)) % 26

                index = (verschiebung + alphabet.find(buchstabe)) % 26
                zwischen_erg += alphabet[index]

                #print(f"DEBUG_Transformation: buchstabe '{buchstabe}' -> '{alphabet[index]}' (Index: {index})")
                #Leerzeichen?

            else:
                zwischen_erg += " "

                #print("DEBUG_Leerzeichen: true")

        erg_liste.append(f"Verschiebung {verschiebung + 1} = {zwischen_erg}")


    return erg_liste


for loesung in brute_force_chiffre():
    print(loesung)

print(f'\nDie entschlüsselte Nachricht lautet: {brute_force_chiffre()[20]}')



