""" 
The program will ask:

How many letters would you like in your password?
How many symbols would you like?
How many numbers would you like?

The objective is to take the inputs from the user to these questions and then generate a random password.
"""

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#not random password
password = ""
for i in range(0, nr_letters):
    password =  password+letters[i]
for i in range(0,nr_symbols):
    password =  password+symbols[i]
for i in range(0,nr_numbers):
    password =  password+numbers[i]
print("Your simple password is: " +password)

random_password = ""
for i in range(0, nr_letters):
    random_password += random.choice(letters)
for i in range(0,nr_symbols):
    random_password += random.choice(symbols)
for i in range(0,nr_numbers):
    random_password += random.choice(numbers)
print("Your complex  password is: "+random_password)


