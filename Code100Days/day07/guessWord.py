import random

word_list = ["apple", "ball", "cat"]

random_word = random.choice(word_list)
print(random_word)

word_guess = input("Guess the letter: ").lower()

for letter in range(0, len(random_word)):
    if word_guess == random_word[letter]:
        print("True")
    else:
        print("False")

