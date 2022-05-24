stock = [["Asics Gel 2000", 42, 119],
        ["Asics Gel 2000", 39, 119],
        ["Mizuno Wave rider", 38, 129],
        ["Nike Air Zoom", 42, 125],
        ["Mizuno Wave plus", 39, 83.40],
        ["Mizuno Wave plus", 40, 83.40],
        ["Mizuno Wave plus", 41, 83.40],
        ["Merrell Poseidon", 39, 118.30]]

for item in stock:
    print(f"{item[0]} | {item[1]} | {item[2]}")

print(f"\n 1 : Afficher les articles pour une pointure\n",
        "2 : Afficher les articles présents plusieurs fois\n",
        "3 : Afficher les articles pour chaque pointure\n",
        "4 : Afficher la pointure la plus présente\n",
        "5 : Afficher le nombre de fois la pointure la plus présente\n",
        "6 : Afficher l’article le plus cher\n",
        "0 : Quitter le programme\n")

def sizeSearch():
    found = False
    size = int(input("Quelle taille voulez vous: "))
    print() # Adds space between input and print

    for i in stock:
        if size in i:
            found = True
            print(f"{i[0]} | {i[1]} | ${i[2]}")
    if not found:
        print("Cette taille n'est pas dans notre base de donnees")

options = {
    1: sizeSearch
}

response = int(input("Quelle commande voulez vous: "))
options[response]()