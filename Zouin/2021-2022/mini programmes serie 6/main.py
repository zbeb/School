# EX 1
# a = 7
# b = 10
# x = 0
#
# print(a, b)
# x = a
# a = b
# b = x
# print(a, b)

# EX 2
# numbers = []
#
# for x in range(3):
#     x = int(input("Entrez un nombre: "))
#     numbers.append(x)
# numbers.sort()
# print(*numbers)

# EX 3
# reponse = input("Internet ou cash: ")
#
# if reponse == "internet":
#     print("Cela vous coute 26 euros")
# else:
#     print("Cela vous coute 32 euros")

# EX 4
# reponse = input("Quelle mode d'operation voulez vous (addition ou multiplication): ")
# nbr1 = int(input("Entrez un nombre: "))
# nbr2 = int(input("Entrez un nombre: "))
#
# if (reponse == "addition"):
#     print(nbr1 + nbr2)
# if (reponse == "multiplication"):
#     print(nbr1 * nbr2)

# EX 5
# cout = 0.23
# nbrCigarette = int(input("Combien de cigarette fume tu par jour: "))
# depenseMens = round((nbrCigarette * cout) * 30, 2)
# depenseAnn = round((nbrCigarette * cout) * 365, 2)
#
# if depenseAnn >= 499:
#     print("si tu ne fumais pas, tu pourrais te payer une tablette ACER A500 32GB WIFI à 499 €")
# elif depenseAnn >= 199:
#     print("si tu ne fumais pas, tu pourrais te payer une mini-tablette de 8 poucesMPMAN à 199 €")

# EX 6
# record = 265
# yourRecord = int(input("Quelle est votre temps: "))
#
# if yourRecord > record:
#     print("Vous etes le nouveau champion")
#     print(f"Votre record est {yourRecord}sec ou {int(yourRecord / 60)}min")
# if yourRecord < record:
#     print("tu dois continuer ton entrainement.")

# EX 7
# import datetime
#
# Dep = input("Quelle est votre temps de depard: ")
# Arr = input("Quelle est votre temps de arrivee: ")
#
# tempsDep = datetime.datetime.strptime(Dep, "%H:%M")
# tempsArr = datetime.datetime.strptime(Arr, "%H:%M")
# dureeVol = tempsArr - tempsDep
#
# print(f"Temps depart: {tempsDep.hour}:{tempsDep.minute}")
# print(f"Temps arrive: {tempsArr.hour}:{tempsArr.minute}")
# print(f"Duree du vol: {dureeVol}")

# EX 8
# def note():
#     n = int(input("Quelle est votre note: "))
#
#     if n >= 16:
#         print("TB")
#         return
#     if n >= 14:
#         print("B")
#         return
#     if n >= 12:
#         print("AB")
#         return
#     if n >= 10:
#         print("Passable")
#         return
#     if n < 10:
#         print("Mauvais")
#         return
# note()