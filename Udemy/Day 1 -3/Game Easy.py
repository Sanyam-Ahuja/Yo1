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

#Write your code below this line 👇
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