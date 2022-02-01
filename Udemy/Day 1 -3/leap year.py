# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
check_1 = year % 4 
check_2 = year % 100
check_3  = year % 400
if check_1 == 0 :
 if check_2 == 0:
  if check_3 == 0: 
   print("Leap year.")
  else:
   print("Not leap year.")
 else:
   print("Leap year.")
else:
 print("Not leap year.")

