class Employe:
    """classe de base pour les employes"""

    def __init__(self, nom_de_l_employe, age_de_l_employe):
        self.nom_de_l_employe = nom_de_l_employe
        self.age_de_l_employe = age_de_l_employe

    def change_name(self, new_name):
        self.nom_de_l_employe = new_name

    def change_age(self, new_age):
        self.age_de_l_employe = new_age


class Society:
    """classe de base pour les societes"""

    def __init__(self):
        self.employes = []
        self.nom_de_la_societe = "Fsociety"
        self.date_de_creation = "31/10/2014"

    def add(self, nom_de_l_employe, age_de_l_employe):
        self.employes.append(Employe(nom_de_l_employe, age_de_l_employe))

    def __repr__(self):
        return str(self.employes)


if __name__ == "__main__":
    # creation de la societe
    carrefour = Society()
    # ajout d'employes
    carrefour.add("Mr. Robot", 26)
    carrefour.add("Darlene", 29)
    carrefour.add("Leslie Romero", 27)
    carrefour.add("Mobley", 23)
    carrefour.add("Trenton", 31)
    # modification d'un employe
    carrefour.employes[2].change_name("Lardon")
    carrefour.employes[2].change_age(32)

    # affichage des informations de la societe
    print(f"La societe {carrefour.nom_de_la_societe} a ete cree le {carrefour.date_de_creation} et compte {len(carrefour.employes)} employes.\n")
    print("Liste des employes:")

    for employe in carrefour.employes:
        # affichage les employes avec un formatage
        print(f"Nom: {employe.nom_de_l_employe :<10} Age: {employe.age_de_l_employe}")
