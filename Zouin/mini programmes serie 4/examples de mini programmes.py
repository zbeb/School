x = [1, 2, 3]
print(*x)

print("-----------------")

print(*x, sep= "\n")

print("-----------------")

name = input("Quelle est votre nom? ")
print(name)

print("-----------------")

for i in range(1):
    print(*x)

for i in x:
    print(i)

print("-----------------")

for i in range(3): #Je nai pas tres bien compris ce que vous voulez faire alors jai fais comme jai compris
    print("Hello world")
    #print("End") Je ne sais pas si vous parlez de cette sortie ou la sortie complete alors jai mis les 2
print("End")

print("-----------------")

num = int(input("Inserez un nombre: "))

if num > 0:
    print("Le chiffre est positive")
if num < 0:
    print("Le chiffre est negative")
if num == 0:
    print("Le chiffre vaut 0")

print("-----------------")

z = 0
while z != 10:
    print("boucle Tant que")
    z += 1
print("") #Pour mettre une espace entre les 2 programmes
for i in range(10):
    print("boucle for")

print("-----------------")

tab = [5, 4, 2, 0]
print(tab[1])
print(tab[2])
print(tab)