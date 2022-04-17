import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
human_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. " ))
print("You Chose")
print(game_images[human_selection])
machine_selection = random.randint(0, 2)
print(machine_selection)
print("Machine Chose")
print(game_images[machine_selection])

if human_selection == 2 and machine_selection == 0:
    print("You Lose")
elif human_selection == 0 and machine_selection == 2:
    print("You Win")
elif human_selection > machine_selection:
    print("You Win")
elif human_selection < machine_selection:
    print("You Lose")
elif human_selection == machine_selection:
    print("Draw")
else:
    print("Invalid Entry")


