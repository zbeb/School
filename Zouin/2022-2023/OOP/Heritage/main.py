class Animal:
    """animal class with name attribute"""

    def __init__(self, nom):
        self.nom = nom


class Chien(Animal):
    """dog class with bark method"""

    def aboyer(self):
        print(f"{self.nom} aboie")


class Chat(Animal):
    """cat class with meow method"""

    def miauler(self):
        print(f"{self.nom} miaule")


def main():
    chien = Chien("Rex")  # create a dog and give it a name
    print(f"Chien cree **{chien.nom}**")  # print the dog's name
    chien.aboyer()

    chat = Chat("Felix")  # create a cat and give it a name
    print(f"Chat cree **{chat.nom}**")  # print the cat's name
    chat.miauler()


if __name__ == "__main__":
    main()
