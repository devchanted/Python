print("Welcome to roller coaster")

height = int(input("Enter your height in cms: "))

if height > 120 :
    age = int(input("Please enter your age: "))

    if age < 12:
        price = 5
    elif age <18:
        price = 7
    else:
        price = 12
    
    photo = input("Do you need photos? ")

    if photo == "yes":
        price = price + 3
        print(f"Total ticket price is : {price} ")
    else:
        print(f"Total ticket price is : {price} ")
else:
    print("you are not tall enough")