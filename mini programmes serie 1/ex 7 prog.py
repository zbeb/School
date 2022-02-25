CA = float(input("Quelle est votre chiffre d'affaire: "))

if (CA > 100000):
    commission = 0.15
elif (CA > 30000 and CA <= 100000):
    commission = 0.1
else:
    commission = 1