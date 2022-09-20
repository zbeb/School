import random

gain = 1000000


def loterie():
    global gain
    ticketUtil = []
    ticketGag = []
    while True:
        try:
            nbrMax = 0
            # 1) Demander l’intervalle de nombre de chiffres à cocher et le nombre de chiffres à choisir.
            nbrChiffres = int(input("Entrez le nombre de chiffre que vous voulez: "))
            while nbrMax < 1 or nbrMax > 50:
                nbrMax = int(input("Entrez la valeur maximum des chiffres a chocher (1-50): "))
        except ValueError:
            print("Ceci n'est pas un nombre")
        else:
            break

    pasJouer = input("Appuyer sur Enter pour jouer ou taper 'exit' pour quitter: ").lower() == "exit"
    if pasJouer:
        exit()

    while len(ticketUtil) < nbrChiffres:
        ticketUtil.append(random.randint(1, nbrMax))
        ticketGag.append(random.randint(1, nbrMax))
    # 2) Appel fonction Tirage_ticket() pour le ticket_joueur et le ticket_gagnant.
    print(f"Votre ticket:\n{ticketUtil}\nTicket gagnant:\n{ticketGag}")
    if gagnat(ticketUtil, ticketGag):
        # 3) Affichage des messages (Gain ou défaite).
        print(f"Vous avez remporte le grand prix de {'{:,}'.format(gain)} euros")
    else:
        print(f"Vous n'avez pas remporte le grand prix de {'{:,}'.format(gain)} euros. Vous aurez plus de change la prochaine fois")
        gain *= 2

    rejouer()


def rejouer():
    # Repter les fonctions
    print("---------------------------------")
    print("\nNouveau ticket\n")
    loterie()


def gagnat(ticketUtilisateur: list, ticketGagnant: list):
    # Fonction qui va comparer les deux tickets et retourner un booléens si l’utilisateur gagne ou non.
    if ticketUtilisateur == ticketGagnant:
        return True

    return False


def calcul_probabilite():
    pass


if __name__ == "__main__":
    loterie()
