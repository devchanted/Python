#Previous one we guess the word and printed true or false 
# in this program we will create a list with '_' for the words selected
# then for the letter guessed corerctly , we will replace the '_' with correct letter 

import random

word_list = ["apple", "ball", "cat"]

random_word = random.choice(word_list)
print(random_word)

letter_guess = input("Guess the letter: ").lower()


display = []

for i in range(0,len(random_word)):
    if letter_guess == random_word[i]:
        display.insert(i, random_word[i])
    else:
        display.insert(i, "_")
print(display)


        