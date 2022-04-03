
from tkinter.tix import InputOnly


print("Welcome to tip calculator")
total_bill = int(input("what was the total bill? "))
percent_tip = int(input("what percentage tip would you like to gibe? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_bill_with_tip = float((total_bill) + (total_bill* (percent_tip)/100))
pay_per_person = total_bill_with_tip/int(people)

print(f"Each person should pay: ${pay_per_person}")