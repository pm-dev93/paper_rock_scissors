# Pedra papel ou tesoura 
import random

your_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
computer_choice = random.randint(0,2)
a ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''# rock
b = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''#paper
c = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)  
'''# scissors
if your_choice == "0":
    if computer_choice == 0:
        print(f'''You chose rock.
{a}
The computer chose rock. 
{a}    
It's a draw.''')
    elif computer_choice == 1:
        print(f'''You chose rock.
{a}
The computer chose paper.
{b}
You lose.''')
    elif computer_choice == 2:
        print(f'''You chose rock. 
{a}             
The computer chose scissors. 
{c} 
You win.''')
else:
    print("You choose a invalid number. You lose LOOSER!")
if your_choice == "1":
    if computer_choice == 0:
        print(f'''You chose paper.
{b}
The computer chose paper. 
{b}    
It's a draw.''')
    elif computer_choice == 1:
        print(f'''You chose paper.
{b}
The computer chose scissors.
{c}
You lose.''')
    elif computer_choice == 2:
        print(f'''You chose paper. 
{a}             
The computer chose rock. 
{c} 
              You win.''')
else:
    print("You choose a invalid number. You lose LOOSER!")
if your_choice == "2":
    if computer_choice == 0:
        print(f'''You chose scissors.
{c}
The computer chose scissors. 
{c}    
It's a draw.''')
    elif computer_choice == 1:
        print(f'''You chose scissors.
{c}
The computer chose rock.
{a}
You lose.''')
    elif computer_choice == 2:
        print(f'''You chose scissors. 
{c}             
The computer chose paper. 
{b} 
You win.''')
else:
    print("You choose a invalid number. You lose LOOSER!")