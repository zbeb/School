with open ("test.txt", "w") as file:
    file.write("YAa\naaaaaS\nTigre\nB\nMoutons")

# ouvre le fichier ainsi cree en mode lecture
# affiche le nom le polus court dans le fichier
# affiche le nom le plus long dans le fichier

with open ("test.txt", "r") as file:
    lines = file.readlines()
    lines.sort(key=len)
    print("Le mot le plus court est:", lines[0])
    print("Le mot le plus long est:", lines[-1])