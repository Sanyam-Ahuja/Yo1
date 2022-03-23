import random
print('''  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
''')
print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.''')
def random_number():
    return random.randint(1,100)
number = random_number()
def diff(chosen):
    if chosen == "e":
        return 10
    elif chosen == "d":
        return 5
chose = input("Chose A Difficulty 'e' for easy and 'd' for difficult. You Get 10 chances in easy and 5 chances in difficult: ")
turns = diff(chose)


win = False
def check_number():
    global win
    global turns
    if turns == 1:
        print(f"Oh No You Lost You ran Out Of Chances The No. Was {number}")
        win = True
    elif c_n > 100:
        print("Please enter a No. Between 1 and 100")
    elif c_n > number:
        turns = turns - 1
        print(f"You Went a Little Ahead Try a Smaller No. You Have {turns} left")
    elif c_n < number:
        turns = turns - 1
        print(f"You Went a Little Low Try a larger No. You Have {turns} left")
    elif c_n == number:
        print(f"Yay You guessed it right the no. was {number}")
        win = True

while not win:
    c_n = int(input("Chose a no. between 1 and 100: "))
    check_number()