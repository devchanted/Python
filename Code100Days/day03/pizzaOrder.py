from re import M


print("Welcome to awesome Pizza Shop")

size = input("What size pizz you woould like to order. S M L : ")
pepperoni = input('Do you want pepperoni? Y or N :')
extra_cheese = input("Do you need extra cheese? Y or N: ")
bill =0

if size == "L":
    bill =+25
elif size == "M":
    bill =+20
elif size == "S":
    bill =+15
else:
    print("invalid Entry")

if pepperoni == "Y":
    if size == "S":
        bill =+2
    else:
        bill =+3

if extra_cheese == "Y":
    bill +=1

print(bill)


