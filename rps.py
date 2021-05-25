#rock paper sicssors game
import string
import random

counter = 0
scorePlayer = 0
scoreComputer =0
print("Welcome to the rock paper sicssors game")
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
# playerChoose = input("Hey, please choose 'r' for rock, 'p' for paper, 's' for sicssor: ")
gameOption = [scissors, paper, rock]  #game option!

roundNumber = (int)(input("Please enter the number of rounds:"))   #asking user how many rounds he want to play
while counter != roundNumber:
    userChoose = input("Please Choose 's' for sicssors, 'p' for paper, 'r' for rock:\n")  #asking user for game option
    computerChoose = random.randint(0,2) # computer choose randomly
    counter += 1
    print(computerChoose)
    # print(f"the counter number {counter} \n the round number {roundNumber}")
    if userChoose == 's': 
        print(scissors)
        print(gameOption[computerChoose])
        if computerChoose == 2:
            scoreComputer+=1
        elif computerChoose == 1:
            scorePlayer+=1
        else: 
            continue        
    
    elif userChoose == 'p':
        print(paper)
        print(gameOption[computerChoose]) 
        if computerChoose == 0:
            scoreComputer+=1
        elif computerChoose == 2:
            scorePlayer+=1
        else:
            continue

    elif userChoose == 'r':
        print(rock)
        print(gameOption[computerChoose]) 
        if computerChoose == 1:
            scoreComputer+=1
        elif computerChoose == 0:
            scorePlayer+=1
        else:
            continue        
    print(f"Your score is: {scorePlayer}\n Computer score is: {scoreComputer}")
print(f"Your score is: {scorePlayer}\n Computer score is: {scoreComputer}")
if scorePlayer > scoreComputer:
    print("You win")
elif scoreComputer > scorePlayer:
    print("You lose")
elif scorePlayer == scoreComputer:
    print("Eaqual")        







