from tabulate import tabulate


class Stock:
    def __init__(self):
        self.rowNames = ["Nom", "Pointure (EU)", "Prix (€)"]
        self.colNames = [1, 2, 3, 4, 5, 6, 0]

        self.stock = [["Asics Gel 2000", 42, 119],
                      ["Asics Gel 2000", 39, 119],
                      ["Mizuno Wave Rider", 38, 129],
                      ["Nike Air Zoom", 42, 125],
                      ["Mizuno Wave Plus", 39, 83.40],
                      ["Mizuno Wave Plus", 40, 83.40],
                      ["Mizuno Wave Plus", 41, 83.40],
                      ["Merrell Poseidon", 39, 118.30]]

        self.menuOptions = [["Afficher les articles pour une pointure"],
                            ["Afficher les articles présents plusieurs fois"],
                            ["Afficher les articles pour chaque pointure"],
                            ["Afficher la pointure la plus présente"],
                            ["Afficher le nombre de fois la pointure la plus présente"],
                            ["Afficher l’article le plus cher"],
                            ["Quitter le programme"]]
        self.options = {
            "1": self.search_by_size,
            "2": self.multiple_articles,
            "3": self.size_by_article,
            "4": self.most_frequent_size,
            "5": self.number_of_most_frequent_size,
            "6": self.most_expensive_item,
            "0": self.func_quit
    }

    def show_catalogue(self):
        print("Voici le catalogue:")
        print(f"{tabulate(self.stock, headers=self.rowNames, numalign='center', tablefmt='rounded_grid')}\n\n")

    def show_options(self):
        print("Voici les commandes disponibles")
        print(f"{tabulate(self.menuOptions, tablefmt='rounded_grid', showindex=self.colNames)}\n\n")

    def search_by_size(self):
        sizes = []
        found = False
        size = int(input("Quelle taille voulez vous: "))

        for i in self.stock:
            if size in i:
                found = True
                sizes.append([i[0]])
        print(f"{tabulate(sizes, headers=self.rowNames, tablefmt='rounded_grid')}")
        if not found:
            print("Cette taille n'est pas dans notre base de donnees")

    def multiple_articles(self):
        shoe_sizes = {}
        final = []
        headers = ["Model", "Pointure"]

        for name, *size in self.stock:  # Unpack the 'stock' list, place first value in name and every other value in size hence the '*'
            if name in shoe_sizes:  # Checks if the shoe's name is already in the dictionary
                shoe_sizes[name].append(size[0])  # Append the shoe size to the already existing key in the dictionary
            else:
                shoe_sizes[name] = [size[0]]  # If the key doesn't exist add it and asign the size

        for shoe, sizes in shoe_sizes.items():  # Unpack the dictionary containing the shoe name and all sizes available for it
            if len(sizes) > 1:  # Checks if a key has multiple values eg. "Asics Gel 2000", [42, 39]
                final.append([shoe, sizes])  # Append the name and the sizes to a final list
        print(f"{tabulate(final, headers, tablefmt='rounded_grid')}")

    def size_by_article(self):
        self.show_catalogue()

    def most_frequent_size(self):
        sizes = []
        for i in self.stock:
            sizes.append(i[1])
        print(f"La pointure la plus présente est: {max(sizes, key=sizes.count)}")

    def number_of_most_frequent_size(self):
        sizes = []
        for i in self.stock:
            sizes.append(i[1])
        nbrOfMostFrequentSize = max(sizes, key=sizes.count)
        print(f"La pointure la plus présente apparait {sizes.count(nbrOfMostFrequentSize)} fois")

    def most_expensive_item(self):
        prices = []
        for i in self.stock:
            prices.append(i)
        prices.sort()
        prices = [prices[-1]]
        print(tabulate(prices, headers=self.rowNames, tablefmt='rounded_grid'))

    def func_quit(self):
        exit()


if __name__ == "__main__":
    stock = Stock()
    stock.show_catalogue()
    stock.show_options()
    userInput = input("Quelle commande voulez vous: ")
    stock.options[userInput]()