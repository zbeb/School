class GrandPere:
    """Classe définissant le grand-père"""
    def __init__(self, nom, somme):
        self.nom = nom
        self.somme = somme


class Ryad(GrandPere):
    """Classe définissant le petit-fils Ryad"""
    def __init__(self, nom, somme):
        super().__init__(nom, somme * 0.75)  # Appel de constructeur de la superclasse


class Sefa(GrandPere):
    """Classe définissant le petit-fils Sefa"""
    def __init__(self, nom, somme):
        super().__init__(nom, somme * 0.25)  # Appel de constructeur de la superclasse


def main():
    grandPere = GrandPere("Simou", 50000)
    ryad = Ryad("Ryad", grandPere.somme)
    sefa = Sefa("Sefa", grandPere.somme)
    print(f"{grandPere.nom} a laissé {grandPere.somme}€ à ses petits-enfants")
    print(f"{ryad.nom} hérite de {ryad.somme}€")
    print(f"{sefa.nom} hérite de {sefa.somme}€")


if __name__ == "__main__":
    main()
