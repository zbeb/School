userInput = int(input("Inserez un nombre non null: "))

somme = 0
for x in range (1, userInput + 1):
    somme += x ** 5
print(somme)