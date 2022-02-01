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