import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
import random
print("Welcome To The Game Of Black Jack")
input("Press Enter Key To Begin")
clearConsole()

play = True
while play:
    p_1 = random.randint(1, 11)
    p_2 = random.randint(1, 11)

    c_1 = random.randint(1, 11)
    c_2 = random.randint(1, 11)

    choice = random.randint(0,1)
    if choice == 1:
        c_3 = random.randint(1, 11)
    else:
        c_3 = 0
    print(f"You Got Two Cards They Are {p_1} and {p_2}")
    print(f"One Of The Computer Cards is {c_1}")

    if input("Type 'y' to get another card and 'n' to go with this card") == "y":
        p_3 = random.randint(1, 11)
    else:
        p_3 = 0
    t_s_p = p_1 + p_2 + p_3
    t_s_c = c_1 + c_2 + c_3

    if t_s_p > t_s_c and t_s_p<22:
        print(f"Yay You won as your score {t_s_p} was higher Than Computer's{t_s_c}")
    elif t_s_c>21:
        print(f"Yay You won as Computer's Score {t_s_c} was higher that 21. Your score Was {t_s_p}")
    elif t_s_c> t_s_p and t_s_c<22:
        print(f"Oh No You Lost as Your score was lower than that of comp. Your score was {t_s_p} and computer's score was {t_s_c}")
    elif t_s_p>21:
        print(f"Oh No You Lost as Your score was Higher Than 21. Your score was {t_s_p} and computer's score was {t_s_c}")
    elif t_s_p == t_s_c:
        print("OMG ITS A DRAW Lets Play Again")
    print(f"All Your Cards Were {p_1}, {p_2}, {p_2} ")
    print(f"All Computer's Cards were {c_1}, {c_2}, {c_3} ")

    if input("If You want to play again type 'y' if not type 'n'") == "y":  
        clearConsole()
    else:
        play = False
        print("Thanks For Playing Come Again")