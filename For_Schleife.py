# Die for-Schleife  in Python
# for zahl in range(1, 11):
#   print(zahl)     

zahlen = [1, 2, 3, 4, 5]
for zahl in zahlen:
    print(zahl)

teilnehmerliste = ["Pia", "Lea", "Menma", "Mia", "Lisa"]
for teilnehmer in teilnehmerliste:
    print(teilnehmer)

zeichenliste = []
for zeichen in "Python":
    zeichenliste.append(zeichen)
print(zeichenliste)

text = "Ich bin ein Programmierer"
statistik = {}
for zeichen in text:
    if zeichen in statistik:
        statistik[zeichen] += 1
    else:
        statistik[zeichen] = 1
print(statistik)

namen = {"Florian": "Dalwigk",
         "Hans": "Huber",
         "Mila": "Star",
         "Rei": "Hino",
         "Ayumi": "Tsukino"}
for vorname in namen:   
    print(f"{vorname}, {namen[vorname]}")

print(list(range(0,10)))  # list() wandelt einen Bereich in eine Liste um
print(list(range(0,10,2)))  # mit Schrittweite 2
print(list(range(10,0,-1)))  # rückwärts zählen mit Schrittweite -1     

namen = ["Leon", "Lexa", "Aron"]
for i in range(0,3):
    print(namen[i])

zahlen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(zahlen))  # Länge der Liste
for i in range(len(zahlen)-1, -1, -1):  # rückwärts zählen
    print(zahlen[i])

for i in range(1,100):
    if i % 3 == 0 and i % 7 == 0:
        print(f"{i} ist durch 3 und 7 teilbar")
        break
   
zahlen = [3, 4,15, 42, 99, 101]
for zahl in zahlen:
    if zahl == 4:
        continue
    print(zahl)

for _ in range(10):  # _ wird verwendet, wenn die Schleifenvariable nicht benötigt wird
    print("Hallo Welt!")

namen = ["Pam", "Mia", "Luna", "Ulf"]
for i, name in enumerate(namen):  # enumerate liefert den Index und den Wert
    print(f"Index: {i} - Name: {name}") 

M = [
    [1,2,3],
    [4,5,6]
]

zeilen = len(M)
spalten = len(M[0])
ergebnis = ""
for zeile in range(zeilen):
    for spalte in range(spalten):
        ergebnis += f"{M[zeile][spalte]}  "
    ergebnis += "\n"
print(ergebnis.strip())
#print(ergebnis)

print([zahl for zahl in range(0, 31, 2)])

# print(gerade)
gerade  = [zahl for zahl in range(0, 31) if zahl % 2 == 0]
print(gerade)

dictionary = {"A":0,"B":1,"C":2,"D":3,"E":4}
schlüsselliste = [schlüssel for schlüssel in dictionary.keys()]
werteliste = [wert for wert in dictionary.values()]
print(schlüsselliste)
print(werteliste)

# Aufbau einer Liste aus Tupeln
namen = ["Chan", "Kevin", "Mayu", "Haruka"]
print([(name,Index) for Index, name in enumerate(namen)])

print([(i,i*3) for i, name in enumerate(namen)])

obstsorten = ["Banane", "Melonen", "Ananas"]

for obst in obstsorten:
    if obst == "Melone":
        print(  f"Melone gefunden!"       )
        break
else:        
    print(  f"keine Melone gefunden."       )
# Das else gehört zur for-Schleife und wird ausgeführt, wenn die Schleife nicht durch break abgebrochen wurde.

zahl = 1
while zahl <= 10:
    print(zahl)
    zahl = zahl + 1

zahl = 0
fortfahren = "J"
while fortfahren == "J":
    zahl = zahl + 1
    print(zahl)
    fortfahren = input("Hochzählen? (J/N) ")
print(f"Du hast bis {zahl} gezählt.")

# Pokemons
# mit while-Schleife
pokemons = ["Pikachu", "Glumanda", "Bisasam", "Schiggy"]
index = 0
while index < len(pokemons):
    print(pokemons[index])
    index += 1

# mit for-Schleife
for pokemon in pokemons:
    print(pokemon)

# Nachbidung einer do-while-Schleife in Python
antwort = ""   
while True:
    antwort = input("Magst Du Python? (J/N) ")
    if antwort in ["J", "N"]:
        break     

# der Walross-Operator (ab Python 3.8)
teilnehmerliste = []
while (teilnehmer := input("Name des Teilnehmers (Ende zum Abbrechen): ")) != "Ende":
    teilnehmerliste.append(teilnehmer) 
print(teilnehmerliste)

# 9.4.6 while-else-Schleife
# Beispiel: Einkaufsliste mit while-Schleife
einkaufsliste = []
while (obstsorte := input("Gib eine Obstsorte ein (X zum Abbrechen): ")) != "X":
    if obstsorte == "Kiwi":
        print("Kiwis sind ausverkauft!")  
        break  
    einkaufsliste.append(obstorte)  
else:
    einkaufen(einkaufsliste)
    print("Einkaufsliste vollständig.")

def einkaufen(einkaufsliste):
    print(f"Ich kaufe {einkaufsliste} ein.")