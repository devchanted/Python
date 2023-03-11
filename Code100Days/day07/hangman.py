import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False

word_list = ["ardvark", "baboon", "camel"]
word_random = random.choice(word_list)
print(word_random)
lives = 6

display = []
for char in range(len(word_random)):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for char in range(len(word_random)):
        letter = word_random[char]
        if guess == letter:
            display[char] = letter
    if guess not in word_random:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")
print(f"{' '.join(display)}")

if "_" not in display:
        end_of_game = True
        print("You win.")

print(stages[lives])

