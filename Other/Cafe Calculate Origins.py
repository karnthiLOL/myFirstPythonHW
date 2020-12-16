W = 400
M = 540
B = 120
C = 9
m = 550

y = 1
while True:
  if y == 1:

    print("The Coffee machine has:")
    print((W),"ml of water")
    print((M),"ml of milk ")
    print((B),"g of coffee beans")
    print((C),"of disposable cups ")
    print((m),"$ of money")

    p = input("choose one option - buy / fill/ take\n>")

    if "buy" in p or "Buy" in p or "BUY" in p:
      c = str(input("choose kind of coffee - (1)espresso / (2)latte / (3)cappuccino\n>"))
      if 'espresso' in c or '1' in c:
        print("you must pay 4 $")
        print("")
        print("The Coffee machine has:")
        print(int(W)-250,"ml of water")
        print((M),"ml of milk ")
        print(int(B)-16,"g of coffee beans")
        print(int(C)-1,"of disposable cups ")
        print(int(m)-4,"$ of money") 
      elif 'latte' in c or '2' in c:
        print("you must pay 7 $")
        print("")
        print("The Coffee machine has:")
        print(int(W)-350,"ml of water")
        print(int(M)-75,"ml of milk ")
        print(int(B)-20,"g of coffee beans")
        print(int(C)-1,"of disposable cups ")
        print(int(m)-7,"$ of money")
      elif 'cappuccino' in c or '3' in c:
        print("you must pay 6 $")
        print("")
        print("The Coffee machine has:")
        print(int(W)-200,"ml of water")
        print(int(M)-100,"ml of milk ")
        print(int(B)-12,"g of coffee beans")
        print(int(C)-1,"of disposable cups ")
        print(int(m)+6,"$ of money")
      else:
        print("Error")

    elif "fill" in p or "Fill" in p or "FILL" in p:
      wf = int(input("write how many ml of water do you want to add:\n>"))
      Mf = int(input("write how many ml of milk do you want to add:\n>"))
      Bf = int(input("write how many grams of coffee beans do you want to add:\n>"))
      mf = int(input("write how many disposable cups do you want to add:\n>"))
      print("")
      print("The Coffee machine has:")
      print(int(W)+(wf),"ml of water")
      print(int(M)+(Mf),"ml of milk ")
      print(int(B)+(Bf),"g of coffee beans")
      print(int(C)+(mf),"of disposable cups ")
      print(int(m),"$ of money")

    elif "take" in p or "Take" in p or "TAKE" in p:
      print("I gave you $",(m))
      print("")
      print("The Coffee machine has:")
      print(int(W)+(wf),"ml of water")
      print(int(M)+(Mf),"ml of milk ")
      print(int(B)+(Bf),"g of coffee beans")
      print(int(C)+(mf),"of disposable cups ")
      print(int(m),"$ of money")
    else:
      print("Error")  

    x = input("Exit/Restart\n>")
    if "Exit" in x:
      y = 0
    elif "Restart" in x:
      y = 1
    else:
      print("Error")
  elif y == 0:
    break
