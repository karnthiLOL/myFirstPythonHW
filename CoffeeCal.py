#กำหนดค่า วัตถุดิบในเครื่องชงกาแฟ
W = 400
M = 540
B = 120
C = 9
m = 550

#วนลูปเมื่อเป็นไปตามเงื่อนไข Restart / Exit
y = 1
while True:
    if y == 1:

#โชว์รายละเอียดวัตถุดิบที่มีอยู่ในเครื่องชงกาแฟ
        print("################################################################################")
        print("#  **The Coffee machine has:                                                   #")
        print("#                                                                              #")
        print(
            "#   ",
            (W),
            "ml of water                                                           #")
        print("#                                                                              #")
        print("#                                                                              #")
        print("#                                                                              #")
        print(
            "#   ",
            (M),
            "ml of milk                                                            #")
        print("#                                                                              #")
        print("#                                                                              #")
        print("#                                                                              #")
        print(
            "#   ",
            (B),
            "g of coffee beans                                                     #")
        print("#                                                                              #")
        print("#                                                                              #")
        print("#                                                                              #")
        print(
            "#   ",
            (C),
            "of disposable cups                                                      #")
        print("#                                                                              #")
        print("#                                                                              #")
        print("#                                                                              #")
        print(
            "#   ",
            (m),
            "$ of money                                                            #")
        print("#                                                                              #")
        print("#                                                                              #")
        print("################################################################################")

        #เลือกเมนูการใช้งาน ซื้อ/ เติม / รับเงิน
        p = input("choose one option - buy / fill/ take >")

#ทำงานตามเงื่อนไขของBuy
        if "buy" in p or "Buy" in p or "BUY" in p:

#แสดงประเภทของกาแฟ
            print(
                "################################################################################")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#  **Choose Kind Of Coffee                                                     #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#  ( 1 ) Espresso                                                              #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#  ( 2 ) Latte                                                                 #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#  ( 3 ) Cappuccino                                                            #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "################################################################################")

#กรอกประเภทของกาแฟที่ต้องการ
            c = str(input("tell me what number do you want ? >"))

#เงื่อนไข Buy ตามประเภทของกาแฟ โดยแสดง ประเภท / เงินที่ต้องจ่าย และ วัตถุดิบที่เหลือ
            if 'espresso' in c or '1' in c:
                print(
                    "################################################################################")
                print(
                    "#                                                                              #")
                print(
                    "#  Espresso                                                                    #")
                print(
                    "#  *you must pay 4 $                                                           #")
                print(
                    "#                                                                              #")
                print(
                    "#  *The Coffee machine has:                                                    #")
                print(
                    "#                                                                              #")
                print(
                    "#                                                                              #")
                print(
                    "#  ",
                    (int(W) - 250),
                    "ml of water                                                            #")
                print(
                    "#                                                                              #")
                print(
                    "#                                                                              #")
                print(
                    "#  ",
                    (M),
                    "ml of milk                                                             #")
                print(
                    "#                                                                              #")
                print(
                    "#                                                                              #")
                print(
                    "#  ",
                    (int(B) - 16),
                    "g of coffee beans                                                      #")
                print(
                    "#                                                                              #")
                print(
                    "#                                                                              #")
                print(
                    "#  ",
                    (int(C) - 1),
                    "of disposable cups                                                       #")
                print(
                    "#                                                                              #")
                print(
                    "#                                                                              #")
                print(
                    "#  ",
                    (int(m) + 4),
                    "$ of money                                                             #")
                print(
                    "#                                                                              #")
                print(
                    "#                                                                              #")
                print(
                    "################################################################################")
            elif 'latte' in c or '2' in c:
                print(
                    "################################################################################")
                print(
                    "#                                                                              #")
                print(
                    "#  Latte                                                                       #")
                print(
                    "#  *you must pay 7 $                                                           #")
                print(
                    "#                                                                              #")
                print(
                    "#  *The Coffee machine has:                                                    #")
                print(
                    "#                                                                              #")
                print(
                    "#                                                                              #")
                print(
                    "#  ",
                    (int(W) - 350),
                    "ml of water                                                             #")
                print(
                    "#                                                                              #")
                print(
                    "#                                                                              #")
                print(
                    "#  ",
                    (int(M) - 75),
                    "ml of milk                                                             #")
                print(
                    "#                                                                              #")
                print(
                    "#                                                                              #")
                print(
                    "#  ",
                    (int(B) - 20),
                    "g of coffee beans                                                      #")
                print(
                    "#                                                                              #")
                print(
                    "#                                                                              #")
                print(
                    "#  ",
                    (int(C) - 1),
                    "of disposable cups                                                       #")
                print(
                    "#                                                                              #")
                print(
                    "#                                                                              #")
                print(
                    "#  ",
                    (int(m) + 7),
                    "$ of money                                                             #")
                print(
                    "#                                                                              #")
                print(
                    "#                                                                              #")
                print(
                    "################################################################################")
            elif 'cappuccino' in c or '3' in c:
                print(
                    "################################################################################")
                print(
                    "#                                                                              #")
                print(
                    "#  Cappuccino                                                                  #")
                print(
                    "#  *you must pay 6 $                                                           #")
                print(
                    "#                                                                              #")
                print(
                    "#  *The Coffee machine has:                                                    #")
                print(
                    "#                                                                              #")
                print(
                    "#                                                                              #")
                print(
                    "#  ",
                    (int(W) - 200),
                    "ml of water                                                            #")
                print(
                    "#                                                                              #")
                print(
                    "#                                                                              #")
                print(
                    "#  ",
                    (int(M) - 100),
                    "ml of milk                                                             #")
                print(
                    "#                                                                              #")
                print(
                    "#                                                                              #")
                print(
                    "#  ",
                    (int(B) - 12),
                    "g of coffee beans                                                      #")
                print(
                    "#                                                                              #")
                print(
                    "#                                                                              #")
                print(
                    "#  ",
                    (int(C) - 1),
                    "of disposable cups                                                       #")
                print(
                    "#                                                                              #")
                print(
                    "#                                                                              #")
                print(
                    "#  ",
                    (int(m) + 6),
                    "$ of money                                                             #")
                print(
                    "#                                                                              #")
                print(
                    "#                                                                              #")
                print(
                    "################################################################################")
            else:
                print("Error")

#เงื่อนไขการเติมวัตถุดิบ - fill
        elif "fill" in p or "Fill" in p or "FILL" in p:

#ระบุบปริมาณวัตถุดิบต่างๆที่ต้องการเติม
            wf = int(input("write how many ml of water do you want to add:\n>"))
            Mf = int(input("write how many ml of milk do you want to add:\n>"))
            Bf = int(
                input("write how many grams of coffee beans do you want to add:\n>"))
            mf = int(
                input("write how many disposable cups do you want to add:\n>"))

#แสดงวัตถุดิบหลังจากที่เติมแล้ว
            print(
                "################################################################################")
            print(
                "#                                                                              #")
            print(
                "#  **Result                                                                    #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#  *The Coffee machine has:                                                    #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#  ",
                (int(W) + (wf)),
                "ml of water                                                            #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#  ",
                (int(M) + (Mf)),
                "ml of milk                                                             #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#  ",
                (int(B) + (Bf)),
                "g of coffee beans                                                      #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#  ",
                (int(C) + (mf)),
                "of disposable cups                                                      #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#  ",
                (int(m)),
                "$ of money                                                             #")
            print(
                "#                                                                              #")
            print(
                "################################################################################")

#เงื่อนไขขอรับเงิน - take >> จำนวนเงินที่ได้รับ และ วัตถุดิบที่เหลือ
        elif "take" in p or "Take" in p or "TAKE" in p:
            print(
                "################################################################################")
            print(
                "#                                                                              #")
            print(
                "#  < I gave you ",
                (m),
                " $ >                                                      #")
            print(
                "#                                                                              #")
            print(
                "#  **Result                                                                    #")
            print(
                "#  *The Coffee machine has:                                                    #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#  ",
                (int(W)),
                "ml of water                                                            #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#  ",
                (int(M)),
                "ml of milk                                                             #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#  ",
                (int(B)),
                "g of coffee beans                                                      #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#  ",
                (int(C)),
                "of disposable cups                                                       #")
            print(
                "#                                                                              #")
            print(
                "#                                                                              #")
            print(
                "#  ",
                (int(m) - m),
                "$ of money                                                               #")
            print(
                "#                                                                              #")
            print(
                "################################################################################")
        else:
            print("Error")

#ป้อนคำสั่ง restart / exit
        x = input("Exit/Restart : >")
        if "Exit" in x or "exit" in x or "x" in x or "X" in x:
            y = 0
        elif "Restart" in x or "restart" in x or "R" in x or "r" in x:
            y = 1
        else:
            print("Error")
    elif y == 0:
        break
