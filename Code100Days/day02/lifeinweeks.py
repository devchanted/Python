#Assuming we live 90 years

age = input("What is your current age? " )
years_left = 90 - int(age)
weeks_left = years_left * 52
months_left = years_left * 12 
days_left = years_left * 365

print("You have " + str(days_left) + " days," + str(weeks_left) +" weeks, and " + str(months_left) + " months left.")

print("print using f strings")
print(f"yoh have {days_left} days {weeks_left} weeks and {months_left} left ")