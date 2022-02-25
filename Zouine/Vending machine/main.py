items = [["eau", 0.90], ["chocolat", 1.50], ["enfant", 69], ["doritos", 2.30]]
i = 0

print("Hello welcome to the vending machine, here is our menu \n") #Welcome message

print("Menu: ")
for item in items:
    i += 1
    print(f"{i}. {item[0]} ${item[1]}")

def Taking_Order():

    def Order_Proccess():
        itemOrdered = items[order - 1][0]
        orderPrice = items[order - 1][1]
        print(f"You ordered {itemOrdered}, that will be ${orderPrice}")

        money = float(input("Please insert your money: "))
        print(f"You inserted ${money}")

        if money >= orderPrice:
            print(f"You have received {itemOrdered} \nMoney to return ${round(money - orderPrice, 2)}")
        else:
            print(f"Insufficient funds \nReturned ${money}")
            answer = input("Would you like to try again? y/n\n")
            if answer == "y":
                Taking_Order()
            else:
                exit()

    order = int(input("\nEnter the number of the item you would like to order: \n"))
    if order in range(1, 5):
        Order_Proccess()
    else:
        print("Please select a valid item")
        Taking_Order()

Taking_Order()

input("\n\nPress any key to exit...")