import random

# Var declaration
playerScore = 0
computerScore = 0

gameOn = True

while gameOn:
    # Input handler
    playerInput = int(input("Combien de des souhaitez-vous lancer ? "))
    if playerInput == 0:
        if playerScore > computerScore:
            print(f"Vous avez gagne ({playerScore}) contre l'ordianteur ({computerScore})")
            gameOn = False
            break
        else:
            print(f"Vous avez perdu ({playerScore}) contre l'ordianteur ({computerScore})")
            gameOn = False
            break

    computerInput = random.randint(1, 6)

    if computerScore < 6:
        computerInput = 3
    elif 6 >= computerScore < 12:
        computerInput = 2

    # Score handler
    for x in range(playerInput):
        playerScore += random.randint(1, 6)
    # Prints player's score
    print(f"Vous avez un score de {playerScore}\n")

    for x in range(computerInput):
        if 12 <= computerScore < 18:
            break
        computerScore += random.randint(1, 6)
    # Prints the computers input and score
    print(f"L'ordinateur choisi {computerInput} des\nL'ordinatuer a un score de {computerScore}\n")

    # Checks if someone one
    if playerScore > 21 or computerScore == 21:
        print(f"Vous avez perdu ({playerScore}) contre l'ordianteur ({computerScore})")
        gameOn = False
        break

    if computerScore > 21 or playerScore == 21:
        print(f"Vous avez gagne ({playerScore}) contre l'ordianteur ({computerScore})")
        gameOn = False
        break

    if playerScore == computerScore:
        print(f"Vous avez fait un match nul ({playerScore}) contre l'ordianteur ({computerScore})")
        gameOn = False
        break
