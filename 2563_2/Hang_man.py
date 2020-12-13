wordlist = ['python','java','kotlin','javascrip']

import random
word = random.choice(wordlist)
#print(word)

HP = 8
text = ""

while True:
    for i in word:
        if i in text:
            print(i,end=" ")
            check = "T"
        else:
            print("_",end=" ")
            check = "F"

    answer = str(input("\n>>>"))
    if answer in text:
        print("This answer has already in the word")
    else:
        text += answer


    if answer not in word:
        print("No such letter in the word ")
        HP -= 1
        print("HP : ",HP)
    if HP <= 0:
        print("You're lose! ToT")
        break
    if "F" not in check:
        print("Congreatulation You Win!!!")
        break