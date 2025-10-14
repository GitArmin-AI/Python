# 9.4.6 while-else-Schleife
# Beispiel: Einkaufsliste mit while-Schleife

def einkaufen(einkaufsliste):
    print(f"Ich kaufe {einkaufsliste} ein.")

einkaufsliste = []
while (obstsorte := input("Gib eine Obstsorte ein (X zum Abbrechen): ")) != "X":
    if obstsorte == "Kiwi":
        print("Kiwis sind ausverkauft!")  
        break  
    einkaufsliste.append(obstsorte)  
else:
    einkaufen(einkaufsliste)
    print("Einkaufsliste vollständig.")

