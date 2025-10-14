# 9.5 Übungsaufgaben
name = input("Gib deinen Namen ein: ")
if name[0].lower() in "aeiou":
    print(f"Hallo {name.upper()}, dein Name beginnt mit einem Vokal.")   
else:
    print(f"Hallo {name}, dein Name beginnt mit einem Konsonanten.")

x = True
y = False   
if x and y or not x:
    print(y)  # Ausgabe: False
else:
    print(x)  # Ausgabe: True

stimmung = input("Wie ist deine Stimmung heute? (top/gut/schlecht): ").lower()
if stimmung == "top":
    print("Sehr gut!")
if stimmung == "gut":
    print("Das freut mich!")
elif stimmung == "schlecht":    
    print("Oh nein!.")