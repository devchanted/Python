import random
print("Welcome to Number Guessing Game")

random_number = random.randint(1,100)

guess_number = int(input("Enter your Guess: "))

if random_number == guess_number:
    print("Yayy! you guessed it right")
else:
    print(f" You lost. The number is:  {random_number} ")