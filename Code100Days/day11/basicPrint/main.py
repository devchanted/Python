""" 
Let's create a program that acts as an e-waiter. The program should be able to do the following:
Greet the user by welcoming them to their restaurant and asking for the user’s name.
Prompt the user to choose from starters, main menu, and dessert respectively.
Take their name and repeat their order for confirmation. """


print("Welcome to our restaurant")
name = input("What's youe name: ")

starter = input("Please select a starter (chicken wings, veg platter, soup): ")
main_course = input("Please select a main course item (burger, pasta, steak): ")
dessert = input("What dessert would you like (icecream, cake, ): " )

print(f" Hi {name}, your order is confirmed and {starter}, {main_course} , {dessert} will be ready shortly")