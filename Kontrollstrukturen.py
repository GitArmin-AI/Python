# Kontrollstrukturen in Python
alter = int(input("Wie alt bist Du?"))   
if alter >= 18:
    print("Du bist volljährig!")

antwort = input("Magst Du Python? (J/N) ")
if antwort == "J":
    print("Das ist toll!") 
elif antwort == "N":
    print("Schade!") 
else:
    print("Bitte antworte mit J oder N!")

note = input("Welche Note hast Du? ")
match note:
    case "1":  
        print("sehr gut")
    case "2": 
        print("gut")
    case "3":
        print("befriedigend")
    case "4":
        print("ausreichend")
    case "5":
        print("mangelhaft")     
    case "6":
        print("ungenügend")
    case _:
        print("ungültige Note")


# Die for-Schleife -> ausgelagert in eigene Datei (For_Schleife.py)
