
from zeep import Client
from lxml import etree
import os

y = 1
while True:
    if y == 1:

        client = Client('http://www.pttor.com/OilPrice.asmx?WSDL')

        result = client.service.CurrentOilPrice("en")

        root = etree.fromstring(result)

        GasProduct = []
        GasPrice = []

        space, high = os.get_terminal_size()
        space -= 2

        def page(strings, symbol="#"):
            s = len(strings) / 2
            if (int(s) != s):
                s1, s2 = s - 1, s
            else:
                s1, s2 = s, s
            print(symbol + (" " * int(space / 2 - s1)) + strings +
                  (" " * int(space / 2 - s2)) + symbol)
        print("#" * (space + 2))
        print("#" + " " * (space) + "#")
        page("*Oil Price")
        for i in range(2):
            print("#" + " " * (space) + "#")

        number = 1

        for r in root.xpath('FUEL'):
            product = r.xpath('PRODUCT/text()')[0]
            price = r.xpath('PRICE/text()') or [0]

            GasProduct.append(product)
            GasPrice.append(float(price[0]))

            page(str(number) + ". " + product + " %2.f" %
                 (float(price[0])) + ' BAHT')

            number += 1

        print("#" + " " * (space) + "#")
        page("Choose kinds of oil(list's ordinal)")
        print("#" + " " * (space) + "#")
        print("#" * (space + 2))

        kind = int(input("Oli kinds: > "))

        n = (kind - 1)

        print("#" * (space + 2))
        print("#" + " " * (space) + "#")
        print("#" + " " * (space) + "#")
        page("*Choose Command")
        for i in range(9):
            print("#" + " " * (space) + "#")
        page("(1) Lit_to_Bath or (2)Bath_to_lit")
        for i in range(8):
            print("#" + " " * (space) + "#")
        print("#" * (space + 2))

        c = str(input("Choose command: > "))

        if "1" in c or "Lit_to_Bath" in c or "LitToBath" in c or "lit_to_bath" in c:
            print("#" * (space + 2))
            for i in range(10):
                print("#" + " " * (space) + "#")
            page("Input Lits")
            for i in range(10):
                print("#" + " " * (space) + "#")
            print("#" * (space + 2))
            lits = float(input("Lits input: > "))

            print("#" * (space + 2))
            for i in range(8):
                print("#" + " " * (space) + "#")
            page("**Result - Lit_To_Bath")
            print("#" + " " * (space) + "#")
            page("Money: " +
                 str(GasProduct[n]) +
                 ":" +
                 " %2.f" %
                 ((GasPrice[n]) *
                  lits) +
                 " Bath")
            for i in range(8):
                print("#" + " " * (space) + "#")
            print("#" * (space + 2))

        elif "2" in c or "Bath_to_Lit" in c or "BathToLit" in c or "Bath_to_Lit" in c:
            print("#" * (space + 2))
            for i in range(10):
                print("#" + " " * (space) + "#")
            page("Input Money(Bath)")
            for i in range(10):
                print("#" + " " * (space) + "#")
            print("#" * (space + 2))
            money = float(input("Money input(Bath): > "))

            print("#" * (space + 2))
            for i in range(8):
                print("#" + " " * (space) + "#")
            page("**Result - Bath_To_Lits")
            print("#" + " " * (space) + "#")
            page("Lits: " +
                 str(GasProduct[n]) +
                 ":" +
                 " %2.f" %
                 (money /
                  (GasPrice[n])) +
                 " Lits")
            for i in range(8):
                print("#" + " " * (space) + "#")
            print("#" * (space + 2))
        else:
            print("Error")

        end = input("(1) Exit / (2) Restart : > ")

        if "Exit" in end or "1" in end or "exit" in end:
            y = 0
        elif "Restart" in end or "2" in end or "restart" in end:
            y = 1
        else:
            print("Error")

    elif y != 1:
        break
