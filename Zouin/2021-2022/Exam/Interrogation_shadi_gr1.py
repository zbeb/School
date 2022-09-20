# def calcMin():
#     value = []
#
#     for i in range(5):
#         value.append(int(input("Entrez un nombre: ")))
#
#     maxValue = value[0]
#     for x in range(len(value)):
#         if value[x] > maxValue:
#             maxValue = value[x]
#     print(maxValue)

def calcAvg():
    value2 = []
    total = 0

    for i in range(5):
        value2.append(int(input("Entrez un nombre: ")))

    for x in range(len(value2)):
        total += value2[x]
    print(total / len(value2))


# calcMin()
calcAvg()