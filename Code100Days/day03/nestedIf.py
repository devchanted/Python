print("Welcome to the rollercoaster!")

height = int(input("Enter your height in cms: "))

if height > 120:
    print("Congrats! you are eligible to ride")
    age = int(input("How old are you? "))

    if age > 12:
        print("Please pay $18")
    else:
        print("please pay $7")
else:
    print("Sorry! you are not old enough")