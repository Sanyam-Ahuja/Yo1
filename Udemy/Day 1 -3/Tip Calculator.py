#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = input("What was the total bill? ")
bill_float = float(bill)
bill_rounded = round(bill_float, 2)
tip = input("How much tip would you like to give(percentage such as 10 ,12 , 15) ")
tip_int = int(tip)
split = input("How many people to split the bill? ")
tip_money = bill_rounded*(tip_int/100)
total_money = bill_rounded + tip_money
split_int = int(split)
pay = round(total_money/split_int , 2)
print(f"Each Person Should Pay: {pay}")