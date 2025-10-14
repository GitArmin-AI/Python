# Set mit Zahlen
# Zahlen in einem Set sind immer einzigartig
zahlen={1,0}
zahlen.clear()
print(len(zahlen)) # 0
zahlen.add(3)
print(len(zahlen)) # 1
zahlen.add(2)
print(len(zahlen)) # 2
zahlen.add(3)
print(len(zahlen)) # 2
zahlen.remove(3)
print(len(zahlen)) # 1
zahlen.add(2)
print(len(zahlen)) # 1
zahlen.add(1)
print(len(zahlen)) # 2     
zahlen.add(1)
print(len(zahlen)) # 2
zahlen.remove(2)
print(len(zahlen)) # 1

gerade ={0,2,4,6,8,10}
kopie = gerade
kopie.remove(4)
print(gerade) # Ausgabe: {0, 2, 6, 8, 10}
print(kopie)  # Ausgabe: {0, 2, 6, 8, 10}
kopie.add(12)
kopie.add(8)

print(gerade) # Ausgabe: {0, 2, 6, 8, 10, 12}
kopie=gerade.copy()
kopie.add(14)       
print(gerade) # Ausgabe: {0, 2, 6, 8, 10, 12}

def prüfen(zahl, zahlen):
    if zahl in zahlen:
        return True      
    
    return False

print(prüfen(4,{2,3,4})) # Ausgabe: False