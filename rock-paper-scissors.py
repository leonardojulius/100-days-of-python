import random
rock = "Rock"'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper ="Paper"'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors ="Scissors"'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
List = [rock,paper,scissors]

Mychoice =List
my = int(input(f"What do you choose?Type 0 for Rock, 1 for Paper or 2 for Scissors "))

print(f"You Chose:{Mychoice[my]}")


ComputerChoice = List
ran = random.randint(0,2)
conv=int(ran)

print(f"Computer chose: {ComputerChoice[conv]}")

Yw="You Win!!!"

if my==0 and conv==2:
  print(Yw)
elif my==2 and conv==1:
  print(Yw)
elif my==1 and conv==0:
  print(Yw)
elif my==conv:
    print("draw")  
else:
  print("You lose")  




