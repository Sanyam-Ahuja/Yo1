import random
from english_words import english_words_set
from PyDictionary import PyDictionary
words = list(english_words_set)
chosen_1 = random.choice(words).lower()
chosen = list(chosen_1)
dict = PyDictionary()
meaning = dict.meaning(chosen_1)
print(f"This is The Meaning Of The Word You Are Going To Guess{meaning}")
chose_edit = list(chosen)
def anti_vowel(c = input):
    newstr = c
    vowels = ('b','R', 'c', 'd', 'f', 'g', 'h', 'j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
    for x in c.lower():
        if x in vowels:
            newstr = newstr.replace(x,"_")
    newstr = list(newstr)
    lives = len(chose_edit)
    for position_1 in range(len(chose_edit)):
        if chose_edit[position_1]== "a" or chose_edit[position_1] == "e" or chose_edit[position_1] =="i" or chose_edit[position_1] =="o" or chose_edit[position_1] =="u":
            lives -= 1
    print(newstr)
    endgame = False
    while not endgame:
        for position in range(len(chose_edit)):
            print(f"Right now U have {lives} lives")
            guess = input("What letter Do U want To enter now\n").lower()
            for position_2 in range(len(chosen)):
                letter = chosen[position_2]
                if letter == guess:
                    newstr[position_2] = letter
                    print(newstr)
                elif guess== "a" or guess == "e" or guess =="i" or guess =="o" or guess =="u":
                    print("Pls Dont enter Any Vowels They are already given i.e dont use a e i o u")
            if "_" not in newstr:
                endgame = True
                print("You win.")
            if guess not in chosen:
                lives -= 1
                print(f"Oh You Lost 1 life, You have {lives} lives left\n {newstr}")
                if lives == 0:
                    endgame = True
                    print("Oh No You Lost The Game")
anti_vowel(chosen_1)
print(f"The Real Word Was {chosen_1}")