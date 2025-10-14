#Berechnung
a = int(input("a = "))
b = int(input("b = "))
c = a + b
print(f"Die Summe der beiden Zahlen {a} und {b} ist {c}")

zahl =int(input("Welche Zahl willst Du verdoppeln? "))
verdoppelt = zahl * 2
print(f"Das Ergebnis lautet {verdoppelt}")

geld = float(input("Geld im Sparschwein "))
rest = geld - 5
print(f"Du hast noch {rest}€ im Sparschwein.")

rechnung = input("Was möchtest Du berechnen? ")
ergebnis = eval(rechnung)
print(f"Das Ergebnis von {rechnung} lautet: {ergebnis}")