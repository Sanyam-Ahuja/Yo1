print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
 print("You can ride The rollercoaster")
 age = int(input("What is Your age? "))
 if age <12:
  print("Child Tickets are 5 Dollars")
  bill = 5
 elif age <= 18:
   print("Youth Tickets are 7 Dollars")
   bill = 7
 elif age >= 45 and age <= 55 :
    bill = 0
    print("Everything is Going to be Fine. Have a free Ride on us!")
 else:
    print("Adult Tickets are 12 Dollars")
    bill = 12
 photo = input("Do You want a Photo taken? Y or N. ")
 photo = photo.capitalize()
 if photo == "Y":
   bill += 3
   print(f"You need To Pay {bill}")
 elif photo == "N":
  print(f"You need To Pay {bill}")
else:
  print("You can not ride The rollercoaster Groww taller man")
