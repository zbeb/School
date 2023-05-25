import os

currentDir = os.path.dirname(os.path.abspath(__file__))
print(currentDir)
filePath = os.path.join(currentDir, "file.txt")

with open(filePath, "w") as file:
    file.write("Nathan\nSteve\nDavid\nSam")

with open(filePath, "r") as file:
    lines = file.readlines()
    lines.sort(key=len)
    print(f"Nom plus \033[1mcourt\033[0m: \033[1m\033[4m{lines[0]}\033[0m\nNom plus \033[1mlong\033[0m: \033[1m\033[4m{lines[-1]}\033[0m")