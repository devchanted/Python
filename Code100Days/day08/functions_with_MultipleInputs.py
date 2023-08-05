# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello")
    print("Welcome")
    print("Thank you!")

greet()

#functions that allows input

""" def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}")

greet_with_name(input("Enter your name: ")) """

#functions with multiple inputs

def gree_with(name,location):
    print(f"Hello {name}")
    print(f"how is it in {location}")

gree_with(input("Your Name: "), input("Where are you from? : "))
