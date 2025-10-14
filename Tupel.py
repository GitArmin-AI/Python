# Kapitel 8.5.2 Tupel
tupel = (0,1,2,3,3,0)
kopie = tupel
print(tupel[2]) # Ausgabe: 2
print(kopie[5]) # Ausgabe: 0
print(tupel.index(0)) # Ausgabe: 0
index=tupel.index(3)
print(kopie[index]) # Ausgabe: 3
index= kopie.count(3)
print(tupel[index]) # Ausgabe: 2
print(5 in kopie)

def rechnen(a,b):
    return a+b, a-b, a*b, a/b

ergebnis=rechnen(6,3)
addition= ergebnis[0]
subtraktion= ergebnis[1]  
multiplikation= ergebnis[2] 
division= ergebnis[3]
print(addition, subtraktion, multiplikation, division)
a,b,c,d = rechnen(6,3)
print(f"Addition: {a} Division: {b} Multiplikation: {c} Division: {d}")

a= (1,2,3)
b= (4,5,6)
c= a+b
print(c)

a= [1,2,3]
b= [4,5]
c= (a,b)
c[1].append(6)
print(c)
