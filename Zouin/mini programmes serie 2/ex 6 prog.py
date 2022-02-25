names = []
x = 0
for i in range(3):
    x += 1
    names.append(input(f"Quelle est le {x} nom: "))
unsortedList = names[:]
sortedNames = sorted(names)

if unsortedList == sortedNames:
    print("les nombres sont en ordre")
else:
    print("les nombres sont pas en ordre")
