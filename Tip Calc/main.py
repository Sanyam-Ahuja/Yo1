print("Welcome To The Tip Calculator $")
tb = float(input("What was the Total Bill? "))
tip = float(input("How Much Tip Do You want to give? 10, 12 , 15 "))
np = float(input("No. Of People? "))
ep = (tb * (tip/100) + tb) /np
print (round(ep,2))