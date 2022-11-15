from tabulate import tabulate

rowNames = ["Nom", "Pointure (EU)", "Prix (€)"]
colNames = [1, 2, 3, 4, 5, 6, 0]

stock = [["Asics Gel 2000", 42, 119],
         ["Asics Gel 2000", 39, 119],
         ["Mizuno Wave Rider", 38, 129],
         ["Nike Air Zoom", 42, 125],
         ["Mizuno Wave Plus", 39, 83.40],
         ["Mizuno Wave Plus", 40, 83.40],
         ["Mizuno Wave Plus", 41, 83.40],
         ["Merrell Poseidon", 39, 118.30]]

menuOptions = [["Afficher les articles pour une pointure"],
               ["Afficher les articles présents plusieurs fois"],
               ["Afficher les articles pour chaque pointure"],
               ["Afficher la pointure la plus présente"],
               ["Afficher le nombre de fois la pointure la plus présente"],
               ["Afficher l’article le plus cher"],
               ["Quitter le programme"]]


def show_catalogue():
    print("Voici le catalogue:")
    print(f"{tabulate(stock, headers=rowNames, numalign='center', tablefmt='rounded_grid')}\n\n")


def show_options():
    print("Voici les commandes disponibles")
    print(f"{tabulate(menuOptions, tablefmt='rounded_grid', showindex=colNames)}\n\n")


def search_by_size():
    sizes = []
    found = False
    size = int(input("Quelle taille voulez vous: "))

    for i in stock:
        if size in i:
            found = True
            sizes.append([i[0]])
    print(f"{tabulate(sizes, headers=rowNames, tablefmt='rounded_grid')}")
    if not found:
        print("Cette taille n'est pas dans notre base de donnees")


def multiple_articles():
    shoe_sizes = {}
    final = []
    headers = ["Model", "Pointure"]

    for name, *size in stock:  # Unpack the 'stock' list, place first value in name and every other value in size hence the '*'
        if name in shoe_sizes:  # Checks if the shoe's name is already in the dictionary
            shoe_sizes[name].append(size[0])  # Append the shoe size to the already existing key in the dictionary
        else:
            shoe_sizes[name] = [size[0]]  # If the key doesn't exist add it and asign the size

    for shoe, sizes in shoe_sizes.items():  # Unpack the dictionary containing the shoe name and all sizes available for it
        if len(sizes) > 1:  # Checks if a key has multiple values eg. "Asics Gel 2000", [42, 39]
            final.append([shoe, sizes])  # Append the name and the sizes to a final list
    print(f"{tabulate(final, headers, tablefmt='rounded_grid')}")


def size_by_article():
    show_catalogue()


def most_frequent_size():
    sizes = []
    for i in stock:
        sizes.append(i[1])
    print(f"La pointure la plus présente est: {max(sizes, key=sizes.count)}")


def number_of_most_frequent_size():
    sizes = []
    for i in stock:
        sizes.append(i[1])
    nbrOfMostFrequentSize = max(sizes, key=sizes.count)
    print(f"La pointure la plus présente apparait {sizes.count(nbrOfMostFrequentSize)} fois")


def most_expensive_item():
    prices = []
    for i in stock:
        prices.append(i)
    prices.sort()
    prices = [prices[-1]]
    print(tabulate(prices, headers=rowNames, tablefmt='rounded_grid'))


def func_quit():
    exit()


show_catalogue(), show_options()
options = {
    "1": search_by_size,
    "2": multiple_articles,
    "3": size_by_article,
    "4": most_frequent_size,
    "5": number_of_most_frequent_size,
    "6": most_expensive_item,
    "0": func_quit
}
userInput = input("Quelle commande voulez vous: ")
options[userInput]()
