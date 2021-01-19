import datetime
def time():
    x = datetime.datetime.now()
    day = (x.strftime("%a"))
    date = (x.strftime("%d"))
    month = (x.strftime("%m"))
    year = (x.strftime("%Y"))
    Time = (x.strftime("%X"))
    all_time = ("{} - {} / {} / {} | {}".format(day,date,month,year,Time))
    return(all_time)

warehouse = []
Volume = []
Date = []

Status = "On"

while Status == "On":
    print("Welcome to My Warehouse Pro. Ver.0.00")
    start = str(input("Choose the command!\n(1)Enter the Warehouse\n(2)Exit\nEnter number > "))
    print("")
    if "2" in start:
        print("Shuting down . . .")
        Status = "off"
    elif "1" in start:
        name = str(input("Enter Warehouse's name > "))
        print("")
        print("Welcome to {} Warehouse".format(name))
        while True:
            command = str(input("Choose the {} Warehouse command!\n(1) Input object\n(2) Delete object \n(3) Show\n(4) Clear\n(5) Sum Volume\n(6) Sum Object\n(7) Exit\nEnter number > ".format(name)))
            print("")
            if "1" in command:
                Input = str(input("In put object's name > "))
                volume = str(input("Input object's volume > "))
                print("You just add object:{} by volume:{} in number:{}\n".format(Input,volume,str(len(warehouse)+1)))
                warehouse.append(Input)
                Volume.append(volume)
                Date.append(time())
            elif "2" in command:
                delete = int(input("Input Number of the object that you want to delete > "))
                if len(warehouse) == 0:
                    print("{} Warehouse is empty!\n".format(name))
                elif delete > len(warehouse):
                    print("the number is out of range!")
                else:
                    print("{}. object:{} volume:{} have deleted!\n".format(str(delete), warehouse[delete - 1],Volume[delete - 1]))
                    warehouse.remove(warehouse[delete-1])
                    Volume.remove(Volume[delete-1])
                    Date.remove(Date[delete-1])
            elif "3" in command:
                n = len(warehouse)
                if n == 0:
                    print("{} Warehouse is empty!\n".format(name))
                else:
                    print("Have {} kind object in {} Warehouse :".format(str(n), name))
                    for i in range(n):
                        print("{}. Name:{} Volume:{} Date:{}".format(str(i+1),warehouse[i],Volume[i],Date[i]))
                    print("")
            elif "4" in command:
                warehouse = []
                Volume = []
                Date = []
                print("{} Warehouse Data have already clear !\n".format(name))
            elif "5" in command:
                Sum_List = []
                for e in Volume:
                    e = int(e)
                    Sum_List.append(e)
                Sum = sum(Sum_List)
                print("Sum of Volume is {}\n".format(str(Sum)))
            elif "6" in command:
                Kind = len(warehouse)
                print("Sum of kind of object is {}\n".format(str(Kind)))
            elif "7" in command:
                Status = "off"
                break
            else:
                print("Error! - Don't have this command\n")
        print("Shuting down . . .")
    elif Status != "On":
        break

    else:
        print("Error! - Don't have this command\n")

