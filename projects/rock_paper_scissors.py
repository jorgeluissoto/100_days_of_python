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

user_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_pick = random.randint(0,2)

# User pick
if user_pick == 0:
  print(rock)
elif user_pick == 1:
  print(paper)
else:
  print(scissors)

print(f"Computer Chose:")
#print(computer_pick)

# Computer pick
if computer_pick == 0:
  print(rock)
elif computer_pick == 1:
  print(paper)
else:
  print(scissors)

# Logic to find winner
if user_pick >= 3 or user_pick <0:
  print("You typed an invalid number, you lose!")
else:
    if user_pick == 0 and computer_pick == 2:
       print("You Win!")
    elif user_pick == 2 and computer_pick == 1:
       print("You Win!")
    elif user_pick == 1 and computer_pick == 0:
        print("You Win")
    elif user_pick == computer_pick:
       print("DRAW!")
    else:
       print("You LOSE!")



