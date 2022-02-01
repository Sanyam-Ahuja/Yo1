# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
n_1 = name1.lower()
n_2 = name2.lower()
t_o = n_1.count("t") + n_2.count("t")
r_o = n_1.count("r") + n_2.count("r")
u_o = n_1.count("u") + n_2.count("u")
e_o = n_1.count("e") + n_2.count("e")

val_1 = t_o + r_o +u_o + e_o
val_str_1 = str(val_1)

l_o = n_1.count("l") + n_2.count("l")
o_o = n_1.count("o") + n_2.count("o")
v_o = n_1.count("v") + n_2.count("v")
e1_o = n_1.count("e") + n_2.count("e")
val_2 = l_o + o_o + v_o + e1_o
val_str_2 = str(val_2)
val_str = val_str_1 + val_str_2
val = int(val_str)

if val < 10 or val > 90:
  print(f"Your score is {val}, you go together like coke and mentos.")
elif val > 40 and val < 50:
  print(f"Your score is {val}, you are alright together.")
else:
    print(f"Your score is {val}.")