"""Tip calculator project
We're going to build a tip calculator.
If the bill was $150.00, split between 5 people, with 12% tip.
Each person should pay:
(150.00 / 5) * 1.12 = 33.6
After formatting the result to 2 decimal places = 33.60"""

print("Welcome to tip calculator!")
bill = float(input("What was the total bill? € "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people =int(input("How many people to split the bill?"))

tip_percent = tip / 100 
tip_amount = bill * tip_percent
bill_with_tip = bill + tip_amount
bill_with_tip_per_person = bill_with_tip / people
final_amount = round(bill_with_tip_per_person, 2)

print(f"Each person :€{final_amount}")