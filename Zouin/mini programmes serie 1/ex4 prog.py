# Ex 4 et 5

"""
Bio1 = float(input("Ecris tes notes d'interro de Bio: "))
Bio1 += float(input("Ecris tes notes d'interro de Bio: "))
Bio1 += float(input("Ecris tes notes d'interro de Bio: "))
Geo1 = float(input("Ecris tes notes d'interro de Geo: "))
Geo1 += float(input("Ecris tes notes d'interro de Geo: "))
fr1 = float(input("Ecris tes notes d'interro de Fr: "))

sommeInterro = Bio1 + Geo1 + fr1
moyenneInterro = sommeInterro / 6
print(f"La moyenne est {moyenneInterro}")

if (moyenneInterro >= 10):
    print("Admis")
else:
    print("Ajourne")
"""

# Ex 4 et 5 v2 (Une autre maniere de faire l'ex)
"""
ieListCount = 0
notesIe = []
matieres = ["Bio", "Geo", "Fr"]
nbrIeCount = 0
count = 0
while count != 3:
    nbrIe = int(input(f"Combien d'interros de {matieres[count]} a tu fait? "))
    nbrIeCount += nbrIe
    for x in range(nbrIe):
        ordreDesIe = ["1ere", "2eme", "3eme"]
        userInput = float(input(f"Quelle etait ta note sur la {ordreDesIe[x]} IE: "))
        notesIe.append(userInput)
        x + 1
    count += 1
    ieListCount + 1

moyenneInterro = sum(notesIe) / nbrIeCount
print(f"La moyenne est de {moyenneInterro}")

if (moyenneInterro >= 10):
    print("Admis, SHEEEEEEEEEEESH")
else:
    print("Ajourne, CRIIING")
"""