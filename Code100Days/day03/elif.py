print("Welcome to the rollercoaster")

height = int(input("Enter you height: "))

if height > 120:
    print("Congrats! you are eligible to ride")
    age = int(input("please enter your age: "))
    if age < 12:
        print("Pay $5")
    elif age<=18:
        print("Pay $7")
    else:
        print("Pay $12")
else:
    print("Sorry, you are not old enough")