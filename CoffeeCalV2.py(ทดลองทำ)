import os

space, high = os.get_terminal_size()
space -= 2

# ฟังชันกรอบ+ตัวหนังสือ


def page(strings, symbol="|"):
    s = len(strings) / 2
    if (int(s) != s):
        s1, s2 = s - 1, s
    else:
        s1, s2 = s, s
    print(symbol + (" " * int(space / 2 - s1)) + strings +
          (" " * int(space / 2 - s2)) + symbol)

# ฟังชันขอบกรอบ


def line(symbol):
    L = str(symbol) * (int(space) + 2)
    print(L)

# ฟังชันกรอบ


def frame(symbol):
    F = (str(symbol) + " " * (space) + str(symbol))
    print(F)
    # ใช้ for i in range(x): - เพื่อทำหลายแถว


water = 400
milk = 540
coffeebean = 120
cup = 9
money = 550

# Buy function


def buy(W, M, B, C, price, kind):
    line("=")
    frame("|")
    frame("|")
    page("Buy : " + str(kind) + " / Price : " + str(price) + " Bath")
    for i in range(4):
        frame("|")
    page("*In Coffee_Selling_Machine")
    frame("|")
    page("Water : " + str(int(water) - W) + " Lits")
    frame("|")
    page("Milk : " + str(int(milk) - M) + " Lits")
    frame("|")
    page("CoffeeBean : " + str(int(coffeebean) - B) + " g")
    frame("|")
    page("Cup : " + str(int(cup) - C) + " Cups")
    frame("|")
    page("Money : " + str(int(money) + int(price)) + " BATH")
    for i in range(3):
        frame("|")
    line("=")
# kind = coffee kinds / price = coffee price / W = used water / M = used
# milk / B = used coffeebean / C = used cup = 1


# Fill function
def fill(W, M, B, C):
    line("=")
    frame("|")
    frame("|")
    page("*In Coffee_Selling_Machine")
    for i in range(6):
        frame("|")
    page("Water : " + str(int(water) + int(W)) + " Lits")
    frame("|")
    page("Milk : " + str(int(milk) + int(M)) + " Lits")
    frame("|")
    page("CoffeeBean : " + str(int(coffeebean) + int(B)) + " g")
    frame("|")
    page("Cup : " + str(int(cup) + int(C)) + " Cups")
    frame("|")
    page("Money : " + str(int(money)) + " BATH")
    for i in range(3):
        frame("|")
    line("=")

# Take Function


def take(TakeMoney):
    line("=")
    frame("|")
    frame("|")
    page("you take money : " + str(TakeMoney) + " BATH")
    for i in range(4):
        frame("|")
    page("*In Coffee_Selling_Machine")
    frame("|")
    page("Water : " + str(int(water)) + " Lits")
    frame("|")
    page("Milk : " + str(int(milk)) + " Lits")
    frame("|")
    page("CoffeeBean : " + str(int(coffeebean)) + " g")
    frame("|")
    page("Cup : " + str(int(cup)) + " Cups")
    frame("|")
    page("Money : " + str(int(money) - int(TakeMoney)) + " BATH")
    for i in range(3):
        frame("|")
    line("=")


# While loop - start
y = 1
while True:
    if y == 1:

        # first window
        line("=")
        for i in range(8):
            frame("|")
        page("WELCOME TO Coffee Selling Machine")
        for i in range(2):
            frame("|")
        page("Press 'Enter' To Continue")
        for i in range(9):
            frame("|")
        line("=")

        Enter = input("*Press Enter >>>>>> To Continue")

# หน้าจอโชว์

        line("=")
        for i in range(5):
            frame("|")
        page("*In Coffee_Selling_Machine")
        for i in range(2):
            frame("|")
        frame("|")
        page("Water : " + str(int(water)) + " Lits")
        frame("|")
        page("Milk : " + str(int(milk)) + " Lits")
        frame("|")
        page("CoffeeBean : " + str(int(coffeebean)) + " g")
        frame("|")
        page("Cup : " + str(int(cup)) + " Cups")
        frame("|")
        page("Money : " + str(int(money)) + " BATH")
        for i in range(3):
            frame("|")
        line("=")

        Enter = input("*Press Enter >>>>>> To Continue")

# menu

        line("=")
        for i in range(6):
            frame("|")
        page("'Choose Menu'")
        for i in range(2):
            frame("|")
        page("(1) Buy")
        frame("|")
        page("(2) Fill")
        frame("|")
        page("(3) Take")
        for i in range(7):
            frame("|")
        line("=")

        com = str(input("Choose Command : >"))

# if

        if "1" in com or "Buy" in com or "buy" in com or "BUY" in com:
            line("=")
            for i in range(6):
                frame("|")
            page("'Choose kind of coffee'")
            for i in range(2):
                frame("|")
            page("(1) espresso")
            frame("|")
            page("(2) latte")
            frame("|")
            page("(3) cappuccino")
            for i in range(7):
                frame("|")
            line("=")

            kind = str(input("Choose coffee kind : >"))

            if "1" in kind or "espresso" in kind:
                buy(250, 0, 16, 1, 4, "espresso")
            elif "2" in kind or "latte" in kind:
                buy(350, 75, 20, 1, 7, "latte")
            elif "3" in kind or "cappuccino" in kind:
                buy(200, 100, 12, 1, 6, "cappuchino")
            else:
                print("Error")

            Enter = input("*Press Enter >>>>>> To Continue")

        elif "2" in com or "Fill" in com or "fill" in com or "FILL" in com:
            line("=")
            for i in range(10):
                frame("|")
            page("*Fill - Input Ingredian")
            for i in range(10):
                frame("|")
            line("=")
            W = int(input("Fill Water (ml) : > "))
            M = int(input("Fill Milk (ml) : > "))
            B = int(input("Fill CoffeeBean (g) : > "))
            C = int(input("Fill Cups (cup) : > "))

            fill(W, M, B, C)

            Enter = input("*Press Enter >>>>>> To Continue")

        elif "3" in com or "Take" in com or "take" in com or "TAKE" in com:
            line("=")
            for i in range(10):
                frame("|")
            page("*Take - Input money do you want")
            for i in range(10):
                frame("|")
            line("=")

            want = int(input("I want to take (BATH) : > "))

            take(want)

            Enter = input("*Press Enter >>>>>> To Continue")

        else:
            print("Error")
            Enter = input("*Press Enter >>>>>> To Continue")

# Exit menu

        line("=")
        for i in range(8):
            frame("|")
        page("Exit Or Restart")
        for i in range(2):
            frame("|")
        page("(1) Exit / (2) Restart")
        for i in range(9):
            frame("|")
        line("=")

        end = input("Choose Command : > ")

        if "1" in end or "Exit" in end or "exit" in end or "EXIT" in end:
            y = 0
        elif "2" in end or "Restart" in end or "restart" in end or "RESTART" in end:
            y = 1

    elif y != 1:
        break
