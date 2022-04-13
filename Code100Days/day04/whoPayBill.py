import random


names_string = input("Enter the names seperated by comma: ")

names = names_string.split(", ")

number_of_Persons = len(names)

random_selection = random.randint(0,number_of_Persons-1)

person_pay = names[random_selection]

print("person who is paying today is : " +person_pay)