def menu(water,milk,beans,cup,money):
    print("\n\n")
    print("The Coffee machine has :")
    print(str(water)+" of water")
    print(str(milk)+" of milk")
    print(str(beans)+" of coffee beans")
    print(str(cup)+" of disposable cups")
    print(str(money)+" of money")
    print("")

def fill(water,water_add,milk,milk_add,beans,beans_add,cup,cup_add):
    water = int(water) + int(water_add)
    milk = int(milk) + int(milk_add)
    beans = int(beans) + int(beans_add)
    cup = int(cup) + int(cup_add)
    return (water,milk,beans,cup)

def take(money):
    print("")
    print("I gave you "+str(money))
    print("")


def buy(water,water_used,milk,milk_used,beans,beans_used,cup,cup_used,money,money_take):
    water = int(water) - int(water_used)
    milk = int(milk) - int(milk_used)
    beans = int(beans) - int(beans_used)
    cup = int(cup) - int(cup_used)
    money = int(money) + int(money_take)
    return (water,milk,beans,cup,money)

y = 1

water = 400
milk = 540
beans = 120
cup = 9
money = 550

while y == 1:

    command = str(input("\nwrite action (buy, fill, take, remaining, exit):\n>"))

    if "buy" in command:
        kind_of_coffee = str(input("What do you want to buy ? 1 - espresso , 2 - latte , 3 - capppuccino :\n> "))
        if "1" in kind_of_coffee:
            if water >= 250 and milk >= 0 and beans >= 16 and cup >= 1:
                print("")
                print("I have enough resources, making you a coffee!")
                print("")
                x = (buy(water,250,milk,0,beans,16,cup,1,money,4))
                water = (x[0])
                milk = (x[1])
                beans = (x[2])
                cup = (x[3])
                money = (x[4])
            else:
                print("")
                print("Don't have enough resources, can't making a coffee!")
                print("")

        elif "2" in kind_of_coffee:
            if water >= 350 and milk >= 75 and beans >= 20 and cup >= 1:
                print("")
                print("I have enough resources, making you a coffee!")
                print("")
                x = (buy(water,350,milk,75,beans,20,cup,1,money,7))
                water = (x[0])
                milk = (x[1])
                beans = (x[2])
                cup = (x[3])
                money = (x[4])

            else:
                print("")
                print("Don't have enough resources, can't making a coffee!")
                print("")

        elif "3" in kind_of_coffee:
            if water >= 200 and milk >= 100 and beans >= 12 and cup >= 1:
                print("")
                print("I have enough resources, making you a coffee!")
                print("")
                x = (buy(water,200,milk,100,beans,12,cup,1,money,6))
                water = (x[0])
                milk = (x[1])
                beans = (x[2])
                cup = (x[3])
                money = (x[4])
            else:
                print("")
                print("Don't have enough resources, can't making a coffee!")
                print("")

    elif "fill" in command:
        water_add = int(input("Write how many ml of water do you want add\n> "))
        milk_add = int(input("Write how many ml of milk do you want add\n> "))
        beans_add = int(input("Write how many grams of coffee beans do you want add\n> "))
        cup_add = int(input("Write how many disposable cups of coffee do you want add\n> "))
        x = fill(water, water_add, milk, milk_add, beans, beans_add, cup, cup_add)
        water = (x[0])
        milk = (x[1])
        beans = (x[2])
        cup = (x[3])
        money = (money)

    elif "take" in command:
        take(money)
        money = int(0)

    elif "remaining" in command:
        menu(water,milk,beans,cup,money)

    elif "exit" in command:
        y = 0