print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
_meaning = input("To see The Code Meaning of Difficulty Press I or Just Press Enter To play game\n")
if _meaning == "I":
    print("In Easy There Is a Specified Answer To The Questions\n In Medium The Value Changes Sometimes \n In Difficult The Values Changes everytime")
else:
    print("")
diff = input("Choose Your Difficulty (D = Super Duper Difficult, Medium = M, Easy = E)\n")
if diff == "E":
    start = input("Would You like to go right or left? (L, R)\n").capitalize()
    if start == "R":
        _2nd = input("Would You Like to Swim across the lake or Wait For The boat? (W,S)\n").capitalize()
        if _2nd == "S":
            _3rd = input("Would U Like to Dig down on Cross or Go in The Palace (DD , G)\n").capitalize()
            if _3rd == "G":
                _4th = input("Which Door Would You Like To Go? (Y, D, R)\n").capitalize()
                if _4th == "D":
                    print("Yo You found The Treasure With 400000000000000 Gold Coins U win")
                elif _4th == "Y":
                    print("Lol You Lost You went in a room of flames")
                elif _4th == "R":
                    print("LOL you Lost You Went into a room With Bears")
            else:
                    print("Lol You Lost You Dug Down And Fell In Lava")
        else:
                print("Lol You Lost You just kept waiting For Your Dumb Boat")
    else:
        print("Lol You Lost You were eaten by the Tiger")
elif diff == "M":
    import random
    from re import S
    n = 1
    print (n)
    m = "R"
    k = "S"
    r = "G"
    s = "Y"
    if n == 2 or n== 3:
        m = m.replace("R", "L")
    else:
        m = "R"
    if n == 2 or n == 1:
        k  = k.replace("S","W")
    else:
        k = "S"
    if n == 3 or n== 1:
        r = r.replace("G", "D")
    else:
        r = "G"
    if n == 2 or n== 3:
        s.replace("Y", "D")
    elif n == 1:
        s.replace("Y", "R")
    else :
        s = "Y"
    start = input("Would You like to go right or left? (L, R)\n").capitalize()
    if start == m:
        _2nd = input("Would You Like to Swim across the lake or Wait For The boat? (W,S)\n").capitalize()
        if _2nd == k:
            _3rd = input("Would U Like to Dig down on Cross or Go in The Palace (D , G)\n").capitalize()
            if _3rd == r:
                _4th = input("Which Door Would You Like To Go? (Y, D, R)\n").capitalize()
                if _4th == s:
                    print("Yo You found The Treasure With 400000000000000 Gold Coins U win")
                elif _4th == "D":
                    print("Lol You Lost You went in a room of flames")
                elif _4th == "R":
                    print("LOL you Lost You Went into a room With Bears")
            elif _3rd != r and _3rd == "G" :
                print("Lol You Lost You Dug Down And Fell In Lava")
            elif _3rd != r and _3rd == "D":
                print("Lol u Lost U were killed By The Palace Gaurds")
        elif _2nd != k and _2nd == "W":
            print("Lol You Lost You just kept waiting For Your Dumb Boat")
        elif _2nd != k and _2nd == "S":
            print("Lol U Lost You were Eaten By The Crocodiles")
    else:
        print("Lol You Lost You were eaten by the Tiger")
elif diff == "D":
    import random
    n_1 = random.randint(1,10)

    if n_1 == 1:
        start = input("Would You like to go right or left? (L, R)\n").capitalize()
        if start == "R":
            _2nd = input("Would You Like to Swim across the lake or Wait For The boat? (W,S)\n").capitalize()
            if _2nd == "S":
                _3rd = input("Would U Like to Dig down on Cross or Go in The Palace (DD , G)\n").capitalize()
                if _3rd == "G":
                    _4th = input("Which Door Would You Like To Go? (Y, D, R)\n").capitalize()
                    if _4th == "D":
                        print("Yo You found The Treasure With 400000000000000 Gold Coins U win")
                    elif _4th == "Y":
                        print("Lol You Lost You went in a room of flames")
                    elif _4th == "R":
                        print("LOL you Lost You Went into a room With Bears")
                else:
                    print("Lol You Lost You Dug Down And Fell In Lava")
            else:
                print("Lol You Lost You just kept waiting For Your Dumb Boat")
        else:
            print("Lol You Lost You were eaten by the Tiger")
    elif n_1== 2:
        start = input("Would You like to go right or left? (L, R)\n").capitalize()
        if start == "L":
            _2nd = input("Would You Like to Swim across the lake or Wait For The boat? (W,S)\n").capitalize()
            if _2nd == "W":
                _3rd = input("Would U Like to Dig down on Cross or Go in The Palace (D , G)\n").capitalize()
                if _3rd == "D":
                    _4th = input("Which Door Would You Like To Go? (Y, D, R)\n").capitalize()
                    if _4th == "Y":
                        print("Yo You found The Treasure With 400000000000000 Gold Coins U win")
                    elif _4th == "D":
                        print("Lol You Lost You went in a room of flames")
                    elif _4th == "R":
                        print("LOL you Lost You Went into a room With Bears")
                else:
                    print("Lol You Lost You were killed by the Guards in the palace")
            else:
                print("Lol You Lost You were Eaten By The Crocodiles")
        else:
            print("Lol You Lost You were eaten by the Tiger")
    elif n_1 == 3 :
        start = input("Would You like to go right or left? (L, R)\n").capitalize()
        if start == "R":
            _2nd = input("Would You Like to Swim across the lake or Wait For The boat? (W,S)\n").capitalize()
            if _2nd == "W":
                _3rd = input("Would U Like to Dig down on Cross or Go in The Palace (D , G)\n").capitalize()
                if _3rd == "G":
                    _4th = input("Which Door Would You Like To Go? (Y, D, R)\n").capitalize()
                    if _4th == "R":
                        print("Yo You found The Treasure With 400000000000000 Gold Coins U win")
                    elif _4th == "Y":
                        print("Lol You Lost You went in a room of flames")
                    elif _4th == "D":
                        print("LOL you Lost You Went into a room With Bears")
                else:
                    print("Lol You Lost You Dug Down And Fell In Lava")
            else:
                print("Lol You Lost You were Eaten By The Crocodiles")
        else:
            print("Lol You Lost You were eaten by the Tiger")
    elif n_1 == 4 :
        start = input("Would You like to go right or left? (L, R)\n").capitalize()
        if start == "R":
            _2nd = input("Would You Like to Swim across the lake or Wait For The boat? (W,S)\n").capitalize()
            if _2nd == "S":
                _3rd = input("Would U Like to Dig down on Cross or Go in The Palace (D , G)\n").capitalize()
                if _3rd == "D":
                    _4th = input("Which Door Would You Like To Go? (Y, D, R)\n").capitalize()
                    if _4th == "Y":
                        print("Yo You found The Treasure With 400000000000000 Gold Coins U win")
                    elif _4th == "R":
                        print("Lol You Lost You went in a room of flames")
                    elif _4th == "D":
                        print("LOL you Lost You Went into a room With Bears")
                else:
                    print("Lol You Lost You were Killed By The Palace Gaurds")
            else:
                print("Lol You Lost You just kept waiting For Your Dumb Boat")
        else:
            print("Lol You Lost You were eaten by the Tiger")
    elif n_1 == 5 :
        start = input("Would You like to go right or left? (L, R)\n").capitalize()
        if start == "L":
            _2nd = input("Would You Like to Swim across the lake or Wait For The boat? (W,S)\n").capitalize()
            if _2nd == "S":
                _3rd = input("Would U Like to Dig down on Cross or Go in The Palace (D , G)\n").capitalize()
                if _3rd == "G":
                    _4th = input("Which Door Would You Like To Go? (Y, D, R)\n").capitalize()
                    if _4th == "D":
                        print("Yo You found The Treasure With 400000000000000 Gold Coins U win")
                    elif _4th == "Y":
                        print("Lol You Lost You went in a room of flames")
                    elif _4th == "R":
                        print("LOL you Lost You Went into a room With Bears")
                else:
                    print("Lol You Lost You Dug Down And Fell In Lava")
            else:
                print("Lol You Lost You just kept waiting For Your Dumb Boat")
        else:
            print("Lol You Lost You were eaten by the Tiger")
    elif n_1 == 6 :
        start = input("Would You like to go right or left? (L, R)\n").capitalize()
        if start == "R":
            _2nd = input("Would You Like to Swim across the lake or Wait For The boat? (W,S)\n").capitalize()
            if _2nd == "W":
                _3rd = input("Would U Like to Dig down on Cross or Go in The Palace (D , G)\n").capitalize()
                if _3rd == "D":
                    _4th = input("Which Door Would You Like To Go? (Y, D, R)\n").capitalize()
                    if _4th == "R":
                        print("Yo You found The Treasure With 400000000000000 Gold Coins U win")
                    elif _4th == "Y":
                        print("Lol You Lost You went in a room of flames")
                    elif _4th == "D":
                        print("LOL you Lost You Went into a room With Bears")
                else:
                    print("Lol You Lost You were Killed By The Palace Gaurds")
            else:
                print("Lol You Lost You were Eaten By The Crocodiles")
        else:
            print("Lol You Lost You were eaten by the Tiger")
    elif n_1 == 7 :
        start = input("Would You like to go right or left? (L, R)\n").capitalize()
        if start == "R":
            _2nd = input("Would You Like to Swim across the lake or Wait For The boat? (W,S)\n").capitalize()
            if _2nd == "W":
                _3rd = input("Would U Like to Dig down on Cross or Go in The Palace (D , G)\n").capitalize()
                if _3rd == "G":
                    _4th = input("Which Door Would You Like To Go? (Y, D, R)\n").capitalize()
                    if _4th == "D":
                        print("Yo You found The Treasure With 400000000000000 Gold Coins U win")
                    elif _4th == "Y":
                        print("Lol You Lost You went in a room of flames")
                    elif _4th == "R":
                        print("LOL you Lost You Went into a room With Bears")
                else:
                    print("Lol You Lost You Dug Down And Fell In Lava")
            else:
                print("Lol You Lost You were Eaten By The Crocodiles")
        else:
            print("Lol You Lost You were eaten by the Tiger")
    elif n_1 == 8 :
        start = input("Would You like to go right or left? (L, R)\n").capitalize()
        if start == "L":
            _2nd = input("Would You Like to Swim across the lake or Wait For The boat? (W,S)\n").capitalize()
            if _2nd == "S":
                _3rd = input("Would U Like to Dig down on Cross or Go in The Palace (D , G)\n").capitalize()
                if _3rd == "D":
                    _4th = input("Which Door Would You Like To Go? (Y, D, R)\n").capitalize()
                    if _4th == "D":
                        print("Yo You found The Treasure With 400000000000000 Gold Coins U win")
                    elif _4th == "Y":
                        print("Lol You Lost You went in a room of flames")
                    elif _4th == "R":
                        print("LOL you Lost You Went into a room With Bears")
                else:
                    print("Lol You Lost You were Killed By The Palace Gaurds")
            else:
                print("Lol You Lost You just kept waiting For Your Dumb Boat")
        else:
            print("Lol You Lost You were eaten by the Tiger")
    elif n_1 == 9 :
        start = input("Would You like to go right or left? (L, R)\n").capitalize()
        if start == "R":
            _2nd = input("Would You Like to Swim across the lake or Wait For The boat? (W,S)\n").capitalize()
            if _2nd == "S":
                _3rd = input("Would U Like to Dig down on Cross or Go in The Palace (D , G)\n").capitalize()
                if _3rd == "D":
                    _4th = input("Which Door Would You Like To Go? (Y, D, R)\n").capitalize()
                    if _4th == "R":
                        print("Yo You found The Treasure With 400000000000000 Gold Coins U win")
                    elif _4th == "Y":
                        print("Lol You Lost You went in a room of flames")
                    elif _4th == "D":
                        print("LOL you Lost You Went into a room With Bears")
                else:
                    print("Lol You Lost You were Killed By The Palace Gaurds")
            else:
                print("Lol You Lost You just kept waiting For Your Dumb Boat")
        else:
            print("Lol You Lost You were eaten by the Tiger")
    elif n_1 == 10 :
        start = input("Would You like to go right or left? (L, R)\n").capitalize()
        if start == "L":
            _2nd = input("Would You Like to Swim across the lake or Wait For The boat? (W,S)\n").capitalize()
            if _2nd == "S":
                _3rd = input("Would U Like to Dig down on Cross or Go in The Palace (D , G)\n").capitalize()
                if _3rd == "G":
                    _4th = input("Which Door Would You Like To Go? (Y, D, R)\n").capitalize()
                    if _4th == "Y":
                        print("Yo You found The Treasure With 400000000000000 Gold Coins U win")
                    elif _4th == "D":
                        print("Lol You Lost You went in a room of flames")
                    elif _4th == "R":
                        print("LOL you Lost You Went into a room With Bears")
                else:
                    print("Lol You Lost You Dug Down And Fell In Lava")
            else:
                print("Lol You Lost You just kept waiting For Your Dumb Boat")
        else:
            print("Lol You Lost You were eaten by the Tiger")
#Working Of Code Is Below
# Here is How This Code Works
# First It Asks if You Want To know The Difficulty Pattern If You ask For It It gives the difficulty Settings. If Not it Continues
# Then It Asks For The Difficulty You Want
# According To Your Choice it seperates The Code in 3 If elif elif
# If The Difficuty Chosen is Easy
# Then The Answers Have Specefic Values to win They Are Constant
# It asks if You want to go Right or left
# if You Choose Left(Example) It takes You Forward Other wise It ends the code Saying You Lost
# And It goes on in this Pattern

# In Medium Also The Patern Is Same the Only Difference is The Right Answers are not constant But Variable They Change According To The No. Given By Random Function, Nut It only has 3 Possibilities It has a Winning probablity of 13% appox

# In Super Duper Difficut also Its The Same pattern But There Are 10 possibilities of Random Funtion Hence Winning Chances are 2 or 3 % appox
# Huff It was A long typing at my tortoise speed of 18WPM ;D