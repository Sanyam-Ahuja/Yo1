<<<<<<< HEAD
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
=======
# import random

# # 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆
>>>>>>> 65eb86fb698e6413038a5cd285076e35cd4aa5a0

# #Write your code below this line 👇
# print(random.choice(names))

a= ["yo", "jo", "lo", "go"]
b = ["Sam", "Game", "Lame"]
c = [a , b]
c[1][2] = "Sanyam"
print(c)
