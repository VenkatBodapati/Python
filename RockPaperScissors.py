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

#Write your code below this line 👇
import random

game_list = [rock,paper,scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0,len(game_list)-1)

print(game_list[user_choice])

print ("Computer choose: ")
print(game_list[computer_choice])

if user_choice == 0:
    if computer_choice == 1 :
        print("Computer wins")
    elif computer_choice == 2:
        print("You win")
    else:
        print('Match draw')
elif user_choice == 1:
    if computer_choice == 1 :
        print("Match draw")
    elif computer_choice == 2:
        print("Computer win")
    else:
        print('You wins')
else:
    if computer_choice == 2 :
        print("Match draw")
    elif computer_choice == 1:
        print("You win")
    else:
        print('Computer wins')
    
