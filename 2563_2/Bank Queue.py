class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def show(self):
        return self.items

def menu():
    print("\nWelcome to Bank's Orders manager programe - Please choose the commands",
          "\n Press 1 Check/Choose the customer in 1st couter",
          "\n Press 2 Check/Choose the customer in 2nd couter",
          "\n Press 3 Add the customer in the orders",
          "\n Press 4 Exit")

Q = Queue()

x = 1

while x==1:

    menu()

    Num = int(input("Choose the command\n>>>"))

    Waiting = Q.size()

    if Num == 1:
        if Waiting > 0:
            DeQ = Q.dequeue()
            ShowQ = Q.show()
            print("({}) is coming to Counter 1".format(DeQ))
            Waiting -= 1
            print("Waiting Customer : ({})".format(Waiting))
            print("Waiting Customer (Name) : ({})".format(ShowQ))
        else:
            print("Waiting Customer : ({})".format(Waiting))
            print("No one Waiting")

    elif Num == 2:
        if Waiting > 0:
            DeQ = Q.dequeue()
            ShowQ = Q.show()
            print("({}) is coming to Counter 2".format(DeQ))
            Waiting -= 1
            print("Waiting Customer : ({})".format(Waiting))
            print("Waiting Customer (Name) : ({})".format(ShowQ))
        else:
            print("Waiting Customer : ({})".format(Waiting))
            print("No one Waiting")

    elif Num == 3:
        Name_input = input("Enter Customer Name\n>>>").strip()
        Q.enqueue(Name_input)
        ShowQ = Q.show()
        print("Waiting Customer : ({})".format(Waiting))
        print("Waiting Customer (Name) : ({})".format(ShowQ))

    else:
        x = 0

while x != 1:
    break