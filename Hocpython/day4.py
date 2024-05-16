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
choose = int(input("What do you choose"))
if choose == 0:
    print(rock)
elif choose == 1:
    print(paper)
elif choose == 2:
    print(scissors)
print("Computer choose:")
game = [rock, paper, scissors]
game_len = len(game) - 1
import random
computer = random.randint(0, game_len)
print(game[computer])
if choose == 0:
    if computer == 0:
        print("Draw")
    elif computer == 1:
        print("You win")
    else:
        print("You lose")
elif choose == 1:
    if computer == 1:
        print("Draw")
    elif computer == 2:
        print("You win")
    else:
        print("You lose")
elif choose == 2:
    if computer == 2:
        print("Draw")
    elif computer == 1:
        print("You win")
    else:
        print("You lose")