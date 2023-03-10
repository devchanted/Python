import random

word_list = ["apple", "ball", "cat"]

random_word = random.choice(word_list)
print(random_word)

display = []
for char in range(len(random_word)):
    display.append("_")
print(display)



while '_' in display:
    letter_guess = input("Guess the letter: ").lower()
    for i in range(len(random_word)):
        if letter_guess == random_word[i]:
            display[i] = letter_guess
    print(display)

print(display)
print("You win")
