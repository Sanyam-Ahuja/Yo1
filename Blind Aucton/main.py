import os
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
#HINT: You can call clear() to clear the output in the console.
auctions = {}
a = input("Are You Sure You Want TO Bid y For Yes: ").lower()
while a == "y":
  new_name = input("What is You name: ")
  new_amount = float(input("What Is The Amount You Want To Bid: "))
  auctions[new_name] = new_amount
  a = input("Are There more Bidders y For Yes: ").lower()
  if a == "y":
    clearConsole()

def highest(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    b_a = bidding_record[bidder]
    if b_a > highest_bid:
      highest_bid = b_a
      winner = bidder
  print(f"{winner} won as he/she had the highest amount {highest_bid}")

highest(auctions)