print("Welcome to roller coaster")

height = int(input("Enter your height in cms: "))
price = 0
if height > 120 :
    age = int(input("Please enter your age: "))

    if age < 12:
        price = 5
    elif age <18:
        price = 7
    elif age >=45 and age <=55:
        print("please ride for free")
    else:
        price = 12
    
    photo = input("Do you need photos? ")

    if photo == "yes":
        price = price + 3
        print(f"Total ticket price is : {price} ")
    elif price == "no":
        print(f"Total ticket price is : {price} ")
    else:
        print(f"Invalid Entry")
else:
    print("you are not tall enough")