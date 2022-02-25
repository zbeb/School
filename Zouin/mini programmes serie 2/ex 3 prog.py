prixI1 = float(input("Quelle est le prix du 1er item: "))
prixI2 = float(input("Quelle est le prix du 2eme item: "))
tva = 79
horsTax = 1
prixTotal = prixI1 + prixI2
print(((horsTax * prixI1) + (horsTax * prixI2)) * (tva/100))