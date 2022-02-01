import random
print("Lets Play Rock Paper Scisor")
player = input("What Do You Want To Choose R= Rock, P = Paper, S= Scisors\n").capitalize()
comp = random.randint(1,3)
if comp == 1:
    ccomp = "R"
elif comp == 2:
    ccomp = "P"
elif comp == 3:
    ccomp = "S"
print(f"You Chose {player} and Computer Chose {ccomp}")
if ccomp == player:
    print("Draw")
elif ccomp != player:
    if ccomp == "R" and player == "S":
        print(f"Computer Won As It Chosse {ccomp} and you chose {player}")
    elif ccomp == "R" and player == "P":
        print(f"Computer Lost As It Chosse {ccomp} and you chose {player}")
    elif ccomp == "S" and player == "R":
        print(f"Computer Lost As It Chosse {ccomp} and you chose {player}")
    elif ccomp == "S" and player == "P":
        print(f"Computer Won As It Chosse {ccomp} and you chose {player}")
    elif ccomp == "P" and player == "R":
        print(f"Computer Won As It Chosse {ccomp} and you chose {player}")
    elif ccomp == "P" and player == "S":
        print(f"Computer Lost As It Chosse {ccomp} and you chose {player}")