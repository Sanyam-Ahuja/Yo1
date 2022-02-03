import random
from english_words import english_words_set
from PyDictionary import PyDictionary
words = list(english_words_set)
chosen = "r"
dict = PyDictionary()
meaning = dict.meaning(chosen)
print(f"This is The Meaning Of The Word You Are Going To Guess{meaning}")
chose_edit = chosen
def anti_vowel(c = input):
    newstr = c
    vowels = ('b','R', 'c', 'd', 'f', 'g', 'h', 'j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
    for x in c.lower():
        if x in vowels:
            newstr = newstr.replace(x,"_")
    newstr = list(newstr)
    print(newstr)

chose_edit = list(chosen)
anti_vowel(chosen)
guess = input("What letter Do U want To enter First").lower

for position in range(len(chose_edit)):
    letter = chose_edit[position]
    if letter == guess:
        print("k")